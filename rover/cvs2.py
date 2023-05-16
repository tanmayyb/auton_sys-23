"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Code for Computer Vision Sub-System (CVS2) for AR Tag detection, localisation and approach guidance 
    - Turned ON/OFF using topic 'set_cvs2_state' topic
    - Interrupts SearchWalk
    - Gets Target Visual Confirmation (TVC)
    - Signals approach behaviour to 'action_manager'
    - Directs 'rover' approach behaviour 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

import cv2, sys, time
sys.path.append("..")

from threading import Thread, Event

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from rover_utils.msg import TankDriveMsg

from std_msgs.msg import Bool
from std_srvs.srv import Trigger

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.localiser import aruco_localiser
from libs.overlay import overlay_on

from settings.pipeline import *
from settings.states import SM_DICT, SM_INFO

from std_msgs.msg import Bool, Float64

class CVSubSystem(Node):
    def __init__(self):
        super().__init__('cv_subsystem_node')

        """
        TRACKERS
            - subsystem state
            - ARUCO 
            - node events
            - threading
        """


        """
        Cvs2 System Variables
        """
        self.subsystem_state = SM_DICT['idle_scan']
        self.aruco_is_detected = False
        self.aruco_detection_timestamp = None
        
        self.searchwalk_interrupted = False
        self.searchwalk_interruption_thread = None
        self.searchwalk_resume_thread = None

        self.main_thread = None
        self.main_thread_event = None


        """
        Cvs2 Settings
        """
        self.aruco_confimation_wait_time = 0.7 #seconds
        """Cvs2 Stream Settings"""
        self.process_cvs2_overlay_frame = True
        self.show_cvs2_output_locally = False
        self.show_cvs2_output_on_network = True

        """
        LIBS
            - streaming
            - detection
            - localization
            - overlay
        """

        self.stream = streamer()
        self.frame_dims, self.fov = self.stream.get_info()
        self.detector = aruco_detector(self)
        self.localiser = aruco_localiser(self.detector, dims=self.frame_dims, fov=self.fov)
        self.overlay_handler = overlay_on(detector=self.detector, localiser=self.localiser, dims=self.frame_dims) #make this less messy

        """
        ROS2 INTERFACES
        """
        self.set_cvs2_state_subscription = self.create_subscription(
            Bool,
            'set_cvs2_state',
            self.set_cvs2_state_callback,
            10)

        self.interrupt_searchwalk_service_client = self.create_client(
            Trigger, 
            'pause_searchwalk')

        self.resume_searchwalk_service_client = self.create_client(
            Trigger, 
            'resume_searchwalk')

        self.aruco_detection_state_pub = self.create_publisher(
            Bool, 
            'aruco_detection_state',
            10)
        
        self.send_cv_error_pub = self.create_publisher(
            Float64, 
            'cvs2_error_msg',
            10)
        
        """
        https://stackoverflow.com/questions/61394756/how-to-use-opencv-videowriter-with-gstreamer
        """
        self.out_streamer = cv2.VideoWriter(gst_out_command,cv2.CAP_GSTREAMER,0, 20, self.frame_dims, True)


    def set_cvs2_state_callback(self, msg):
        msg = msg.data
        if (msg==True):
            self.get_logger().warn("cvs2 START request received! starting cvs2... ") 
            self.start_subsystem_thread()
        else:
            self.get_logger().warn("cvs2 STOP request received! stopping cvs2... ") 
            self.stop_subsystem_thread()

    def main_subsystem_thread(self):
        self.get_logger().info("cvs2 STARTED!")
        
        while not self.main_thread_event.is_set():
            
            frame = self.process_data()
            
            self.run_state_machine()
                
            self.finalize_iteration(frame)

        #cleanup video pointers
        cv2.destroyAllWindows()
        # self.stream.stop() #this stops the class
        self.get_logger().info("cvs2 STOPPED!") 

    def process_data(self):
        """detect and localise ARUCO markers"""
        ret, frame = self.stream.get_frame()
        # These functions have to occur in this sequence
        self.detector.do_aruco_marker_detection(frame)
        self.localiser.do_localisation()
        return frame

    def run_state_machine(self):
        """
        State Machine for CVS2
        """
        if self.subsystem_state == SM_DICT['idle_scan']:
            """
            IDLE/SCANNING
                - checks for aruco detections
                - interrupts 'action_manager'
            """
            if self.aruco_is_detected:
                
                # OPTIMIZATION, PERFOMANCE ANALYSIS:
                #   how to handle fast false positives at this stage if they exist? 
                #   what if we interrupted but because it was a false positive 
                #   our rover has stopped for nothing.
                #   will it affect the performance of our rover in the competition as a whole?
                
                self.register_aruco_detection_time()
                self.interrupt_searchwalk() 
                self.subsystem_state = SM_DICT['interrupt_searchwalk']

        elif self.subsystem_state == SM_DICT['interrupt_searchwalk']:
            if self.searchwalk_interrupted: #if successfully interrupted
                
                # OPTIMIZATION, PERFOMANCE ANALYSIS: (Persistance of vision)
                #   how to handle fast false positives at this stage if they exist? 
                #   what if we interrupted but because it was a false positive 
                #   our rover has stopped for nothing.
                #   will it affect the performance of our rover in the competition as a whole?
                self.searchwalk_interruption_thread.join()  #reset searchwalk interruption thread
                self.searchwalk_interruption_thread = None
                self.subsystem_state = SM_DICT['confirm_aruco']

        elif self.subsystem_state == SM_DICT['confirm_aruco']:
            """
            CONFIRM ARUCO
                - check for false positives
            """
            #TODO:  envision more robust false positive detection system
            #       maybe add a threshold/buildup function with timeouts to confirm false positives

            if self.aruco_is_detected:
                if self.aruco_signal_confirmed():
                    self.get_logger().warn("Triggering approach behaviour...")
                    self.subsystem_state = SM_DICT['approach']
            else: 
                #false positive
                #TODO:  maybe add a timeout/model for robust false positive
                self.get_logger().warn("false positive detected, resetting CVS2-SM and sW...")
                self.subsystem_state = SM_DICT['reset']

        elif self.subsystem_state == SM_DICT['reset']:
            """
            RESET CVS2
                - resets cvs2 variables
                - resumes searchwalk 
            """
            if self.searchwalk_interrupted:
                if self.searchwalk_resume_thread is None:
                    self.resume_searchwalk()
            else:
                if self.searchwalk_resume_thread is not None:
                    self.searchwalk_resume_thread.join()
                    self.searchwalk_resume_thread = None
                self.subsystem_state = SM_DICT['idle_scan']

            self.reset_cvs2()   #vague function

        elif self.subsystem_state == SM_DICT['approach']: #approach logic
            if self.aruco_is_detected:
                self.publish_approach_error()
            else:
                self.get_logger().warn("aruco not detected, resetting to idle scan...")
                self.subsystem_state = SM_DICT['reset']

    def finalize_iteration(self, frame):
        """
        Overlay functions for debugging and viz purposes
        """
        
        if self.process_cvs2_overlay_frame:
            frame = self.overlay_handler.put_overlay( # overlay handler zips and overlays data 
                frame,
                localiser=self.localiser, 
                use_localiser=True, 
                plot_center_of_mass=True,
                state_text=SM_INFO[self.subsystem_state])        
            """
            Stream Settings
            """
            if self.show_cvs2_output_locally:       self.stream.display_frames(frame)
            if self.show_cvs2_output_on_network:    self.out_streamer.write(frame)

        self.pub_aruco_detection_state_msg()
        self.mainloop = self.stream.check_for_exit_keypresses()

    def reset_cvs2(self):
        self.aruco_detection_timestamp = None
    
    """
    SubSytem Threading
    """
    def start_subsystem_thread(self):    
        if self.main_thread is None:
            self.main_thread_event = Event()
            # create and configure a new thread
            self.main_thread = Thread(target=self.main_subsystem_thread)
            # start the new thread
            self.main_thread.start()

        else:
            print("Subsystem thread is ALREADY running...")

    def stop_subsystem_thread(self):
        """
        about self.main_thread_event.is_set():
        https://superfastpython.com/stop-a-thread-in-python/
        """
        if self.main_thread is not None:
            self.get_logger().info("setting thread event to stop...") 
            self.main_thread_event.set()
            self.main_thread.join()
            self.main_thread = None
        else:
            print("Subsystem thread is NOT running...")


    """
    Interrupt Searchwalk
    """
    def interrupt_searchwalk(self):
        if self.searchwalk_interruption_thread == None:
            self.searchwalk_interruption_thread = Thread(target=self.interrupt_searchwalk_service_thread)
            self.searchwalk_interruption_thread.start()

    def interrupt_searchwalk_service_thread(self):
        self.get_logger().info("signal detected, attempting to interrupt searchwalk...")

        while not self.interrupt_searchwalk_service_client.wait_for_service(timeout_sec=0.5):
            self.get_logger().info('searchwalk interrupt service not available, trying again...')
                
        self.req = Trigger.Request()
        future = self.interrupt_searchwalk_service_client.call_async(self.req)
        future.add_done_callback(self.interrupt_searchwalk_service_callback)

    def interrupt_searchwalk_service_callback(self, future):
        self.searchwalk_interrupted = True
        self.get_logger().warn('interrupt sw signal success!')
    

    """
    Resume Searchwalk
    """
    def resume_searchwalk(self):
        if self.searchwalk_resume_thread == None:
            self.searchwalk_resume_thread = Thread(target=self.resume_searchwalk_service_thread)
            self.searchwalk_resume_thread.start()

    def resume_searchwalk_service_thread(self):
        self.get_logger().info("attempting to resume searchwalk again...")

        while not self.resume_searchwalk_service_client.wait_for_service(timeout_sec=0.5):
            self.get_logger().info('searchwalk resume service not available, trying again...')
                
        self.req = Trigger.Request()
        future = self.resume_searchwalk_service_client.call_async(self.req)
        future.add_done_callback(self.resume_searchwalk_service_callback)

    def resume_searchwalk_service_callback(self, future):
        self.searchwalk_interrupted = False
        self.get_logger().warn('resume sw signal success!')


    """
    Dectection Confirmation
    """
    def aruco_signal_confirmed(self):
        detection_time = time.time() - self.aruco_detection_timestamp
        if detection_time >= self.aruco_confimation_wait_time:
            return True
        return False

    def register_aruco_detection_time(self):
        self.aruco_detection_timestamp = time.time() #register time


    def pub_aruco_detection_state_msg(self):
        msg =  Bool()
        msg.data = self.aruco_is_detected
        self.aruco_detection_state_pub.publish(msg)

    def publish_approach_error(self):
        error = self.localiser.calculate_approach_error()
        msg = Float64()
        msg.data = error
        self.send_cv_error_pub.publish(msg)
        print("[approach_subroutine]: approach_error:\t", error, "[deg]")



def main(args=None):
    rclpy.init(args=args)

    cvs2 = CVSubSystem()

    executor = MultiThreadedExecutor()
    rclpy.spin(cvs2, executor=executor)

    cvs2.destroy()
    rclpy.shutdown()
    exit()


if __name__ == "__main__":
    main()
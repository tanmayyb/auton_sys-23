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

from std_msgs.msg import Empty, Bool
from std_srvs.srv import Trigger

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.processor import aruco_processor
from libs.overlay import overlay_on

from utils.fp_filter import mean_window

from settings.pipeline import *
from settings.cvs2 import SM_DICT, SM_INFO
from settings.fp_filter import *


from std_msgs.msg import Bool, Float64, Int64

class CVSubSystem(Node):
    def __init__(self):
        super().__init__('cv_subsystem_node')

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Print Verbose for User Settings 
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.approach_verbose = False
        self.state_machine_logger_verbose = False
        self.see_filter_activations_verbose = False

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Cvs2 Core System Variables
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.subsystem_state = SM_DICT['idle_scan']
        self.aruco_is_detected = False
        self.min_aruco_distance_approached = False
        
        self.searchwalk_halted = False
        self.searchwalk_interruption_thread_event = None
        self.searchwalk_interruption_thread = None
        self.searchwalk_resume_thread = None

        self.main_thread = None
        self.main_thread_event = None

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Cvs2 FP(False Positive) Filters
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.idle_confirm_filter = mean_window(IDLE_WINDOW_SIZE)
        self.active_confirm_filter = mean_window(ARUCO_COFIRM_WINDOW_SIZE)
        self.reset_to_idle_confirm_filter = mean_window(RESET_WINDOW_SIZE)
        """Cvs2 FP Filter Activations"""
        self.idle_aruco_confirm_activation = 0.0 
        self.active_confirm_activation = 0.0
        self.reset_to_idle_activation = 0.0
        self.idle_confirm_filter.reg_time(None)
        self.active_confirm_filter.reg_time(None)
        self.reset_to_idle_confirm_filter.reg_time(None)
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Cvs2 Graphic I/O and Overlay
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        """Cvs2 Stream Settings"""
        self.process_cvs2_overlay_frame = True
        self.show_cvs2_output_locally = False
        self.show_cvs2_output_on_network = True

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        CORE CVS2 LIBS:
            - streaming
            - detection
            - processing
            - overlay
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.stream = streamer()
        self.frame_dims, self.fov = self.stream.get_info()
        self.detector = aruco_detector(self)
        self.processor = aruco_processor(self.detector, dims=self.frame_dims, fov=self.fov)
        self.overlay_handler = overlay_on(detector=self.detector, processor=self.processor, dims=self.frame_dims) #make this less messy

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        ROS2 INTERFACES
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        CVS2 INTERFACES
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.set_cvs2_state_subscription = self.create_subscription(
            Bool,
            'set_cvs2_state',
            self.set_cvs2_state_callback,
            10)

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        SEARCHWALK INTERFACES
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
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
        
        self.succesful_searchwalk_pub = self.create_publisher(
            Empty, 
            'successful_searchwalk',
            10)
        
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        USER DEBUGGING INTERFACES
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.toggle_cvs2_state_subscription = self.create_subscription(
            Empty,
            'toggle_cvs2_state',
            self.toggle_cvs2_state_callback,
            10)
        self.reset_sW_interruptor_subscription = self.create_subscription(
            Empty,
            'reset_cvs2_sW_interrupt',
            self.reset_sW_interrupt,
            10)

        self.state_publisher = self.create_publisher(
            Int64, 
            'cvs2_state',
            10)
        cvs2_state_pub_timer_period  = 0.2
        self.create_timer(cvs2_state_pub_timer_period, self.state_timer_callback)

        """
        https://stackoverflow.com/questions/61394756/how-to-use-opencv-videowriter-with-gstreamer
        """
        print("\nwaiting for cvs2 input frames...")
        self.out_streamer = cv2.VideoWriter(gst_out_command,cv2.CAP_GSTREAMER,0, 20, self.frame_dims, True)
        print("received frames...")
        print("------------CVS2 CREATED------------") 



    def set_cvs2_state_callback(self, msg):
        msg = msg.data
        if (msg==True):
            self.get_logger().warn("cvs2 start request received. starting cvs2... ") 
            self.start_subsystem_thread()
        else:
            self.get_logger().warn("cvs2 stop request received. stopping cvs2... ") 
            self.stop_subsystem_thread()

    def main_subsystem_thread(self):
        self.get_logger().warning("cvs2 subsystem launched...")
        
        while not self.main_thread_event.is_set():
            
            frame = self.process_data()
            
            self.run_state_machine()
                
            self.finalize_iteration(frame)

        #cleanup video pointers
        cv2.destroyAllWindows()
        # self.stream.stop() #this stops the class
        #self.get_logger().info("cvs2 stopped!") 

    def process_data(self):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        PROCESS DATA
        This function does:
            - processing of frame to detect and localise ARUCO markers
            - find and update distance to markers
            - updates and calculates mean sum of signal windows/FP (False-Positive) Filters
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        """detect and localise ARUCO markers"""
        ret, frame = self.stream.get_frame()
        # These functions have to occur in this sequence
        self.detector.do_aruco_marker_detection(frame)
        self.processor.do_aruco_processing()

        """update filter windows"""
        self.idle_aruco_confirm_activation = self.idle_confirm_filter.update_and_get_activation(self.aruco_is_detected)
        self.active_confirm_activation = self.active_confirm_filter.update_and_get_activation(self.aruco_is_detected)
        self.reset_to_idle_activation = self.reset_to_idle_confirm_filter.update_and_get_activation(self.aruco_is_detected)

        """update min_aruco_distance_approached"""
        self.min_aruco_distance_approached = self.processor.get_min_aruco_distance_approached()

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
            if self.idle_aruco_confirm_activation >= IDLE_ARUCO_CONFIRM_THRESHOLD:                 #Rover saw the Tag for a brief second/IDLE_ARUCO_CONFIRM_THRESHOLD                               
                self.active_confirm_filter.reg_time(time.time())
                if not self.searchwalk_halted:
                    self.interrupt_searchwalk() 
                    self.subsystem_state = SM_DICT['interrupt_searchwalk']
                else:
                    self.subsystem_state = SM_DICT['confirm_aruco']

        elif self.subsystem_state == SM_DICT['interrupt_searchwalk']:
            if self.searchwalk_halted:
                self.searchwalk_interruption_thread.join()  
                self.searchwalk_interruption_thread = None
                self.subsystem_state = SM_DICT['confirm_aruco']

        elif self.subsystem_state == SM_DICT['confirm_aruco']:
            """
            CONFIRM ARUCO
                - check for false positives
            """
            if self.active_confirm_activation >= IDLE_ARUCO_CONFIRM_THRESHOLD: 
                if self.active_confirm_filter.is_timeout(time.time(), ARUCO_COFIRM_TIMEOUT):
                    self.get_logger().info("approaching...")
                    self.subsystem_state = SM_DICT['approach']
            else: 
                self.state_machine_logger_verbose: self.get_logger().info("FP detection spotted...")  
                self.put_sm_into_reset()

        elif self.subsystem_state == SM_DICT['approach']: #approach logic
            if self.active_confirm_activation >= ACTIVE_ARUCO_CONFIRM_ACTIVATION:
                if self.min_aruco_distance_approached:
                    self.get_logger().warn("aruco tag(s) reached!")
                    self.subsystem_state = SM_DICT['aruco_reached']
                else:
                    self.approach_aruco_markers()
            else:
                self.state_machine_logger_verbose: self.get_logger().warn("lost active aruco confirm...")
                self.put_sm_into_reset()

        elif self.subsystem_state == SM_DICT['aruco_reached']:
            msg = Empty()
            self.succesful_searchwalk_pub.publish(msg)
            self.subsystem_state = SM_DICT['standby']

        elif self.subsystem_state == SM_DICT['standby']:

            pass

        elif self.subsystem_state == SM_DICT['reset']:
            """
            RESET CVS2
                - resets cvs2 variables
                - resumes searchwalk/handles poor aruco detection states
            """
            if self.reset_to_idle_confirm_filter.is_timeout(time.time(), RESET_TO_IDLE_CONFIRM_TIMEOUT):
                if self.searchwalk_halted:
                    self.resume_searchwalk()
                else:                              
                    if self.searchwalk_resume_thread is not None:
                        self.searchwalk_resume_thread.join()
                        self.searchwalk_resume_thread = None
                    self.subsystem_state = SM_DICT['idle_scan']
            else: 
                if self.idle_aruco_confirm_activation < IDLE_ARUCO_CONFIRM_THRESHOLD:
                    self.do_something_to_get_higher_activation()
                else:
                    self.subsystem_state = SM_DICT['confirm_aruco']

    def finalize_iteration(self, frame):
        """
        Overlay functions for debugging and viz purposes
        """
        
        if self.process_cvs2_overlay_frame:
            frame = self.overlay_handler.put_overlay( # overlay handler zips and overlays data 
                frame,
                processor=self.processor, 
                use_processor=True, 
                plot_center_of_mass=True,
                state_text=SM_INFO[self.subsystem_state])        
            """
            Stream Settings
            """
            if self.show_cvs2_output_locally:       self.stream.display_frames(frame)
            if self.show_cvs2_output_on_network:    self.out_streamer.write(frame)

        if self.see_filter_activations_verbose: print(self.idle_aruco_confirm_activation, self.active_confirm_activation, self.reset_to_idle_activation)
        
        self.pub_aruco_detection_state_msg()
        self.mainloop = self.stream.check_for_exit_keypresses()
    
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
            self.main_thread_event.set()
            self.main_thread.join()
            self.main_thread = None
            self.get_logger().warn("subsystem thread stopped") 
            self.set_default_cvs2_states()
        else:
            print("attempted to stop subsystem thread, but it is not running...")

    def set_default_cvs2_states(self):
        self.subsystem_state = SM_DICT['idle_scan']
        self.processor.set_default_states()

    """
    Interrupt Searchwalk
    """
    def interrupt_searchwalk(self):
        if self.searchwalk_interruption_thread == None:
            self.searchwalk_interruption_thread_event = Event()
            self.searchwalk_interruption_thread = Thread(target=self.interrupt_searchwalk_service_thread)
            self.searchwalk_interruption_thread.start()

    def interrupt_searchwalk_service_thread(self):
        """
        https://stackoverflow.com/questions/18018033/how-to-stop-a-looping-thread-in-python
        """
        if self.state_machine_logger_verbose: self.get_logger().info("signal detected, interrupting searchwalk...")

        
        while (not self.searchwalk_interruption_thread_event.is_set()) and (not self.interrupt_searchwalk_service_client.wait_for_service(timeout_sec=0.5)):
            if self.state_machine_logger_verbose: self.get_logger().info('searchwalk interrupt service not available, trying again...')

        if not self.searchwalk_interruption_thread_event.is_set():
            self.req = Trigger.Request()
            future = self.interrupt_searchwalk_service_client.call_async(self.req)
            future.add_done_callback(self.interrupt_searchwalk_service_callback)

    def interrupt_searchwalk_service_callback(self, future):
        self.searchwalk_halted = True
        if self.state_machine_logger_verbose: self.get_logger().info('searchwalk interrupt success...')
    

    """
    Resume Searchwalk
    """
    def resume_searchwalk(self):
        if self.searchwalk_resume_thread == None:
            self.searchwalk_resume_thread = Thread(target=self.resume_searchwalk_service_thread)
            self.searchwalk_resume_thread.start()

    def resume_searchwalk_service_thread(self):
        if self.state_machine_logger_verbose: self.get_logger().info("attempting to resume searchwalk again...")

        while not self.resume_searchwalk_service_client.wait_for_service(timeout_sec=0.5):
            if self.state_machine_logger_verbose: self.get_logger().info('searchwalk resume service not available, trying again...')
                
        self.req = Trigger.Request()
        future = self.resume_searchwalk_service_client.call_async(self.req)
        future.add_done_callback(self.resume_searchwalk_service_callback)

    def resume_searchwalk_service_callback(self, future):
        self.searchwalk_halted = False
        if self.state_machine_logger_verbose: self.get_logger().info('resume sw signal success!')


    """
    Reset Functions
    """
    def put_sm_into_reset(self):
        if self.state_machine_logger_verbose: self.get_logger().info('resetting...')
        self.reset_to_idle_confirm_filter.reg_time(time.time())
        self.subsystem_state = SM_DICT['reset']
    
    def do_something_to_get_higher_activation(self):
        self.publish_approach_error(0)

    """
    SM Processing
    """
    def approach_aruco_markers(self):
        error = self.processor.calculate_approach_error()
        self.publish_approach_error(error)

    """
    PUBLISHING MESSAGES
    """
    def pub_aruco_detection_state_msg(self):
        msg =  Bool()
        msg.data = self.aruco_is_detected
        self.aruco_detection_state_pub.publish(msg)

    def publish_approach_error(self, error):
        if error is not  None:
            msg = Float64()
            msg.data = float(error)
            self.send_cv_error_pub.publish(msg)
            if self.approach_verbose: print("[approach_subroutine]: approach_error:\t", error, "[deg]")


    """
    USEFUL DEBUGGING INTERFACES
    """
    def toggle_cvs2_state_callback(self, msg): 
        self.get_logger().info("state toggle requested...")
        if self.main_thread is None:
            self.start_subsystem_thread()
        else:
            self.stop_subsystem_thread()

    def reset_sW_interrupt(self, msg):

        self.get_logger().warn("request to stop cvs2 sW interrupt received... ") 
        if self.searchwalk_interruption_thread == None:
            print("Subsystem thread is NOT running...")            
        else:
            print("stopping searchwalk_interruption_thread... ") 
            self.searchwalk_interruption_thread_event.set()
            self.searchwalk_interruption_thread.join()
            self.searchwalk_interruption_thread = None
            print("resetting... ") 
            self.subsystem_state = SM_DICT['reset']

    def state_timer_callback(self):
        msg = Int64()
        msg.data = self.subsystem_state
        self.state_publisher.publish(msg)



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
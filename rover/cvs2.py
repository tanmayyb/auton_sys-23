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
from libs.controller import pid_controller

from settings.pid import *
from settings.states import *
from settings.pipeline import *

from std_msgs.msg import Bool

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
        self.subsystem_state = SM_DICT['idle_scan']
        self.aruco_is_detected = False
        self.aruco_detection_timestamp = None
        self.aruco_confimation_wait_time = 0.7 #seconds
        self.searchwalk_interrupted = False
        self.searchwalk_interruption_thread = None
        self.main_thread = None
        self.main_thread_event = None

        """
        LIBS
            - streaming
            - detection
            - localization
            - overlay
            - pid
        """
        self.stream = streamer()
        self.frame_dims = self.stream.get_frame_dims()
        self.detector = aruco_detector(self)
        self.localiser = aruco_localiser(self.detector, dims=self.frame_dims)
        self.pid = pid_controller(self.localiser, self.frame_dims, pid_const=PID_TUNING_CONSTS)
        self.overlay_handler = overlay_on(detector=self.detector, localiser=self.localiser, controller=self.pid, dims=self.frame_dims) #make this less messy

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
            'halt_searchwalk')

        self.send_cv_pid_vals_pub = self.create_publisher(
            TankDriveMsg, 
            'drive_msg',
            10)

        self.aruco_detection_state_pub = self.create_publisher(
            Bool, 
            'aruco_detection_state',
            10)
        
        """
        https://stackoverflow.com/questions/61394756/how-to-use-opencv-videowriter-with-gstreamer
        """
        self.out_streamer = cv2.VideoWriter(gst_out_command,cv2.CAP_GSTREAMER,0, 20, self.frame_dims, True)

        #remove
        self.start_subsystem_thread()

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
        self.pid_vals = self.pid.get_pid_c2mm()
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
                self.register_aruco_detection_time()
                #self.interrupt_searchwalk() 
                #self.subsystem_state = SM_DICT['interrupt_searchwalk']
                self.subsystem_state = SM_DICT['confirm_aruco']

        elif self.subsystem_state == SM_DICT['interrupt_searchwalk']:
            if self.searchwalk_interrupted: #if successfully interrupted
                self.subsystem_state = SM_DICT['confirm_aruco']
                #reset searchwalk
                self.searchwalk_interruption_thread.join()
                self.searchwalk_interruption_thread = None
                self.searchwalk_interrupted = False
            # how to handle fast false positives at this stage if they exist? 

        elif self.subsystem_state == SM_DICT['confirm_aruco']:
            """
            CONFIRM ARUCO
                - check for false positives
            """
            if self.aruco_is_detected:
                if self.aruco_signal_confirmed():
                    self.get_logger().warn("Triggering approach behaviour...")
                    self.subsystem_state = SM_DICT['approach']
            else: 
                #false positive
                self.subsystem_state = SM_DICT['reset']

        elif self.subsystem_state == SM_DICT['reset']:
            """
            RESET LOGIC
                - resets cvs2
                - resumes 'action_manager' 
            """
            #add function to resume manager's goals
            self.searchwalk_interrupted = False
            self.aruco_detection_timestamp = None
            self.subsystem_state = SM_DICT['idle_scan']

        elif self.subsystem_state == SM_DICT['approach']:
            #approach logic
            if self.aruco_is_detected:
                val = self.pid.get_pid_c2mm()
                if val is not None:
                    leftval, rightval = val
                    msg = TankDriveMsg()
                    msg.lpwm = leftval
                    msg.rpwm = rightval
                    self.send_cv_pid_vals_pub.publish(msg)
                    self.get_logger().info("approaching target...")
            else:
                self.get_logger().warn("aruco not detected, resetting to idle scan...")
                self.subsystem_state = SM_DICT['reset']

    def finalize_iteration(self, frame):
        """
        Overlay functions for debugging and viz purposes
        """
        frame = self.overlay_handler.put_overlay( # overlay handler zips and overlays data 
            frame,
            localiser=self.localiser, 
            use_localiser=True, 
            controller=self.pid, 
            plot_center_of_mass=True,
            state_text=SM_INFO[self.subsystem_state])
        
        #self.stream.display_frames(frame)
        self.out_streamer.write(frame)
        self.mainloop = self.stream.check_for_exit_keypresses()
        self.pub_aruco_detection_state_msg()

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

    def register_aruco_detection_time(self):
        self.aruco_detection_timestamp = time.time() #register time

    def interrupt_searchwalk(self):
        if self.searchwalk_interruption_thread == None:
            self.searchwalk_interruption_thread = Thread(target=self.interrupt_searchwalk_service_thread)
            self.searchwalk_interruption_thread.start()

    def interrupt_searchwalk_service_thread(self):
        self.get_logger().info("signal detected, attempting to interrupt searchwalk")

        while not self.interrupt_searchwalk_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('searchwalk interrupt service not available, trying again...')
                
        self.req = Trigger.Request()
        future = self.interrupt_searchwalk_service_client.call_async(self.req)
        future.add_done_callback(self.interrupt_searchwalk_service_callback)

    def interrupt_searchwalk_service_callback(self, future):
        self.get_logger().warn('interrupt signal success!')
        self.searchwalk_interrupted = True

    def aruco_signal_confirmed(self):
        detection_time = time.time() - self.aruco_detection_timestamp
        if detection_time >= self.aruco_confimation_wait_time:
            return True
        return False

    def pub_aruco_detection_state_msg(self):
        msg =  Bool()
        msg.data = self.aruco_is_detected
        self.aruco_detection_state_pub.publish(msg)

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
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

from std_msgs.msg import Bool
from std_srvs.srv import Trigger

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.localiser import aruco_localiser
from libs.overlay import overlay_on
from libs.controller import pid_controller

from settings.pid import *

class CVSubSystem(Node):
    def __init__(self):
        super().__init__('cv_subsystem')

        self.stream = streamer()
        self.frame_dims = self.stream.get_frame_dims()

        self.detector = aruco_detector()
        self.localiser = aruco_localiser(self.detector, dims=self.frame_dims)
        self.overlay_handler = overlay_on(self.detector, dims=self.frame_dims)
        self.pid = pid_controller(self.localiser, self.frame_dims, pid_const=PID_TUNING_CONSTS)

        self.set_cvs2_state_subscription = self.create_subscription(
            Bool,
            'set_cvs2_state',
            self.set_cvs2_state_callback,
            10)

        self.interrupt_searchwalk_service_client = self.create_client(
            Trigger, 
            'halt_searchwalk')

        self.thread = None
        self.event = None

        self.sm_dict = {
            'idle_scan':0,
            'confirm_aruco':1,
            'approach':2,
            'reset':3}

        self.sm_info = ['READY/SCANNING','CONFIRMING...','APPROACHING','RESETING']
        self.subsystem_state = self.sm_dict['idle_scan']
        
        self.aruco_detected = False
        self.aruco_detection_timestamp = None
        self.aruco_confimation_time = 4.0 #seconds

        self.searchwalk_interrupted = False



    def set_cvs2_state_callback(self, msg):
        msg = msg.data
        if (msg==True):
            self.get_logger().warn("cvs2 START request received! starting cvs2... ") 
            self.start_subsystem_thread()
        else:
            self.get_logger().warn("cvs2 STOP request received! stopping cvs2... ") 
            self.stop_subsystem_thread()

    def main_subsystem_thread(self):
        """
        https://superfastpython.com/stop-a-thread-in-python/
        """
        self.get_logger().info("cvs2 STARTED!")

        while not self.event.is_set():
            ret, frame = self.stream.get_frame()

            # detector detects 
            self.detector.do_aruco_marker_detection(frame)
            self.aruco_detected = self.detector.is_aruco_detected()
            

            """
            State Machine for CVS2
            """
            self.run_state_machine()

            #localisation for pid error calc and overlay
            self.localiser.do_localisation()  
            
            """
            Overlay functions for debugging and viz purposes
            """
            frame = self.overlay_handler.put_overlay( # overlay handler zips and overlays data 
                frame,
                localiser=self.localiser, 
                use_localiser=True, 
                controller=self.pid, 
                plot_center_of_mass=True,
                state_text=self.sm_info[self.subsystem_state])
            self.stream.display_frames(frame)
            self.mainloop = self.stream.check_for_exit_keypresses()

        #cleanup video pointers
        cv2.destroyAllWindows()
        # self.stream.stop() #this stops the class
        self.get_logger().info("cvs2 STOPPED!") 

    def run_state_machine(self):
        """
        STATE MACHINE PROGRAM
        """
        
        if self.subsystem_state == self.sm_dict['idle_scan']:
            """
            IDLE/SCANNING
                - checks for aruco detections
                - interrupts 'action_manager'
            """
            if self.aruco_detected:
                self.register_aruco_detection_time()
                #self.interrupt_searchwalk()
                self.subsystem_state = self.sm_dict['confirm_aruco']

        elif self.subsystem_state == self.sm_dict['confirm_aruco']:
            """
            CONFIRM ARUCO
                - check for false positives
            """
            if self.aruco_detected:
                if self.aruco_signal_confirmed():
                    self.subsystem_state = self.sm_dict['approach']
            else: 
                #false positive
                self.subsystem_state = self.sm_dict['reset']

        elif self.subsystem_state == self.sm_dict['reset']:
            """
            RESET LOGIC
                - resets cvs2
                - resumes 'action_manager' 
            """
            #add function to resume manager's goals
            self.searchwalk_interrupted = False
            self.aruco_detection_timestamp = None
            self.subsystem_state = self.sm_dict['idle_scan']

        elif self.subsystem_state == self.sm_dict['approach']:
            self.get_logger().warn("Triggering approach behaviour...")
            self.subsystem_state = self.sm_dict['reset']
            #approach logic

    def start_subsystem_thread(self):    
        if self.thread is None:
            self.event = Event()
            # create and configure a new thread
            self.thread = Thread(target=self.main_subsystem_thread)
            # start the new thread
            self.thread.start()

        else:
            print("Subsystem thread is ALREADY running...")

    def stop_subsystem_thread(self):
        if self.thread is not None:
            self.get_logger().info("setting thread event to stop...") 
            self.event.set()
            self.thread.join()
            self.thread = None
        else:
            print("Subsystem thread is NOT running...")

    def register_aruco_detection_time(self):
        self.aruco_detection_timestamp = time.time() #register time

    def interrupt_searchwalk(self):
        if not self.searchwalk_interrupted:
            self.get_logger().info("signal detected, attempting to interrupt searchwalk")

            while not self.interrupt_searchwalk_service_client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('searchwalk interrupt service not available, trying again...')
                    
            self.req = Trigger.Request()
            future = self.interrupt_searchwalk_service_client.call_async(self.req)
            future.add_done_callback(self.interrupt_searchwalk_service_callback)
            self.searchwalk_interrupted = True

    def interrupt_searchwalk_service_callback(self, future):
        self.get_logger().info('searchwalk succesfully interrupted...')
    
    def aruco_signal_confirmed(self):
        detection_time = time.time() - self.aruco_detection_timestamp
        if detection_time >= self.aruco_confimation_time:
            return True
        return False

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
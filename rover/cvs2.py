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

import cv2,sys
sys.path.append("..") 

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Bool

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.localiser import aruco_localiser
from libs.overlay import overlay_on
from libs.controller import pid_controller
from libs.sender import teensy_sender

from settings.pid import *

from threading import Thread, Event
    
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

        self.thread = None
        self.event = None

    def set_cvs2_state_callback(self, msg):
        msg = msg.data
        if (msg==True):
            self.get_logger().warn("cvs2 START request received! starting cvs2... ") 
            self.start_subsystem_thread()
        else:
            self.get_logger().warn("cvs2 STOP request received! stopping cvs2... ") 
            self.stop_subsystem_thread()

    def subsystem_thread(self):
        """
        https://superfastpython.com/stop-a-thread-in-python/
        """
        self.get_logger().info("cvs2 STARTED!")

        while not self.event.is_set():
            ret, frame = self.stream.get_frame()

            # detector detects 
            self.detector.detect_aruco_marker(frame)
            self.localiser.do_localisation()
            
            val = self.pid.get_pid_c2mm()        
            if(val != None):
                print(val, self.pid.fetch_error())

            """
            Overlay functions for debugging and viz purposes
            """
            frame = self.overlay_handler.put_overlay( # overlay handler zips and overlays data 
                frame,
                localiser=self.localiser, 
                use_localiser=True, 
                controller=self.pid, 
                plot_center_of_mass=True)

            self.stream.display_frames(frame)
            self.mainloop = self.stream.check_for_exit_keypresses()

        #cleanup video pointers
        cv2.destroyAllWindows()
        # self.stream.stop() #this stops the class
        self.get_logger().info("cvs2 STOPPED!") 

    def start_subsystem_thread(self):    
        if self.thread is None:
            self.event = Event()
            # create and configure a new thread
            self.thread = Thread(target=self.subsystem_thread)
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
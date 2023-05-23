from tkinter import *
from turtle import color

import rclpy
from rclpy.node import Node

from std_msgs.msg import Empty, Bool
from std_srvs.srv import Trigger

from rclpy.executors import MultiThreadedExecutor
from threading import Thread

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        
        self.INTERFACE_SEARCHWALK = True
         
        self.toggle_cvs2_pub = self.create_publisher(Empty, 'toggle_cvs2_state', 10)
        self.reset_cvs2_sW_inttr_pub = self.create_publisher(Empty, 'reset_cvs2_sW_interrupt', 10)
        self.state = False

        self.pause_searchwalk_service = None
        self.resume_searchwalk_service = None
       
        if self.INTERFACE_SEARCHWALK:
            self.pause_searchwalk_service = self.create_service(
                Trigger, 
                'pause_searchwalk', 
                self.pause_searchwalk_callback)

            self.resume_searchwalk_service = self.create_service(
                Trigger,
                'resume_searchwalk',
                self.resume_searchwalk_callback)
        #

    def toggle_cvs2(self):
        msg = Empty()
        self.toggle_cvs2_pub.publish(msg)
        print("toggle toggle_cvs2_state sent")

    def reset_cvs2_sW_inttr(self):
        msg = Empty()
        self.reset_cvs2_sW_inttr_pub.publish(msg)
        print("interrupt reset_cvs2_sW_interrupt sent")
        

    def publish(self):
        msg = Bool()
        self.state = not self.state
        msg.data = self.state
        self.publisher.publish(msg)
        print('set_cvs2_state = ON = ', self.state)

    
    def pause_searchwalk_callback(self, request, response):
        self.get_logger().warn('pause sW request received...accepting...')
        response.success = True  
        return response

    def resume_searchwalk_callback(self, request, response):
        self.get_logger().warn('resume sW request received...accepting...')
        response.success = True  
        return response


def on_click1(publisher,msg):
    publisher.toggle_cvs2()

def on_click2(publisher, msg):
    publisher.reset_cvs2_sW_inttr()

def main(args=None):
    rclpy.init()

    cvs2 = MinimalPublisher()

    executor = MultiThreadedExecutor()
    executor.add_node(cvs2)
    executor_thread = Thread(
        target=executor.spin, 
        daemon=True)
    executor_thread.start()
    root = Tk()

    button1 = Button(root, bg="white", command=lambda msg = None: on_click1(cvs2, msg), padx= 50, pady= 50, text="toggle cvs2 state")
    button2 = Button(root, bg="white", command=lambda msg = None: on_click2(cvs2, msg), padx= 50, pady= 50, text="reset cvs2 sW interrupt")
    

    button1.pack()
    button2.pack()

    root.mainloop()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
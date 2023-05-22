from tkinter import *
from turtle import color

import rclpy
from rclpy.node import Node

from std_msgs.msg import Empty, Bool


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.toggle_cvs2_pub = self.create_publisher(Empty, 'toggle_cvs2_state', 10)
        self.reset_cvs2_sW_inttr_pub = self.create_publisher(Empty, 'reset_cvs2_sW_interrupt', 10)
        self.state = False
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

def on_click1(publisher,msg):
    publisher.toggle_cvs2()

def on_click2(publisher, msg):
    publisher.reset_cvs2_sW_inttr()

def main(args=None):
    rclpy.init()

    pub = MinimalPublisher()
    root = Tk()

    button1 = Button(root, bg="white", command=lambda msg = None: on_click1(pub, msg), padx= 50, pady= 50, text="toggle cvs2 state")
    button2 = Button(root, bg="white", command=lambda msg = None: on_click2(pub, msg), padx= 50, pady= 50, text="reset cvs2 sW interrupt")
    

    button1.pack()
    button2.pack()

    root.mainloop()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
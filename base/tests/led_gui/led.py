from tkinter import *
from turtle import color

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Int64, 'led_msg', 10)

    def publish(self, num):
        msg = Int64()
        msg.data = num
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def on_click(publisher,msg):
    publisher.publish(msg)

def main(args=None):
    rclpy.init()

    pub = MinimalPublisher()
    root = Tk()

    button1 = Button(root, bg="black", command=lambda msg = 0: on_click(pub, msg), padx= 50, pady= 50, text="0")
    button2 = Button(root, bg="red", command=lambda msg = 1: on_click(pub, msg), padx= 50, pady= 50, text="1")
    button3 = Button(root, bg="green", command=lambda msg = 2: on_click(pub, msg), padx= 50, pady= 50, text="2")
    button4 = Button(root, bg="blue", command=lambda msg = 3: on_click(pub, msg), padx= 50, pady= 50, text="3")
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    root.mainloop()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
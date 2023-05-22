from tkinter import *
from turtle import color

import rclpy
from rclpy.node import Node

from std_msgs.msg import Empty


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Empty, 'launch_green_flash', 10)

    def publish(self):
        msg = Empty()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: Empty Trigger')

def on_click(publisher,msg):
    publisher.publish()

def main(args=None):
    rclpy.init()

    pub = MinimalPublisher()
    root = Tk()

    button1 = Button(root, bg="white", command=lambda msg = 0: on_click(pub, msg), padx= 50, pady= 50, text="launch led subrtn")
    button1.pack()

    root.mainloop()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
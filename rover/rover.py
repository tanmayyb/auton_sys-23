"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16

class Rover(Node):
    def __init__(self):

        self.state = 0
        self.state_dict = {
            "Initializing": 0,
            "Standby": 1,
            "Transit": 2,
            "Teleop": 3}

        """
        location and attitude trackers
        """
        self.rover_lat = None
        self.rover_lon = None

        self.state_publisher = self.create_publisher(
            Int16(),
            'state_topic',
            10)

        self.lhrs_subscriber = self.create_subscription(
            Int16(),
            'pose_topic',
            self.update_pose_trackers)

    def update_pose_trackers(self, msg):
        pass
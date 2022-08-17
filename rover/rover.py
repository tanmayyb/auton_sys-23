"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from rover_utils.action import MinimalWalk

from std_msgs.msg import Int16


class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')
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

        self.pose_subscriber = self.create_subscription(
            Int16(),
            'pose_topic',
            self.update_pose_trackers,
            10)

        self._action_server = ActionServer(
            self,
            MinimalWalk,
            'action_topic',
            self.execute_minimal_walk_callback)

        
        print("initialised")

    def update_pose_trackers(self, msg):
        pass
    
    def execute_minimal_walk_callback(self, goal_handle):
        # self.position = goal_handle.request.position

        # feedback_msg = MinimalWalk.Feedback()
        # import time
        # for i in range(10):
        #     feedback_msg.d2t = i*10
        #     feedback_msg.he = i*1.3
        #     goal_handle.publish_feedback(feedback_msg)
        #     time.sleep(1)

        # goal_handle.succeed()

        result = MinimalWalk.Result()
        result.sequence = 1
        return result

def main(args=None):
    rclpy.init(args=args)

    rover_node = Rover()

    rclpy.spin(rover_node)


if __name__ == '__main__':
    main()
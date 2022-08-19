"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

#from geometry_msgs.msg import Point

from action_tutorials_interfaces.action import Fibonacci
from rover_utils.action import MinimalWalk

import time


class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')
        # self.state = 0
        # self.state_dict = {
        #     "Initializing": 0,
        #     "Standby": 1,
        #     "Transit": 2,
        #     "Teleop": 3}

        """
        location and attitude trackers
        """
        # self.rover_lat = None
        # self.rover_lon = None

        # self.state_publisher = self.create_publisher(
        #     Int16(),
        #     'state_topic',
        #     10)

        # self.pose_subscriber = self.create_subscription(
        #     Int16(),
        #     'pose_topic',
        #     self.update_pose_trackers,
        #     10)

        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'mini_walk_act',
            self.minimal_walk_callback)

        # self.msg_sub = self.create_subscription(
        #     TestMsg,
        #     'topic',
        #     self.handle_sub,
        #     10)

        # self._action_server = ActionServer(
        #     self,
        #     Fibonacci,
        #     'fibonacci',
        #     self.execute_callback)

        print("rover_node initialised")

    
    # def handle_sub(self, msg):
    #     self.get_logger().info('Got Result: "%d"' % msg.my_float)
    #     print(msg.point)

    def minimal_walk_callback(self, goal_handle):

        print("received goal request", goal_handle.request)
        coords = goal_handle.request.coords
        print("received coords: ", coords.x, coords.y)

        self.get_logger().info('Executing Goal...')

        feedback_msg = MinimalWalk.Feedback()

        for i in range(10):
            
            feedback_msg.d2t = float(i*4.2)
            feedback_msg.he = float(i*6.9)

            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()

        result = MinimalWalk.Result()
        result.result = True

        return result

    # def execute_callback(self, goal_handle):
    #     self.get_logger().info('Executing goal...')

    #     feedback_msg = Fibonacci.Feedback()
    #     feedback_msg.partial_sequence = [0, 1]

    #     for i in range(1, goal_handle.request.order):
    #         feedback_msg.partial_sequence.append(
    #             feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
    #         self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
    #         goal_handle.publish_feedback(feedback_msg)
    #         time.sleep(1)

    #     goal_handle.succeed()

    #     result = Fibonacci.Result()
    #     result.sequence = feedback_msg.partial_sequence
    #     return result

    # def update_pose_trackers(self, msg):
    #     pass
    

def main(args=None):
    rclpy.init(args=args)

    rover_node = Rover()

    rclpy.spin(rover_node)


if __name__ == '__main__':
    main()
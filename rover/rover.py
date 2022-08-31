"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


from action_tutorials_interfaces.action import Fibonacci
from rover_utils.action import MinimalWalk

import time


class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')

        print("rover_node initialised")

        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'mini_walk_act',
            execute_callback=self.exec_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,)

    def goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        # This server allows multiple goals in parallel
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def exec_callback(self, goal_handle):

        print("received goal request", goal_handle.request)
        coords = goal_handle.request.coords
        print("received coords: ", coords.x, coords.y)

        self.get_logger().info('Executing Goal...')

        feedback_msg = MinimalWalk.Feedback()

        
        for i in range(10):

            """cancel codition to close callback w/o execution blocking"""
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return MinimalWalk.Result()


            feedback_msg.d2t = float(i*4.2)
            feedback_msg.he = float(i*6.9)

            goal_handle.publish_feedback(feedback_msg)
            time.sleep(.5)

        goal_handle.succeed()

        result = MinimalWalk.Result()
        result.result = True

        self.get_logger().info('Goal Executed!...')

        return result


def main(args=None):
    rclpy.init(args=args)

    rover_node = Rover()

    executor = MultiThreadedExecutor()

    try:
        rclpy.spin(rover_node, executor=executor)
    except:
        rclpy.shutdown()

if __name__ == '__main__':
    
    main()




        # self.state = 0
        # self.state_dict = {
        #     "Initializing": 0,
        #     "Standby": 1,
        #     "Transit": 2,
        #     "Teleop": 3}
 
        # """
        # location and attitude trackers
        # """
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


    
    # def handle_sub(self, msg):
    #     self.get_logger().info('Got Result: "%d"' % msg.my_float)
    #     print(msg.point)


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
    
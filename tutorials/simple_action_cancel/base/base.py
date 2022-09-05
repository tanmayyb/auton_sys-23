from pickle import FALSE, TRUE
from rclpy.node import Node
from rclpy.action import ActionClient



from geometry_msgs.msg import Point

from rover_utils.action import MinimalWalk
from rover_utils.msg import TankDriveMsg

import time 

class baseNode(Node):

    def __init__(self, parent = None):
        super().__init__('base_node')
        
        self.parent = parent

        self.minimal_walk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'point_to_point_minimal_walk')

        self.teensy_teleop = self.create_publisher(
            TankDriveMsg,
            'pwm_to_teensy',
            10)
    
    def send_goal_miniwalk(self,tlat,tlon):
        
        """CREATE GOAL MSG"""
        coords  = Point()
        coords.x = tlat
        coords.y = tlon
        coords.z = 0.0

        """SEND GOAL MSG"""
        minimal_walk_goal_msg = MinimalWalk.Goal()
        minimal_walk_goal_msg.coords = coords
        minimal_walk_goal_msg.use_guidance = False
        minimal_walk_goal_msg.signal_and_wait = False
        
        self.minimal_walk_action_client.wait_for_server()  

        send_goal_future = self.minimal_walk_action_client.send_goal_async(
            minimal_walk_goal_msg, 
            feedback_callback=self.feedback_callback)

        send_goal_future.add_done_callback(self.goal_response_callback_miniwalk)

    def goal_response_callback_miniwalk(self, future):    
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._goal_handle = goal_handle

        get_result_future = goal_handle.get_result_async() #requesting result
        get_result_future.add_done_callback(self.minimal_walk_goal_result_callback)

    def minimal_walk_goal_result_callback(self, future):
        result = future.result().result
        self.parent.print_result("minimal client", result)
        self.parent.insert_in_scroll(result)

    def cancel_miniwalk_goal(self):
        """
        https://blog.csdn.net/qq_27865227/article/details/121207085
        https://answers.ros.org/question/361666/ros2-action-goal-canceling-problem/
        https://github.com/ros2/examples/tree/rolling/rclpy/actions/minimal_action_server 
        """
        cancel_future  = self._goal_handle.cancel_goal_async() #requesting cancel
        print("tryna cancel")
        cancel_future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal successfully canceled')
        else:
            self.get_logger().warning('Goal failed to cancel')
  
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))
        
        self.parent.display_action_feedback("miniwalk_feedback", feedback, show_type = 1)

        
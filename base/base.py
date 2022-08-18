from rclpy.node import Node
from rclpy.action import ActionClient


from std_msgs.msg import Int32
from geometry_msgs.msg import Point

from action_tutorials_interfaces.action import Fibonacci
from rover_utils.action import MinimalWalk
# from rover_utils.msg import TestMsg


import time 

class baseNode(Node):

    def __init__(self, parent = None):
        super().__init__('base_node')
        
        self.parent = parent

        # self.publisher = self.create_publisher(
        #     TestMsg, 
        #     'topic', 
        #     10)
        
        # self.subscription = self.create_subscription(
        #     Int32,
        #     'topic_result',
        #     self.sub_callback,
        #     8)

        # self.state_subscription = self.create_subscription(
        #     Int32,
        #     'state_topic',
        #     self.sub_callback,
        #     8)

        # self._action_client = ActionClient(
        #     self, 
        #     Fibonacci, 
        #     'fibonacci')
        
        self.minimal_walk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'mini_walk_act')
    
    def send_minimal_walk_goal(self,x,y,z):
        # msg  = Point32()
        # msg.x, msg.y, msg.z = float(x), float(y), float(z)

        minimal_walk_goal_msg = MinimalWalk.Goal()
        minimal_walk_goal_msg.goal_var = int(x)

        # print("goal is prepped, now waiting for server")
        self.minimal_walk_action_client.wait_for_server()
        # print("wait over, now sending to action server")
        
        # while not self.minimal_walk_action_client.server_is_ready():
        #     time.sleep(1)
        #     print("retrying")

        # print("wait over, now sending to action server")
        

        send_goal_future = self.minimal_walk_action_client.send_goal_async(
            minimal_walk_goal_msg, 
            feedback_callback=self.feedback_callback)

        send_goal_future.add_done_callback(self.minimal_walk_goal_response_callback)


    def minimal_walk_goal_response_callback(self, future):    
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.minimal_walk_goal_result_callback)

    def minimal_walk_goal_result_callback(self, future):
        result = future.result().result
        self.parent.fetch_result("minimal client", result)
        self.parent.insert_in_scroll(result)

    # def do_pub(self, num):
    #     msg = TestMsg()
    #     point = Point()
    #     point.x = 2.0
    #     point.y = 2.0
    #     point.z = 2.0
    #     msg.point = point
    #     msg.my_float = 3.2
    #     self.publisher.publish(msg)
    #     #self.get_logger().info('Publishing: "%d"' % msg)
    #     print(msg)

    # def sub_callback(self, msg):
    #     self.get_logger().info('Got Result: "%f"' % msg.my_float)
        
    #     #rewrite these ...
    #     self.parent.fetch_result("pub: ", msg.my_float)
    #     self.parent.insert_in_scroll(msg.my_float)

    # # def state_callback(self, msg):
    # #     self.parent.fetch_state(msg.data)

    # def send_goal(self, order):
    #     goal_msg = Fibonacci.Goal()
    #     goal_msg.order = order

    #     self._action_client.wait_for_server()

    #     self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

    #     self._send_goal_future.add_done_callback(self.goal_response_callback)

    # def goal_response_callback(self, future):
    #     goal_handle = future.result()
    #     if not goal_handle.accepted:
    #         self.get_logger().info('Goal rejected :(')
    #         return

    #     self.get_logger().info('Goal accepted :)')

    #     self._get_result_future = goal_handle.get_result_async()
    #     self._get_result_future.add_done_callback(self.get_result_callback)

    # def get_result_callback(self, future):
    #     result = future.result().result
    #     self.get_logger().info('Result: {0}'.format(result.sequence))
        
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))
        self.parent.display_action_feedback("action_client", feedback.feedback)
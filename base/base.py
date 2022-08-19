from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action import ClientGoal



from geometry_msgs.msg import Point


from rover_utils.action import MinimalWalk
from rover_utils.msg import TankDriveMsg


import time 

class baseNode(Node):

    def __init__(self, parent = None):
        super().__init__('base_node')
        
        self.parent = parent

        self.teensy_publisher = self.create_publisher(
            TankDriveMsg, 
            'pwm_to_teensy', 
            10)
        
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

        self.goal_handle = ClientGoalHandle
    
    def send_minimal_walk_goal(self,tlat,tlon):
        coords  = Point()
        coords.x = tlat
        coords.y = tlon
        coords.z = 0.0

        minimal_walk_goal_msg = MinimalWalk.Goal()
        minimal_walk_goal_msg.coords = coords
        minimal_walk_goal_msg.use_guidance = False
        minimal_walk_goal_msg.signal_and_wait = False
        
        self.minimal_walk_action_client.wait_for_server()
        

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

    def do_pub(self):
        msg = TankDriveMsg()
        msg.lpwm = 127
        msg.rpwm = 127
        
        self.teensy_publisher.publish(msg)
        #self.get_logger().info('Publishing: "%d"' % msg)

        #print("Publishing: ")

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
        self.parent.display_action_feedback("action_client", feedback.d2t)
        self.parent.display_action_feedback("action_client", feedback.he)

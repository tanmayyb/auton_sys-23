from rclpy.node import Node
from rclpy.action import ActionClient


from std_msgs.msg import Int32
from action_tutorials_interfaces.action import Fibonacci


class baseNode(Node):

    def __init__(self, parent = None):
        super().__init__('base_node')
        
        self.parent = parent

        self.publisher = self.create_publisher(
            Int32, 
            'topic', 
            10)
        
        self.subscription = self.create_subscription(
            Int32,
            'topic_result',
            self.sub_callback,
            8)

        self.state_subscription = self.create_subscription(
            Int32,
            'state_topic',
            self.sub_callback,
            8)

        self._action_client = ActionClient(
            self, 
            Fibonacci, 
            'fibonacci')
        


    def do_pub(self, num):
        msg = Int32()
        msg.data = num
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)

    def sub_callback(self, msg):
        self.get_logger().info('Got Result: "%d"' % msg.data)
        
        #rewrite these ...
        self.parent.fetch_result(msg.data)
        self.parent.insert_in_scroll(msg.data)

    def state_callback(self, msg):
        self.parent.fetch_state(msg.data)

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))
        self.parent.display_action_feedback("action_client", feedback.partial_sequence)
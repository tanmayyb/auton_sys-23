from example_interfaces.srv import AddTwoInts
from std_msgs.msg import Int32

import rclpy
from rclpy.node import Node

class miniClient(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.subscription = self.create_subscription(
            Int32,
            'topic',
            self.subscription_callback,
            10)
        self.cli = self.create_client(
            AddTwoInts, 
            'add_two_ints')

        self.publisher = self.create_publisher(
            Int32,
            'topic_result',
            8)
        
        self.req = AddTwoInts.Request()
        self.num = 0
        
    def subscription_callback(self, msg):
        self.send_request(self.num, msg.data)
        self.num += msg.data

    def send_request(self, a, b):
        self.req.a = int(a)
        self.req.b = int(b)
        self.future = self.cli.call_async(self.req)
        self.future.add_done_callback(self.get_response)
        
    def get_response(self, future):
        result = future.result().sum
        self.get_logger().info('Got Result: "%d"' % result)
        
        msg = Int32()
        msg.data = int(result)
        self.publisher.publish(msg)

        
def main(args=None):
    rclpy.init(args=args)

    minimal_client = miniClient()

    while rclpy.ok():
        rclpy.spin(minimal_client)

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

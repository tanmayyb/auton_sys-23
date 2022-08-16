from rclpy.node import Node

from std_msgs.msg import Int32

class miniPub(Node):

    def __init__(self, parent = None):
        super().__init__('minimal_publisher')
        
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
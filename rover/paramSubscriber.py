import rclpy
from rclpy.node import Node

from custom_msg.msg import Robotparam #Need to put the msg file into a msg folder in a package

import json
from JsonFile import editJson

topicName = "robotJson"

class acquireParam(Node):

    def __init__(self):
        super().__init__('acquiring_parameters')

        #Get custom messages
        self.subscription = self.create_subscription(
            Robotparam,
            topicName,
            self.getParams,
            10)
        self.subscription  # prevent unused variable warning


    #Subscriber attempts to update rover JSON based on Publisher data
    def getParams(self, msg):
        params = dict() #Create an empty dictionary for settings
        try:
            params["BF-P"] = msg.bfp
            params["BF-R"] = msg.bfr
            params["D: PID"] = msg.d
            params["Drift Speed"] = msg.driftspeed
            params["I: PID"] = msg.i
            params["P: PID"] = msg.p
            params["Turn Speed"] = msg.turnspeed

            editJson(params)
        except:
            print("Error, invalid message.")
        self.get_logger().info('I heard: "%s"' % str(params))
    


#Run subscriber
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = acquireParam()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
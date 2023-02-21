from custom_msg.srv import Service

import rclpy
from rclpy.node import Node

from JsonFile import loadJson_file

topicName = 'get_params'

class sendingParam(Node):

    def __init__(self):
        super().__init__('sending_paramaters')
        self.srv = self.create_service(Service, topicName, self.sendResponse)

    #Service sends rover settings to client
    def sendResponse(self, request, response):
        jsonFile = loadJson_file()
        
        if (request.request == -1): #Check request id

            response.bfp = jsonFile["BF-P"]
            response.bfr = jsonFile["BF-R"]
            response.driftspeed = jsonFile["Drift Speed"]
            response.p = jsonFile["P: PID"]
            response.i = jsonFile["I: PID"]
            response.d = jsonFile["D: PID"]
            response.turnspeed = jsonFile["Turn Speed"]
        
            self.get_logger().info('Incoming request\nRequest Number: %d' % (request.request))
            return response
        else:
            self.get_logger().info('Error receiving request')


#Run service
def main(args=None):
    rclpy.init(args=args)

    minimal_service = sendingParam()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
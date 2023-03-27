import rclpy
from rclpy.node import Node

from rover_utils.msg import SendingParam
from rover_utils.srv import RequestParam

pubTopicName = "robotJson"
cliTopicName = "get_params"

class PublisherClient(Node):

    def __init__(self):
        super().__init__('publisher_client') #Calls the node class's constructor and gives it the node name 'publisher_client'

        #Init publisher
        self.publisher_ = self.create_publisher(SendingParam, pubTopicName, 10) #declares the node publishes message of type string with a topic name (must be same as Subscriber)

        #Init client
        self.cli = self.create_client(RequestParam, cliTopicName)                                 


    #Publisher sends rover parameters to the subscriber
    def sendParam(self, updatedParameters): 

        msg = SendingParam()
        #Check if updatedParameters is Python dictionary, adds values to msg
        if (type(updatedParameters) is dict):
            msg.bfp = updatedParameters["BF-P"]
            msg.bfer = updatedParameters["BF-ER"]
            msg.p = updatedParameters["P: PID"]
            msg.i = updatedParameters["I: PID"]
            msg.d = updatedParameters["D: PID"]
            msg.lpwm = updatedParameters["Left PWM"]
            msg.rpwm = updatedParameters["Right PWM"]
            msg.driftspeed = updatedParameters["Drift Speed"]
            msg.controloutput = updatedParameters["Control Output"]

            try:
                self.publisher_.publish(msg) #sends the JSON String to the robot
                self.get_logger().info('Sending: "%s"' % str(updatedParameters)) #prints what it sent on terminal
            except:
                print("Unable to send parameters") 
        else:
            print("Invalid data type, expected dictionary")
                                       

    #Client attempts to connect with service
    def sendRequest(self):

        time = 0 #Init Timer count
        while not self.cli.wait_for_service(timeout_sec=1.0): #Checks to see if there is a service node open, if not wait 1 sec
            time += 1 #Increase count by 1 (represent 1 sec)
            self.get_logger().info('service not available, waiting again...')
            if (time == 10): #If timer reaches 10 (sec) then stop trying to find service node
                self.get_logger().info('unable to find service. SERVICE TIMEOUT')
                raise Exception("Service Timeout") #send error
        self.req = RequestParam.Request()         
        
        self.req.request = -1           
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        
        response = self.future.result()

        params = dict() #Create an empty dictionary

        #Update rover settings to match with service response
        try:
            params["BF-P"] = response.bfp
            params["BF-ER"] = response.bfer
            params["P: PID"] = response.p
            params["I: PID"] = response.i
            params["D: PID"] = response.d
            params["Left PWM"] = response.lpwm
            params["Right PWM"] = response.rpwm
            params["Drift Speed"] = response.driftspeed
            params["Control Output"] = response.controloutput

            return params
        
        except:
            print("Error, invalid message.")
     
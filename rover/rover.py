"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rover_utils.action import MinimalWalk

from rover_utils.msg import SendingParam
from rover_utils.srv import RequestParam

from rover_utils.msg import TankDriveMsg
from geometry_msgs.msg import Point

from utils.JsonFile import *

from nvc.nvc import nv_calc  
from pid.error import heading_error
from pid.pid import pid_controller



import time


class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')

        print("rover_node initialised")

        self.parameters = loadJson_file()

        self.pid_controller = None

        """
        Operational Variable Initialisations
        ab2t:   Absolute Bearing to Target
        d2t:    Distance to Target
        arb:    Absolute Rover Bearing
        rc:     Rover Coordinates
        """
        self.ab2t = None
        self.d2t = None
        self.arb = None
        self.rc = None
        
        self.verbose = False
        
        #tunining variable initialisations
        self.neutral_pwms = (self.parameters["Left PWM"],self.parameters["Right PWM"])
        self.pid_const  = (self.parameters["P: PID"],  self.parameters["I: PID"], self.parameters["D: PID"]) # good for kerr 
        self.drift_and_control_output_pwms = (self.parameters["Drift Speed"], self.parameters["Control Output"]) # quad grass 

        self.pid_controller = pid_controller(
            self.pid_const, 
            self.drift_and_control_output_pwms)

        
        """LAUNCH ROS2 ACTION SERVER, PUB, SUB """

        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'MiniWalkTopic',
            execute_callback=self.miniwalk_exec_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.miniwalk_goal_callback,
            cancel_callback=self.miniwalk_cancel_callback,)

        self.teensy_pub = self.create_publisher(
            TankDriveMsg,
            'TeensySubscriberTopic',
            10)

        self.vectornav_sub = self.create_subscription(
            Point,
            'VectorNavPublisherTopic',
            self.update_sensor_data,
            10)

        self.param_sub = self.create_subscription(
            SendingParam,
            'robotJson',
            self.getParams,
            10)

        self.param_srv = self.create_service(
            RequestParam, 
            'get_params', 
            self.sendParams)

        #VectorNavSensorData


    def update_sensor_data(self, msg):
        lat = msg.x
        lon = msg.y
        arb = msg.z

        self.rc = (lat, lon)
        self.arb = arb

        if self.verbose == True:
            print(msg)

    def miniwalk_goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        # This server allows multiple goals in parallel
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def miniwalk_cancel_callback(self, goal_handle):
        self.get_logger().warn('Received cancel request!')
        self.set_rover_to_neutral()
        return CancelResponse.ACCEPT

    async def miniwalk_exec_callback(self, goal_handle):
        print("received goal request", goal_handle.request)
        
        coords = goal_handle.request.coords
        tc = (coords.x, coords.y)   #get coordinates from msg
        geofence = coords.z  #get geofence from msg
        
        #signal_and_wait = goal_handle.request.signal_and_wait
        #use_guidance = goal_handle.request.use_guidance

        print("received coords: ", coords.x, coords.y)
        
        self.get_logger().warn('Walking to Target...')

        feedback_msg = MinimalWalk.Feedback()

        loop = True
        while loop:

            """cancel codition to close callback w/o execution blocking"""
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return MinimalWalk.Result()

            """logic of walk"""
            ab2t, d2t = nv_calc(self.rc, tc)
            error = heading_error(self.arb, ab2t)
            control = self.pid_controller.do_pid(error)
            boost = self.pid_controller.do_boost(error)
            """send signal to teensy"""
            c2mm = self.pid_controller.do_c2mm(control, boost)
            self.send_to_teensy(c2mm)
            

            feedback_msg.d2t = d2t
            feedback_msg.he = error

            goal_handle.publish_feedback(feedback_msg)
            
            #time.sleep(.05)

            if d2t<geofence:
                loop = False

        goal_handle.succeed()
        self.set_rover_to_neutral()
        result = MinimalWalk.Result()
        result.result = True

        self.get_logger().info('Goal Executed!...')

        return result
    
    def set_rover_to_neutral(self):
        self.send_to_teensy(self.neutral_pwms)

    def send_to_teensy(self, c2mm):
        msg = TankDriveMsg()
        msg.lpwm = c2mm[0]
        msg.rpwm = c2mm[1]
        self.teensy_pub.publish(msg)
        """leds have to be accounted for"""
    
    def getParams(self, msg):
        params = dict() #Create an empty dictionary for settings
        try:
            params["BF-P"] = msg.bfp
            params["BF-ER"] = msg.bfer
            params["P: PID"] = msg.p
            params["I: PID"] = msg.i
            params["D: PID"] = msg.d
            params["Left PWM"] = msg.lpwm
            params["Right PWM"] = msg.rpwm
            params["Drift Speed"] = msg.driftspeed
            params["Control Output"] = msg.controloutput
            editJson(params)
        except:
            print("Error, invalid message.")
        self.get_logger().info('I heard: "%s"' % str(params))
    
    def sendParams(self, request, response):
        jsonFile = loadJson_file()
        
        if (request.request == -1): #Check request id

            response.bfp = jsonFile["BF-P"]
            response.bfer = jsonFile["BF-ER"]
            response.p = jsonFile["P: PID"]
            response.i = jsonFile["I: PID"]
            response.d = jsonFile["D: PID"]
            response.lpwm = jsonFile["Left PWM"]
            response.rpwm = jsonFile["Right PWM"]
            response.driftspeed = jsonFile["Drift Speed"]
            response.controloutput = jsonFile["Control Output"]

            self.set_params()
        
            self.get_logger().info('Incoming request\nRequest Number: %d' % (request.request))
            return response
        else:
            self.get_logger().info('Error receiving request')
    
    def set_params(self):
        self.neutral_pwms = (self.parameters["Left PWM"],self.parameters["Right PWM"])
        self.pid_const  = (self.parameters["P: PID"],  self.parameters["I: PID"], self.parameters["D: PID"])
        self.drift_and_control_output_pwms = (self.parameters["Drift Speed"], self.parameters["Control Output"])


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

"""Original Parameter values"""
#self.neutral_pwms = (127,127)
#self.pid_const  = (0.6,  0.0, 0.1) # good for kerr 
#self.drift_and_control_output_pwms = (20, 40) # quad grass 



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
    
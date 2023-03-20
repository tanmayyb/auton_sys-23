"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Main 'rover' node with action logics

    - Miniwalk action
    - Approach action
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from rover_utils.action import MinimalWalk
from rover_utils.msg import TankDriveMsg
from geometry_msgs.msg import Point

from utils.nvc import nav_vec_calc  
from utils.error import heading_error
from utils.pid import pid_controller

import time

class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')

        print("rover_node initialised")


        self.pid_controller = None

        """
        Navigational Variables
        ab2t:       Absolute Bearing to Target
        d2t:        Distance to Target
        arb:        Absolute Rover Bearing
        rcrds:      Rover Coordinates
        """
        self.ab2t = None
        self.d2t = None
        self.arb = 0.0
        self.rcrds = (0.0,0.0)
        
        self.verbose = False
        
        #tunning variable initialisations
        # <<<<< add load functionality here 

        # miniwalk tunings
        self.neutral_pwms = (127,127)
        self.pid_const  = (0.6,  0.0, 0.1) # good for kerr 
        self.drift_and_control_output_pwms = (20, 40) # quad grass 
        # approach tunings
        

        self.pid_controller = pid_controller(
            self.pid_const, 
            self.drift_and_control_output_pwms)

        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'miniwalk',
            execute_callback=self.miniwalk_exec_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.miniwalk_goal_callback,
            cancel_callback=self.miniwalk_cancel_callback,)

        self.teensy_pub = self.create_publisher(
            TankDriveMsg,
            'drive_msg',
            10)

        self.vectornav_sub = self.create_subscription(
            Point,
            'rover_pose_msg',
            self.update_sensor_data_callback,
            10)
        #VectorNavSensorData


    def update_sensor_data_callback(self, msg):
        lat = msg.x
        lon = msg.y
        arb = msg.z

        self.rcrds = (lat, lon)
        self.arb = arb

        if self.verbose == True:
            print(msg)

    def miniwalk_goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        # This server allows multiple goals in parallel
        self.get_logger().info('received new goal request')
        return GoalResponse.ACCEPT

    def miniwalk_cancel_callback(self, goal_handle):
        self.get_logger().warn('received current goal cancel request!')
        self.set_rover_to_neutral()
        return CancelResponse.ACCEPT

    async def miniwalk_exec_callback(self, goal_handle):
        print("received goal request", goal_handle.request)
        
        coords = goal_handle.request.coords
        tcrds = (coords.x, coords.y)   #get coordinates from msg
        geofence = coords.z  #get geofence from msg

        #signal_and_wait = goal_handle.request.signal_and_wait

        print("received coords: ", coords.x, coords.y)
        
        self.get_logger().warn('Walking to Target...')

        feedback_msg = MinimalWalk.Feedback()

        self.miniwalk_loop = True   
        while self.miniwalk_loop:

            """cancel codition to close callback w/o execution blocking"""
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return MinimalWalk.Result()

            """logic of mini walk"""
            ab2t, d2t = nav_vec_calc(self.rcrds, tcrds)
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
                self.miniwalk_loop = False

        #if cvs2 interrupts and no false alarm detected stop miniwalk and execute approach behaviour
        #if cvs2 false alarm, then continue on as you were

        goal_handle.succeed()
        self.set_rover_to_neutral()
        result = MinimalWalk.Result()
        result.result = True

        self.get_logger().info('Goal Finished Executing!...')

        return result
    
    def set_rover_to_neutral(self):
        self.send_to_teensy(self.neutral_pwms)

    def send_to_teensy(self, c2mm):
        msg = TankDriveMsg()
        msg.lpwm = c2mm[0]
        msg.rpwm = c2mm[1]
        self.teensy_pub.publish(msg)
        """leds have to be programmed"""

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
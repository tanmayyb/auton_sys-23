"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Main 'rover' node with low level action logics

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
from std_msgs.msg import Empty, Float64, Int64

from libs.controller import controller
from settings.pid import *
from settings.rover import *

from utils.navigation_vector import calculate_navigation_vector  
from utils.navigation_error import calculate_heading_error

import time

class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')

        print("rover_node initialised")


        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        miniWalk Navigation Variables
        ab2t:       Absolute Bearing to Target
        d2t:        Distance to Target
        arb:        Absolute Rover Bearing
        rcrds:      Rover Coordinates
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.ab2t = None
        self.d2t = None
        self.arb = 0.0
        self.rcrds = (0.0,0.0)
        
        self.verbose = False
        
        #tunning variable initialisations
        # <<<<< add load functionality here 

        """
        PID for Miniwalk and Approach
        """
        self.neutral_pwms = (127,127)

        self.miniwalk_pid = controller(
            MINIWALK_PID_CONTROL_CONSTS ,
            MINIWALK_AUX_CONTROL_CONSTS,
            sample_time=0.5)
        
        self.approach_pid = controller(
            APPROACH_PID_CONTROL_CONSTS,
            APPROACH_AUX_CONTROL_CONSTS,
            sample_time=0.1)
        
    
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        ROS 2 Interfaces
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'miniwalk',
            execute_callback=self.miniwalk_exec_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.miniwalk_goal_callback,
            cancel_callback=self.miniwalk_cancel_callback,)

        """Teensy Node Interfaces"""
        self.teensy_drive_pub = self.create_publisher(
            TankDriveMsg,
            'drive_msg',
            10)
        self.teensy_led_pub = self.create_publisher(
            Int64,
            'led_msg',
            10)
        """Sensor Module Interface"""
        self.vectornav_sub = self.create_subscription(
            Point,
            'rover_pose_msg',
            self.update_sensor_data_callback,
            10)
        """CVS2 Interface"""
        self.cvs2_error_sub = self.create_subscription(
            Float64,
            'cvs2_error_msg',
            self.approach_drive_callback,
            10)
        
        self.successful_searchwalk_sub = self.create_subscription(
            Empty,
            'successful_searchwalk',
            self.successful_searchwalk_callback, 
            10)
        
        self.node_sub = self.create_subscription(
            Int64,
            'node_test',
            self.node_callback,
            10)

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        State Variables
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.state = RVR_DICT['idle_standby']
        self.state_publisher = self.create_publisher(
            Int64, 
            'rover_state', 
            10)
        self.state_pub_timer = self.create_timer(
            ROVER_STATE_PUB_TIMER_PERIOD, 
            self.state_pub_timer_callback)
        self.set_rover_state_sub = self.create_subscription(
            Int64,
            'set_rover_state',
            self.set_rover_state_callback,
            10)
        
        """
        DEBUGGING/DEVELOPMENT INTERFACES
        """
        """
        self.launch_subroutine_sub = self.create_subscription(
            Empty,
            'launch_green_flash',
            self.green_flash_callback,
            10)
        """

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    vectorNav subscriber
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def update_sensor_data_callback(self, msg):
        lat = msg.x
        lon = msg.y
        arb = msg.z

        self.rcrds = (lat, lon)
        self.arb = arb

        if self.verbose == True:
            print(msg)

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    miniWalk action
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
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

        self.set_rover_state(RVR_DICT['miniwalk'])
        
        coords = goal_handle.request.coords
        use_signal_and_wait = goal_handle.request.signal_and_wait
        tcrds = (coords.x, coords.y)        #get coordinates from msg
        geofence = coords.z                 #get geofence from msg

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
                self.send_to_teensy_drive(self.neutral_pwms)               #set to neutral
                return MinimalWalk.Result()

            """logic of mini walk"""
            ab2t, d2t = calculate_navigation_vector(self.rcrds, tcrds)
            error = calculate_heading_error(self.arb, ab2t)
            c2mm = self.miniwalk_pid.control(error)
        
            """send signal to teensy"""
            self.send_to_teensy_drive(c2mm)
            
            """create feedback"""
            feedback_msg.d2t = d2t
            feedback_msg.he = error
            goal_handle.publish_feedback(feedback_msg)
            
            if d2t<geofence:
                self.miniwalk_loop = False

        goal_handle.succeed()
        self.set_rover_to_neutral()
        result = MinimalWalk.Result()
        result.result = True

        self.get_logger().info('Goal Finished Executing!...')
        #dont flash green at every waypoint
        if use_signal_and_wait:
            self.state = RVR_DICT['goal_reached']
            self.green_flash_subroutine()
        return result
    
    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    other actions
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def approach_drive_callback(self, msg):
        cvs2_error = msg.data
        c2mm = self.approach_pid.control(cvs2_error)
        self.send_to_teensy_drive(c2mm)
        self.state = RVR_DICT['approaching_aruco']
        self.set_led_state(LED_DICT['AUTONOMOUS MODE'])

    def successful_searchwalk_callback(self, msg):
        self.send_to_teensy_drive(self.neutral_pwms)
        self.state = RVR_DICT['goal_reached']
        self.green_flash_subroutine()
        self.state = RVR_DICT['idle_standby']
    
    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    teensy
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def set_rover_to_neutral(self):
        self.send_to_teensy_drive(self.neutral_pwms)

    def send_to_teensy_drive(self, c2mm):
        msg = TankDriveMsg()
        msg.lpwm = c2mm[0]
        msg.rpwm = c2mm[1]
        self.teensy_drive_pub.publish(msg)

    def send_to_teensy_led(self, state):
        msg = Int64()
        msg.data = int(state)
        self.teensy_led_pub.publish(msg)

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    state callback
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    def state_pub_timer_callback(self):
        msg = Int64()
        msg.data = self.state
        self.state_publisher.publish(msg)

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    subroutines
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    # def green_flash_callback(self, msg):
    #     start_time = time.time()
    #     self.green_flash_subroutine(start_time)
        
    def green_flash_subroutine(self):
        #print("Green Flash Subroutine Triggered, looping..", time.time())
        start_time = time.time()
        while(time.time()-start_time<FLASH_LED_GREEN_TIMEOUT):
            self.set_led_state(GREEN_LED_CODE)
            time.sleep(FLASH_LED_GREEN_ON_DURATION)
            self.set_led_state(OFF_LED_CODE)
            time.sleep(FLASH_LED_GREEN_OFF_DURATION)
        if self.verbose: print("Green Flash Subroutine completed") 

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    states and LEDs
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def set_rover_state_callback(self, msg):
        state = msg.data
        self.state = state
        print("setting rover state as:", RVR_INFO[state])
        self.set_led_state(state)

    def set_rover_state(self, state):
        self.state = state
        print("setting rover state as:", RVR_INFO[state])
        self.set_led_state(state)

    def set_led_state(self, led_code):
        msg = Int64()
        msg.data = led_code
        self.teensy_led_pub.publish(msg)
    
    def node_callback(self, msg):
        None

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
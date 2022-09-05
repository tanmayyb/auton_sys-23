"""
https://levelup.gitconnected.com/ros-spinning-threading-queuing-aac9c0a793f

"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor


from action_tutorials_interfaces.action import Fibonacci
from rover_utils.action import MinimalWalk
from rover_utils.msg import TankDriveMsg

from nvc.nvc import nv_calc  
from pid.error import heading_error
from pid.pid import pid_controller


import time


class Rover(Node):
    def __init__(self):
        super().__init__('rover_node')

        print("rover_node initialised")


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
        

        
        #tunining variable initialisations
        self.neutral_pwms = (127,127)
        self.pid_const  = (0.6,  0.0, 0.1) # good for kerr 
        self.drift_and_control_output_pwms = (20, 40) # quad grass 

        self.pid_controller = pid_controller(
            self.pid_const, 
            self.drift_and_control_output_pwms)

        
        """LAUNCH ROS2 ACTION SERVER, PUB, SUB """

        self.min_walk_act_server = ActionServer(
            self,
            MinimalWalk,
            'point_to_point_minimal_walk',
            execute_callback=self.miniwalk_exec_callback,
            callback_group=ReentrantCallbackGroup(),
            goal_callback=self.miniwalk_goal_callback,
            cancel_callback=self.miniwalk_cancel_callback,)

        self.teensy_pub = self.create_publisher(
            TankDriveMsg,
            'pwm_to_teensy',
            10)

        # self.vectornav_sub = self.create_subscription(
        #     SensorMsg,
        #     'VectorNavSensorData',
        #     self.update_sensor_data)


    def update_sensor_data(self, msg):
        pass

    def miniwalk_goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        # This server allows multiple goals in parallel
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def miniwalk_cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    async def miniwalk_exec_callback(self, goal_handle):

        print("received goal request", goal_handle.request)
        coords = goal_handle.request.coords
        print("received coords: ", coords.x, coords.y)

        self.get_logger().info('Walking to Target...')

        feedback_msg = MinimalWalk.Feedback()


        time_ = time.time()

        loop = True
        while loop:

            """cancel codition to close callback w/o execution blocking"""
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return MinimalWalk.Result()

            self.rc = (43.65897373429778, -79.37932931217927)

            self.arb = 30.000

            """logic of walk"""
            tc = (coords.x, coords.y)
            ab2t, d2t = nv_calc(self.rc, tc)
            error = heading_error(self.arb, ab2t)
            control = self.pid_controller.do_pid(error)
            
            """send signal to teensy"""
            c2mm = self.pid_controller.do_c2mm(control)
            self.send_to_teensy(c2mm)
            

            feedback_msg.d2t = d2t
            feedback_msg.he = error

            goal_handle.publish_feedback(feedback_msg)
            time.sleep(.05)

            if time.time() - time_ > 5.0:
                loop = False

        goal_handle.succeed()
        
        self.send_to_teensy(self.neutral_pwms)
        result = MinimalWalk.Result()
        result.result = True

        self.get_logger().info('Goal Executed!...')

        return result

    def send_to_teensy(self, c2mm):
        msg = TankDriveMsg()
        msg.lpwm = c2mm[0]
        msg.rpwm = c2mm[1]
        self.teensy_pub.publish(msg)
        """leds have to be accounted for"""



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
    
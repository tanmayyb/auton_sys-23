from pickle import FALSE, TRUE
from rclpy.node import Node
from rclpy.action import ActionClient

from std_msgs.msg import Bool, Empty, Int64
from geometry_msgs.msg import Point

from rover_utils.action import MinimalWalk
from rover_utils.msg import TankDriveMsg, SearchWalk

import time 

class baseNode(Node):

    def __init__(self, parent = None):
        super().__init__('base_node')
        
        self.parent = parent

        """
        ROS 2 Interfaces
        """
        self.minimal_walk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'miniwalk')

        self.teleop_pub = self.create_publisher(
            TankDriveMsg,
            'drive_msg',
            10)

        self.sensor_sub = self.create_subscription(
            Point,
            'rover_pose_msg',
            self.gui_update_rover_lla,
            10)

        self.do_searchwalk_pub = self.create_publisher(
            SearchWalk,
            'start_searchwalk',
            10)
        
        self.cancel_searchwalk_pub = self.create_publisher(
            Bool,
            'stop_searchwalk',
            10)
        
        self.set_cvs2_state_pub = self.create_publisher(
            Bool,
            'set_cvs2_state',
            10)
        
        self.e_stop_pub = self.create_publisher(
            Empty,
            'e_stop',
            10)

        self.enable_drive_pub = self.create_publisher(
            Empty,
            'enable_drive',
            10)
        
        self.set_rover_state_pub = self.create_publisher(
            Int64,
            'set_rover_state',
            10)
        
        self.set_rover_state_sub = self.create_subscription(
            Int64,
            'rover_state',
            self.set_rover_state_callback,
            10)
        
        self.set_cvs2_state_sub = self.create_subscription(
            Int64,
            'cvs2_state',
            self.set_cvs2_state_callback,
            10)

        self.node_test_timer = self.create_timer(
            3.0,
            self.node_test_callback)

        self.node_test_publisher = self.create_publisher(
            Int64,
            'node_test',
            10)

    def send_goal_miniwalk(self,tlat,tlon, gf_rad):
        
        """CREATE GOAL MSG"""
        coords  = Point()
        coords.x = tlat
        coords.y = tlon
        coords.z = gf_rad

        """SEND GOAL MSG"""
        minimal_walk_goal_msg = MinimalWalk.Goal()
        minimal_walk_goal_msg.coords = coords
        minimal_walk_goal_msg.use_guidance = False
        minimal_walk_goal_msg.signal_and_wait = True
        
        self.minimal_walk_action_client.wait_for_server()  

        send_goal_future = self.minimal_walk_action_client.send_goal_async(
            minimal_walk_goal_msg, 
            feedback_callback=self.feedback_callback)

        send_goal_future.add_done_callback(self.goal_response_callback_miniwalk)

    def goal_response_callback_miniwalk(self, future):    
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._goal_handle = goal_handle

        get_result_future = goal_handle.get_result_async() #requesting result
        get_result_future.add_done_callback(self.minimal_walk_goal_result_callback)

    def minimal_walk_goal_result_callback(self, future):
        result = future.result().result
        self.parent.scroll.print_result("minimal client", result)
        self.parent.scroll.insert_in_scroll(result)

    def cancel_miniwalk_goal(self):
        """
        https://blog.csdn.net/qq_27865227/article/details/121207085
        https://answers.ros.org/question/361666/ros2-action-goal-canceling-problem/
        https://github.com/ros2/examples/tree/rolling/rclpy/actions/minimal_action_server 
        """
        cancel_future  = self._goal_handle.cancel_goal_async() #requesting cancel
        print("tryna cancel")
        cancel_future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal successfully canceled')
        else:
            self.get_logger().warning('Goal failed to cancel')
  
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))
        
        self.parent.scroll.display_action_feedback("miniwalk_feedback", feedback, show_type = 1)

    def do_teleop(self, lpwm, rpwm):
        msg = TankDriveMsg()
        msg.lpwm=lpwm
        msg.rpwm=rpwm
        self.teleop_pub.publish(msg)

    def gui_update_rover_lla(self, msg):
        x = msg.x
        y = msg.y
        z = msg.z
        self.parent.actionConsole.update_rover_lla(x,y,z)
        self.parent.map.update_rover_marker(x,y)
        # #print(x,y,z)
        pass

    def start_searchwalk(self, msg):
        lat, lon, srad, s_pttrn, e_cv, e_oa  = msg

        searchwalk_msg = SearchWalk()
        
        coords = Point()
        coords.x = lat
        coords.y = lon
        coords.z = 0.0
        
        searchwalk_msg.coords = coords
        searchwalk_msg.search_radius = srad
        searchwalk_msg.search_pattern = s_pttrn
        searchwalk_msg.enable_cv = e_cv
        searchwalk_msg.enable_oa = False
        searchwalk_msg.loop_searchwalk = False

        print(searchwalk_msg)
        self.do_searchwalk_pub.publish(searchwalk_msg)

    def cancel_searchwalk(self):
        #cancel Searchwalk on Action Manager
        msg = Bool()
        msg.data = True
        self.cancel_searchwalk_pub.publish(msg)

        #shut down CVS2
        msg = Bool()
        msg.data = False
        self.set_cvs2_state_pub.publish(msg)
        

    def trigger_e_stop(self):
        msg = Empty()
        self.e_stop_pub.publish(msg)
        self.get_logger().error("drive E_STOP triggered!")

    def enable_drive(self):
        msg = Empty()
        self.enable_drive_pub.publish(msg)
        self.get_logger().warn("drive ENABLE triggered!")

    def set_rover_state(self, state):
        msg = Int64()
        msg.data = state
        self.set_rover_state_pub.publish(msg)
    
    def set_rover_state_callback(self, msg):
       self.state = msg.data
       self.parent.topBar.set_rover_state(self.state)
    
    def node_test_callback(self):
       rover_node_list = []
       self.rover_node_alive = self.get_subscriptions_info_by_topic('node_test')
       for nodes in self.rover_node_alive:
           rover_node_list.append(str(nodes.node_name))
       self.parent.topBar.set_led_status(rover_node_list)
    
    def set_cvs2_state_callback(self, msg):
        self.cvs2_state = msg.data
        self.parent.topBar.set_cvs2_state(self.cvs2_state)


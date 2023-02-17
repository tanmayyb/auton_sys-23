"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Search and Approach Action Manager (S.A.A.M.)

    - Search Action (Multiwalk)
    - Instructs 'rover' to perform Approach Action
    - Communicates with 'cvs2' and 'rover' nodes
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import MultiThreadedExecutor

from std_srvs.srv import Trigger

from rover_utils.action import MinimalWalk
from rover_utils.msg import Searchwalk

import math

class SearchApproachActionManager(Node):

    def __init__(self):
        super().__init__('action_manager')

        """
        Searchwalk Variables
        """
        self.sw_goal_list = []
        self.sw_goal_list_last_index = -1
        self.sw_gid = 0
        

        self.running_search = False

        self.miniwalk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'miniwalk')

        self.load_goals_and_execute_searchwalk_subscription = self.create_subscription(
            Searchwalk,
            'searchwalk',
            self.load_goals_and_execute_searchwalk,
            10)

        self.searchwalk_interruption_service = self.create_service(
            Trigger, 
            'halt_searchwalk', 
            self.searchwalk_interruption_callbak)


        self.get_logger().info("!action manager created!") 


    def load_goals_and_execute_searchwalk(self, msg):
        lat,lon = msg.data.x, msg.data.y #this should be points = msg.data??
        radius = msg.radius
        pattern = msg.pattern
        self.loop_searchwalk = msg.loop_searchwalk

        """
        create searchwalk goals
        """
        try: #this can be tested using a pub to the gui to plot the pattern
            self.sw_goal_list = self.generateSearchPattern((lat, lon), radius, pattern)
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk failed to create goal queue')
        
        self.running_search = True
        self.sw_goal_list_last_index = self.sw_goal_list_last_index + len(self.sw_goal_list)
        self.searchwalk_goal_executor()

    def searchwalk_goal_executor(self): #searchwalk behaviour management function
        while not self.miniwalk_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('SearchWalk: waiting for MiniWalk action server to become available...')
        
        if(self.running_search):
            if self.sw_gid<=self.sw_goal_list_last_index:
                goal = self.sw_goal_list[self.sw_gid]
                print("sw_gid", self.sw_gid, goal)
                self.get_logger().warning('sending miniwalk goal:') #define goal here
                self.send_goal(goal)
            
            else: #patch this part of code
                self.get_logger().warning('all goals successfully completed: %d' % (goal.order,))
                self.reset_goal_queue()

    def searchwalk_interruption_callbak(self):
        #code for interruption of searchwalk by cvs2
        
        pass

    def generateSearchPattern(self, center_coord, radius, step_angle):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Search pattern algorithm
        Main Auth:  Niko Trivanovic
        Created:    15 January, 2023
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """        
        """
        algorithmic constants, determined by experimentation
        """
        slope = 0.2
        scale = 0.00001
        
        step_depth = slope*radius + 1.0

        multiwalk_points = [center_coord]
        num_search_points = (radius//step_depth) * (360//step_angle)
        theta = 0
        step = 1

        for n in range(num_search_points):
            if theta >= 360:
                theta = 0
                step += 1
        
            lat = center_coord[0] + (((step * step_depth) * math.cos(math.radians(theta)))*scale) 
            lon = center_coord[1] + (((step * step_depth) * math.sin(math.radians(theta)))*scale)
            multiwalk_points.append((lat,lon))
            theta += step_angle

        return multiwalk_points


def main(args=None):
    rclpy.init(args=args)

    saam = SearchApproachActionManager()

    executor = MultiThreadedExecutor()

    rclpy.spin(saam, executor=executor)

    saam.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
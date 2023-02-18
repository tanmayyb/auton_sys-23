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
from rover_utils.msg import SearchWalk

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

        self.do_searchwalk = self.create_subscription(
            SearchWalk,
            'searchwalk',
            self.do_searchwalk_callback,
            10)

        self.searchwalk_interruption_service = self.create_service(
            Trigger, 
            'halt_searchwalk', 
            self.searchwalk_interruption_callbak)


        print("------------ACTION MANAGER CREATED------------") 

    def do_searchwalk_callback(self, msg):
        self.get_logger().warn("searchwalk goal received...\n")
        self.load_goals_and_execute_searchwalk(msg)

    def load_goals_and_execute_searchwalk(self, msg):
        try:
            lat = msg.coords.x #this should be points = msg.data??
            lon = msg.coords.y
            search_radius = msg.search_radius
            search_pattern = msg.search_pattern
            self.loop_searchwalk = msg.loop_searchwalk
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk failed to read msg')
        """
        create searchwalk goals
        """
        try: #this can be tested using a pub to the gui to plot the pattern
            searchwalk_goal = ((lat, lon), search_radius, search_pattern)
            self.sw_goal_list = self.create_searchwalk_goals(searchwalk_goal)
            self.running_search = True
            self.sw_goal_list_last_index = self.sw_goal_list_last_index + len(self.sw_goal_list)
            #self.searchwalk_goal_executor()
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk failed to create goal queue')
            
    # def searchwalk_goal_executor(self): #searchwalk behaviour management function
    #     while not self.miniwalk_action_client.wait_for_server(timeout_sec=1.0):
    #         self.get_logger().info('SearchWalk: waiting for MiniWalk action server to become available...')
        
    #     if(self.running_search):
    #         if self.sw_gid<=self.sw_goal_list_last_index:
    #             goal = self.sw_goal_list[self.sw_gid]
    #             print("sw_gid", self.sw_gid, goal)
    #             self.get_logger().warning('sending miniwalk goal:') #define goal here
    #             self.send_goal(goal)
            
    #         else: #patch this part of code
    #             self.get_logger().warning('all goals successfully completed: %d' % (goal.order,))
    #             self.reset_goal_queue()

    def searchwalk_interruption_callbak(self):
        #code for interruption of searchwalk by cvs2
        pass

    def create_searchwalk_goals(self, searchwalk_goal):
        self.get_logger().info("searchwalk goal list CREATED:\n")
        searchwalk_points = self.generateSearchPattern(searchwalk_goal)
        for point in searchwalk_points:
            """create miniwalk goal and add to goals list"""
            goal = MinimalWalk()
            goal.coords.x = point[0]
            goal.coords.y = point[1]
            goal.use_guidance = False
            goal.signal_and_wait = False
            self.sw_goal_list.append(goal)
            print("lat: ", point[0], "\tlon: ", point[1])

    def generateSearchPattern(self, searchwalk_goal):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Search pattern algorithm
        Main Auth:  Niko Trivanovic
        Created:    15 January, 2023
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """        
        """
        algorithm default constants, determined by experimentation
        """
        center_coord, radius, pattern = searchwalk_goal
        print(center_coord, radius, pattern)
        #SearchWalk pattern constants
        slope = 0.2
        scale = 0.00001
        theta = 0
        step_jump = slope*radius + 1.0 #step jump scaling equation
        step = 1
        step_angle = 120.0 #default
        #find step angle
        if(pattern==0): step_angle = 120.0
        elif(pattern==1): step_angle = 90.0
        elif(pattern==2): step_angle = 72.0
        searchwalk_points = [center_coord]
        num_search_points = int((radius//step_jump) * (360.0//step_angle))
        try:
            for n in range(num_search_points):
                if theta >= 360.0:
                    theta = 0
                    step += 1
                lat = center_coord[0] + (((step * step_jump) * math.cos(math.radians(theta)))*scale) 
                lon = center_coord[1] + (((step * step_jump) * math.sin(math.radians(theta)))*scale)
                searchwalk_points.append((lat,lon))
                theta += step_angle
                """
                Tool to plot SEARCHPOINTS: 
                https://maps.co/gis/
                """
                #print(lat,",",lon)
        except:
            self.get_logger().error('generateSearchPattern: error creating searchwalk_points')
        return searchwalk_points

def main(args=None):
    rclpy.init(args=args)

    saam = SearchApproachActionManager()

    executor = MultiThreadedExecutor()

    rclpy.spin(saam, executor=executor)

    saam.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
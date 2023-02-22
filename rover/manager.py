"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

Search and Approach Action Manager (S.A.A.M.)

    - Manages the 'SearchWalk' action (a flavor of Multiwalk/MultiFibonacci)
    - Instructs 'rover' to perform Approach Action
    - Communicates with 'cvs2' and 'rover' nodes
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import MultiThreadedExecutor

from std_srvs.srv import Trigger
from geometry_msgs.msg import Point
from std_msgs.msg import Bool


from rover_utils.action import MinimalWalk
from rover_utils.msg import SearchWalk

from utils.spa import generateSearchPattern

class SearchApproachActionManager(Node):

    def __init__(self):
        super().__init__('action_manager')

        """
        Searchwalk Variables
        """
        self.goal_list = []
        self.goal_list_last_index = -1
        self.gid = 0
        

        self.running_search = False

        """
        ROS2 Interfaces
        """
        self.do_searchwalk_subscription = self.create_subscription(
            SearchWalk,
            'start_searchwalk',
            self.do_searchwalk_callback,
            10)

        self.interrupt_searchwalk_service = self.create_service(
            Trigger, 
            'halt_searchwalk', 
            self.searchwalk_interruption_callback)

        self.resume_searchwalk_subscription = self.create_subscription(
            SearchWalk,
            'resume_searchwalk',
            self.resume_searchwalk_callback,
            10)
        self.stop_searchwalk_subscription = self.create_subscription(
            Bool,
            'stop_searchwalk',
            self.stop_searchwalk_callback,
            10)

        self.miniwalk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'miniwalk')

        print("------------ACTION MANAGER CREATED------------") 

    def do_searchwalk_callback(self, msg):
        self.get_logger().warn("searchwalk goal received...\n")
        print(msg)
        self.load_goals_and_execute_searchwalk(msg)

    def load_goals_and_execute_searchwalk(self, msg):
        verbose = True
        try:
            lat = msg.coords.x
            lon = msg.coords.y
            search_radius = msg.search_radius
            search_pattern = msg.search_pattern
            self.loop_searchwalk = msg.loop_searchwalk
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to read msg')
        """
        create searchwalk goals
        """
        try: #this can be tested using a pub to the gui to plot the pattern
            searchwalk_goal = ((lat, lon), search_radius, search_pattern)
            self.goal_list = self.create_searchwalk_goals(searchwalk_goal, verbose=verbose)
            self.goal_list_last_index = len(self.goal_list) - 1
            self.running_search = True
            if(verbose): print("num of goals in list: ", self.goal_list_last_index)
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to create goal queue!')
            self.running_search = False
            self.goal_list_last_index = -1
            self.goal_list = []
            return
        try:
            self.get_logger().warn('load_goals_and_execute_searchwalk: executing searchwalk...')
            self.searchwalk_goal_executor()
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to execute searchwalk!')
            
    def searchwalk_goal_executor(self): #searchwalk behaviour management function
        while not self.miniwalk_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('SearchWalk: waiting for MiniWalk action server to become available...')
        
        if(self.running_search):
            if self.gid<=self.goal_list_last_index:
                goal = self.goal_list[self.gid]
                print("sw_gid", self.gid, goal)
                self.get_logger().warning('sending miniwalk goal:') #define goal here
                self.send_miniwalk_goal(goal)
            
            else: #patch this part of code
                self.get_logger().warning('searchwalk_goal_executor: all goals successfully completed...')
                self.running_search = False

    def send_miniwalk_goal(self, goal):
        send_goal_future = self.miniwalk_action_client.send_goal_async(
            goal, 
            feedback_callback=self.miniwalk_feedback_callback)
        send_goal_future.add_done_callback(self.miniwalk_goal_response_callback)

    def miniwalk_goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Miniwalk Goal rejected :(')
            return
        
        self.get_logger().info('Miniwalk Goal accepted :)')
        self.goal_handle = goal_handle

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.miniwalk_get_result_callback)

    def miniwalk_get_result_callback(self, future):
        result = future.result().result
        #print(result, result.result)
        
        if result.result ==  True:
        #only continue if last goal result was successful
            self.gid = self.gid + 1
            if self.running_search:
                self.searchwalk_goal_executor()

        if result.result == False:
            self.running_search = False
            self.get_logger().warning("sw: miniwalk goal result=false")
        #if result==False, action could have been interrupted by cvs2
        #if result==False, action could have been interrupted by user
        #if result==False, action could have been interrupted by error

    def miniwalk_feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        #do something with the feedback like publish to gui

    def cancel_miniwalk_goal(self):
        self.get_logger().error('sending cancel request for current miniwalk goal...')
        print("goal_handle: ", self.goal_handle)
        
        if self.goal_handle is not None:
            cancel_future  = self.goal_handle.cancel_goal_async() #requesting cancel
            cancel_future.add_done_callback(self.miniwalk_cancel_done)
            self.get_logger().info('cancel request for goal sent...')
        #generalize for edge cases

    def miniwalk_cancel_done(self, future):
        cancel_response = future.result()

    def searchwalk_interruption_callback(self, request, response):
        if self.running_search:
            self.get_logger().warn('interrupting searchwalk...')
            self.cancel_miniwalk_goal()
            response.success = True    # write condition to ensure cancellation
        else:
            self.get_logger().error('no searchwalk goals to interrupt...')
            response.success = False
        return response

    def resume_searchwalk_callback(self, msg):
        self.get_logger().warn('resuming searchwalk from last goal...')
        self.searchwalk_goal_executor()

    def stop_searchwalk_callback(self, msg):
        self.cancel_miniwalk_goal()
        self.running_search = False

    def create_searchwalk_goals(self, searchwalk_goal, verbose=False):
        self.get_logger().info("creating sw goal list...")
        try:
            searchwalk_points = generateSearchPattern(searchwalk_goal)
        except:
            self.get_logger().error("create_searchwalk_goals: error generating search_pttrn")
        goal_list = []
        for point in searchwalk_points:
            """create miniwalk goal and add to goals list"""
            goal = MinimalWalk.Goal()
            coords  = Point()
            coords.x = point[0]
            coords.y = point[1]
            coords.z = 0.0 
            goal.coords = coords
            goal.use_guidance = False
            goal.signal_and_wait = False
            goal_list.append(goal)
            if(verbose): print("lat: ", point[0], "\t\tlon: ", point[1])
        
        return goal_list
         


def main(args=None):
    rclpy.init(args=args)

    saam = SearchApproachActionManager()

    executor = MultiThreadedExecutor()

    rclpy.spin(saam, executor=executor)

    saam.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
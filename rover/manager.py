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
        super().__init__('action_manager_node')

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

        self.miniwalk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'miniwalk')

        self.set_cvs2_state_publisher = self.create_publisher(
            Bool,
            'set_cvs2_state',
            10)


        """
        Searchwalk Interfaces
        """
        self.do_searchwalk_subscription = self.create_subscription(
            SearchWalk,
            'start_searchwalk',
            self.do_searchwalk_callback,
            10)

        self.stop_searchwalk_subscription = self.create_subscription(
            Bool,
            'stop_searchwalk',
            self.stop_searchwalk_callback,
            10)

        self.pause_searchwalk_service = self.create_service(
            Trigger, 
            'pause_searchwalk', 
            self.pause_searchwalk_callback)

        self.resume_searchwalk_service = self.create_service(
            Trigger,
            'resume_searchwalk',
            self.resume_searchwalk_callback)

        print("------------ACTION MANAGER CREATED------------") 

    def do_searchwalk_callback(self, msg):
        self.get_logger().warn("searchwalk goal received...\n")
        print(msg)  #print the searchwalk request
        self.load_goals_and_execute_searchwalk(msg)

    def load_goals_and_execute_searchwalk(self, msg):
        verbose = True
        try:
            lat = msg.coords.x
            lon = msg.coords.y
            search_radius = msg.search_radius
            search_pattern = msg.search_pattern
            self.enable_cv = msg.enable_cv
            self.loop_searchwalk = msg.loop_searchwalk
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to read msg')
        
        """
        Create Searchwalk Goals
        """
        try: #this can be tested using a pub to the gui to plot the pattern
            searchwalk_goal = ((lat, lon), search_radius, search_pattern)
            self.goal_list = self.create_searchwalk_goals(searchwalk_goal, verbose=False)
            self.goal_list_last_index = len(self.goal_list) - 1
            self.running_search = True
            if(verbose): print("num of goals in list: ", self.goal_list_last_index)
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to create goal queue!')
            self.running_search = False
            self.goal_list_last_index = -1
            self.goal_list = []
            return
        """
        Start Searchwalk
        """
        try:
            self.get_logger().warn('load_goals_and_execute_searchwalk: executing searchwalk...')
            self.searchwalk_goal_executor()
        except:
            self.get_logger().error('load_goals_and_execute_searchwalk: failed to execute searchwalk!')
            
    def searchwalk_goal_executor(self):
        """
        SearchWalk Goal Executor/Behaviour Management Function
        """
        while not self.miniwalk_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('SearchWalk: waiting for MiniWalk action server to become available...')
        
        if(self.running_search):
            if self.gid<=self.goal_list_last_index:
                
                """
                CVS2 Control Condition
                """
                if self.gid == 1:   #run cvs2 after reaching search area
                    self.get_logger().warning('ActionManager: turning CVS2 ON...')
                    self.run_cvs2(True)

                """
                Send New Goals from goal queue
                """"
                goal = self.goal_list[self.gid]
                print("sw: sending mW goal.... \nsw_gid: ", self.gid, "\nsw_goal: ", goal)
                #self.get_logger().warning('sw: sending miniwalk goal...') #define goal here
                self.send_miniwalk_goal(goal)
            
            else: 
                #patch this part of code
                #loop control goes here
                self.get_logger().warning('searchwalk_goal_executor: all goals successfully completed...')
                self.running_search = False
                self.goal_handle = None

    def send_miniwalk_goal(self, goal):
        send_goal_future = self.miniwalk_action_client.send_goal_async(
            goal, 
            feedback_callback=self.miniwalk_feedback_callback)
        send_goal_future.add_done_callback(self.miniwalk_goal_response_callback)

    def miniwalk_goal_response_callback(self, future):
        verbose = True
        goal_handle = future.result()
        if not goal_handle.accepted:
            if verbose: self.get_logger().error('<send_miniwalk_goal>: Miniwalk Goal rejected :(')
            return
        
        if verbose: self.get_logger().info('Miniwalk Goal accepted :)')
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
        self.get_logger().error('cancel requested for current miniwalk goal...')
        print("goal_handle: ", self.goal_handle)
        
        if self.goal_handle is not None:
            cancel_future  = self.goal_handle.cancel_goal_async() #requesting cancel
            cancel_future.add_done_callback(self.miniwalk_cancel_done)
            self.get_logger().info('cancel request for goal sent...')
        else:
            self.get_logger().error('mW: cancel error: no goal handle available...')
        #generalize for edge cases

    def miniwalk_cancel_done(self, future):
        cancel_response = future.result()

    def pause_searchwalk_callback(self, request, response):
        if self.running_search:
            self.get_logger().warn('sw: cvs2 interrupted searchwalk...')
            
            self.cancel_miniwalk_goal()
            response.success = True    # write condition to ensure cancellation
        else:
            self.get_logger().error('no searchwalk goals to interrupt...')
            response.success = False
        return response

    def resume_searchwalk_callback(self, request, response):
        self.get_logger().warn('resume sW request received...')

        if self.running_search:
            self.get_logger().warn('resuming searchwalk, requeuing last goal...')
            response.success = True
            self.searchwalk_goal_executor()
        else:
            self.get_logger().warn('no sW goals to resume...')
            response.success = True
        return response

    def stop_searchwalk_callback(self, msg):
        #check if goal handle is none or not
        self.get_logger().warn('stopping searchwalk...')
        self.cancel_miniwalk_goal()
        self.running_search = False

        if self.enable_cv:
            self.run_cvs2(False)
            self.enable_cv = None

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
            coords.z = 2.0 
            goal.coords = coords
            goal.use_guidance = False
            goal.signal_and_wait = False
            goal_list.append(goal)
            if(verbose): print("lat: ", point[0], "\t\tlon: ", point[1])
        
        return goal_list

    def run_cvs2(self, _msg_):
        if not isinstance(_msg_, bool):
        	raise TypeError("run_cvs2: must be of type Bool")
        msg = Bool()
        msg.data = _msg_
        self.set_cvs2_state_publisher.publish(msg)
         


def main(args=None):
    rclpy.init(args=args)

    saam = SearchApproachActionManager()

    executor = MultiThreadedExecutor()

    rclpy.spin(saam, executor=executor)

    saam.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
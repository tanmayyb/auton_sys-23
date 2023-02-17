"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Search and Approach Action Manager (S.A.A.M.)

    - Search Action (Multiwalk)
    - Approach Action
    - Communicates with 'cvs2' and 'rover' nodes

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import MultiThreadedExecutor

from std_msgs.msg import Int32MultiArray
from std_srvs.srv import Trigger

from rover_utils.action import MinimalWalk

class SearchApproachActionManager(Node):

    def __init__(self):
        super().__init__('action_manager')

        self.goal_handle = None
        self.goal_queue = []
        self.goal_queue_last_index = -1
        self.gid = 0
        self.get_logger().info("!action manager created!") 

        self.running_search = False

        self.miniwalk_action_client = ActionClient(
            self, 
            MinimalWalk, 
            'MiniWalkTopic')

        self.load_goals_and_execute_multifibo_subscriber = self.create_subscription(
            Int32MultiArray,
            'multiwalk_action_manager_goals',
            self.load_goals_and_execute_multiwalk,
            10)

        self.cancel_all_multifibo_goals_service = self.create_service(
            Trigger, 
            'cancel_all_multiwalk_goals', 
            self.cancel_all_goals)

    def load_goals_and_execute_multiwalk(self, msg):
        goals = msg.data

        self.reset_goal_queue()

        for i in goals:
            self.add_goal_to_queue(i)

        print(self.goal_queue)
        self.get_logger().info("loaded {0} goals in queue, executing multifibo...".format(len(self.goal_queue)))

        self.running_search = True
        self.execute_all_goals_in_queue()

    def add_goal_to_queue(self, order):
        goal_msg = MinimalWalk.Goal()
        goal_msg.order = order
        self.goal_queue.append(goal_msg)
        self.goal_queue_last_index=self.goal_queue_last_index+1

    def pop_all_goals(self):
        self.get_logger().info("popping all goals")
        for i in range(0, self.goal_queue_last_index+1):
            self.goal_queue.pop(0)
        self.goal_queue_last_index = -1
        self.get_logger().info("all goals popped")

    def reset_goal_queue(self):
        self.goal_queue = []
        self.gid = 0
        self.goal_queue_last_index = -1 

    def execute_all_goals_in_queue(self): #goal manager function
        while not self.miniwalk_action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('waiting for server to become available...')
        
        if(self.running_search):
            if self.gid<=self.goal_queue_last_index:
                goal = self.goal_queue[self.gid]
                print(self.gid, goal)
                self.get_logger().warning('sending fibonacci goal of order: %d' % (goal.order,))
                self.send_goal(goal)
            
            else: #patch this part of code
                self.get_logger().warning('all goals successfully completed: %d' % (goal.order,))
                self.reset_goal_queue()

    def send_goal(self, goal):
        send_goal_future = self.miniwalk_action_client.send_goal_async(
            goal, 
            feedback_callback=self.feedback_callback)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        
        self._goal_handle = goal_handle
        self.get_logger().info('Goal accepted :)')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().warning('Result: {0}'.format(result.sequence))
        
        self.gid = self.gid + 1
        self.execute_all_goals_in_queue()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        print(':{0}'.format(feedback.partial_sequence))

    def cancel_goal(self):
        self.get_logger().error('Sending goal cancel request for Current Goal...')
        cancel_future  = self._goal_handle.cancel_goal_async() #requesting cancel
        cancel_future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().warning('Goal successfully canceled')
        else:
            self.get_logger().warning('Goal failed to cancel')


    def cancel_all_goals(self, request, response):
        self.get_logger().error('Cancel Request Received to Cancel All Goals...')
        
        #stop current goal
        self.cancel_goal()

        #stop future goals
        self.running_search = False

        #reset goal_queue
        self.reset_goal_queue()

        self.get_logger().warning('All Goals Should Now Be Cancelled...')

        return response


def main(args=None):
    rclpy.init(args=args)

    saam = SearchApproachActionManager()

    executor = MultiThreadedExecutor()

    rclpy.spin(saam, executor=executor)

    saam.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
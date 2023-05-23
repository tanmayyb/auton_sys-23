import rclpy, socket
from rclpy.node import Node

from rover_utils.msg import TankDriveMsg
from std_msgs.msg import Empty, Int64

class Teensy(Node):
    def __init__(self):
        super().__init__('teensy_node')

        """
        Networking
        """
        self.UDP_IP = "172.16.10.2"  # Teensy's address
        self.UDP_PORT = 8080  # port
        self.teensy = 0
        """
        Default Teensy Commands
        """
        self.default_drive_msg = 'D_0_128_0_128_0_0_0_0_0_0_0_0_0_0_0_0_128_128_0_0_0'
        self.default_led_msg = 'S_0'

        try:
            self.teensy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.teensy.sendto(self.default_drive_msg.encode(), (  self.UDP_IP, 
                                                        self.UDP_PORT))
            #print("teensy success")
        except:
            print("error booting teensy server")
            #exit file if not booting

        """
        State Variables and Trackers
        """
        self.current_message = self.def_ros2_tank_drive_msg()   #for display of current message
        self.drive_enabled = False                               #for estop
        
        """
        ROS 2 Interfaces
        """
        self.drive_msg_sub = self.create_subscription(
            TankDriveMsg,
            'drive_msg',
            self.drive_msg_sub_callback,
            10)

        self.led_msg_sub = self.create_subscription(
            Int64,
            'led_msg',
            self.led_msg_sub_callback,
            10)

        self.e_stop_sub = self.create_subscription(
            Empty,
            'e_stop',
            self.e_stop_callback,
            10)

        self.enable_drive_sub = self.create_subscription(
            Empty,
            'enable_drive',
            self.enable_drive_callback,
            10)
        
        print("teensy node online!")
        print("drive_enabled state: ", self.drive_enabled)

        """
        Timer for Process Monitoring Purposes
        """
        timer_period  = 0.2
        self.create_timer(timer_period, self.timer_callback)
    

    """Msg Interface Callbacks"""
    def drive_msg_sub_callback(self, msg):
        if self.drive_enabled:
            self.send_to_drive(msg.lpwm, msg.rpwm)
            self.current_message = msg
        else:
            self.send_to_drive(127, 127)

    def led_msg_sub_callback(self, msg):
        self.send_to_led(msg.data)

    def e_stop_callback(self, msg):
        self.drive_enabled = False
        print("drive disabled")

    def enable_drive_callback(self, msg):
        self.drive_enabled = True
        print("drive enabled")

    def timer_callback(self):
        if self.drive_enabled:
            print("LPWM: ", self.current_message.lpwm, "\tRPWM: ", self.current_message.rpwm,  )

    def send_to_drive(self, lpwm, rpwm):
        # convert c2mm to string
        try:
            left_pwm = str(int(lpwm)) 
            right_pwm = str(int(rpwm))
        except:
            left_pwm = str(127) 
            right_pwm = str(127)
        #compile string and send
        msg = 'D_0_'+left_pwm+'_0_'+right_pwm+'_0_0_0_0_0_0_0_0_0_0_0_0_128_128_0_0_0'
        self.teensy.sendto(msg.encode(), (self.UDP_IP, self.UDP_PORT))

    def send_to_led(self,msg):
        msg = 'S_'+str(msg)
        self.teensy.sendto(msg.encode(), (self.UDP_IP, self.UDP_PORT))

    def def_ros2_tank_drive_msg(self):
        msg = TankDriveMsg()
        msg.lpwm = 127
        msg.rpwm = 127
        return msg

def main(args=None):
    rclpy.init(args=args)

    teensy_node = Teensy()
    rclpy.spin(teensy_node)

if __name__ == '__main__':
    try:
        main()

    except:
        print("exiting")

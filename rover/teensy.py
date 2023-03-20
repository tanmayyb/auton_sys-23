import rclpy, socket
from rclpy.node import Node

from rover_utils.msg import TankDriveMsg
from std_msgs.msg import Empty

class Teensy(Node):
    def __init__(self):
        super().__init__('teensy_node')

        """
        Networking
        """
        self.UDP_IP = "172.16.10.2"  # Teensy's address
        self.UDP_PORT = 8080  # port
        self.default_msg = 'D_0_128_0_128_0_0_0_0_0_0_0_0_0_0_0_0_128_128_0_0_0'
        self.teensy = 0

        try:
            self.teensy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.teensy.sendto(self.default_msg.encode(), (  self.UDP_IP, 
                                                        self.UDP_PORT))
            #print("teensy success")
        except:
            print("error booting teensy server")
            #exit file if not booting

        """
        State Variables and Trackers
        """
        self.current_message = self.default_msg     #for display of current message
        self.drive_enabled = True                    #for estop
        
        """
        ROS 2 Interfaces
        """
        self.drive_msg_sub = self.create_subscription(
            TankDriveMsg,
            'TeensySubscriberTopic',
            self.drive_msg_sub_callback,
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

    def drive_msg_sub_callback(self, msg):
        if self.drive_enabled:
            self.send_to_teensy(msg.lpwm, msg.rpwm)
            print(msg)

    def e_stop_callback(self, msg):
        self.drive_enabled = False
        print("drive disabled")

    def enable_drive_callback(self, msg):
        self.drive_enabled = True
        print("drive enabled")

    def send_to_teensy(self, lpwm, rpwm):
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

def main(args=None):
    rclpy.init(args=args)

    teensy_node = Teensy()
    rclpy.spin(teensy_node)

if __name__ == '__main__':
    try:
        main()

    except:
        print("exiting")

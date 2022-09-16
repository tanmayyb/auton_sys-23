import rclpy, socket
from rclpy.node import Node

from rover_utils.msg import TankDriveMsg

class Teensy(Node):
    def __init__(self):
        super().__init__('teensy_node')
        
        self.UDP_IP = "192.168.1.20"  # Teensy's address
    
        self.UDP_PORT = 8080  # port
        self.default_msg = 'D_0_128_0_128_0_0_0_0_0_0_0_0_0_0_0_0_128_128_0_0_0'
        self.teensy = 0

        self.teleop_id = 1
        self.auton_id = 2
        #self.msg_select = True

        try:
            self.teensy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.teensy.sendto(self.default_msg.encode(), (  self.UDP_IP, 
                                                        self.UDP_PORT))
            #print("teensy success")
        except:
            print("error booting teensy server")
        
        self.subscriber = self.create_subscription(
            TankDriveMsg,
            'TeensySubscriberTopic',
            self.subscription_callback,
            10)
        
        print("teensy server operational")

    def subscription_callback(self, msg):
        #if self.msg_select:
        self.send_to_teensy(msg.lpwm, msg.rpwm)
        
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
        print(msg)

def main(args=None):
    rclpy.init(args=args)

    teensy_node = Teensy()
    rclpy.spin(teensy_node)

if __name__ == '__main__':
    try:
        main()

    except:
        print("exiting")

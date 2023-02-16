import socket

class teensy_sender():
    def __init__(self):
        
        self.UDP_IP = "192.168.1.20"  # Teensy's address
    
        self.UDP_PORT = 8080  # port
        self.default_msg = 'D_0_128_0_128_0_0_0_0_0_0_0_0_0_0_0_0_128_128_0_0_0'

        try:
            self.teensy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.teensy.sendto(self.default_msg.encode(), (  self.UDP_IP, 
                                                        self.UDP_PORT))
            #print("teensy success")
        except:
            print("error booting teensy server")
        
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
        #print(msg)
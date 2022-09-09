"""
##########################################
Handler defined for VN-300
Sensor object is created and getter function are used to get updated 'solutions'/values from the sensor 
##########################################
"""
from vnpy import *
from threading import *


"""
Hanndler Class
"""
class vn_handler():

    def __init__(self, devpath):
        self.vn = None
        self.devpath = devpath
        
    def start(self):
        
        """
        Sensor Connection and Object creation for VN-300
        """
        
        while True:
            
            try:
                self.vn = VnSensor()
                self.vn.connect(self.devpath, 115200)
                print("<vnh>: VN-300 module started")
                break

            except:
                print("<vnh>: VN-300 module startup failure")
            print("<vnh>: retrying connection to VN-300")


    """
    Getter functions defined for lhrs server
    """ 

    def ypr(self):
        return self.vn.read_yaw_pitch_roll()
    
    def ins_pos(self):
        return self.vn.read_ins_solution_lla().pos
    
    def gps_lla(self):
        return self.vn.read_gps_solution_lla().lla
    
    def attitude(self):
        return self.vn.any_attitude()
    
    def gps_compass(self):
        return self.vn.read_gps_compass_estimated_baseline()
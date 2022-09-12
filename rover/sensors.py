
import rclpy
from rclpy.node import Node
from rclpy.timer import Timer

from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Point

from vnpy import *
import time, os


class SensorPub(Node):
    def __init__(self):
        super().__init__('nav_sensors_node')
        
        sudoPassword = 'jetson'
        command = 'chmod 666 /dev/ttyUSB0'
        devpath = '/dev/ttyUSB0'
        self.vn = None

        while 1:
            """
            Add port check function
            """
            try:
                
                os.system('echo %s|sudo -S %s' % (sudoPassword, command))
                break
            except:
                self.get_logger().error("Error getting port access permissions from Linux")
                time.sleep(1)

        while 1:
            try:
                self.vn = VnSensor()
                self.vn.connect(devpath, 115200)
                break
            except:
                self.get_logger().error("failed to connect to VN-300, trying again...")
                time.sleep(1)

        self.publisher = self.create_publisher(
            Point,
            'nav_sensor_data',
            10)

        timer_period  = 0.010
        self.create_timer(timer_period, self.timer_callback)

        
    def timer_callback(self):
        """READ SENSOR DATA"""

        lat = self.gps_lla().x,
        lon = self.gps_lla().y,
        yaw = self.ypr().x

        #print(lat, lon, yaw, type(lat), type(lon), type(yaw))

        """PUBLISH SENSOR DATA"""
        msg = Point()
        msg.x = float(lat[0])
        msg.y = float(lon[0])
        msg.z = float(yaw)
        
        self.publisher.publish(msg)
        print(msg)

    
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


def main(args=None):
    rclpy.init(args=args)

    sensor_pub = SensorPub()

    executor = MultiThreadedExecutor()

    try:
        rclpy.spin(sensor_pub, executor=executor)
    except:
        rclpy.shutdown()

if __name__ == '__main__':
    
    main()

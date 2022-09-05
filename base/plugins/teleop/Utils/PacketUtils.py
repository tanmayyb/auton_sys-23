import socket

from plugins.teleop.Utils.Consts import UDP_IP, UDP_PORT

__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done"


class PacketTool:
    def udp_init(self) -> socket:
        """
        Returns a socket
        :return: socket
        """
        print("Network Details")
        print("\tUDP target IP: %s" % UDP_IP)
        print("\tUDP target port: %s" % UDP_PORT)
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

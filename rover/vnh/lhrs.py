"""
##########################################
##########################################
"""

import time, sys
import socket, json
import threading
import os

"""
Import:
    Vector Nav Python library ('vnpy')
    VN module handler ('vn_handler')  
"""
from vnpy import *
from vnh import vn_handler


""" Variables for LHRS Server Socket """
server_socket_address = ('127.0.0.1', 9090)
start_interval = 0.5
stream_interval = 0.1

running = True


""" handler variable """
lhrs = None

   

def init_lhrs():
    while running:

        """enable permission to read from VN-300 System using Python"""
        try:
            sudoPassword = 'j2'
            command = 'chmod 666 /dev/ttyUSB0'
            os.system('echo %s|sudo -S %s' % (sudoPassword, command))
            print("permission granted:", command)
        except:
            print("sudo error")        
        

        """initialise VN-300 module handler"""
        try:
            lhrs = vn_handler('/dev/ttyUSB0')
            lhrs.start()
            time.sleep(stream_interval)
            print("lhrs module setup complete")
            break
        except:
            print("lhrs module startup failure")


init_lhrs() #initialisation function for lhrs module


def run_lhrs_server():

    """ 
    initialisation of lhrs socket 
    """
    lhrs_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lhrs_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    lhrs_socket.bind(server_socket_address)
    
    while running:                  
        print("listening for lhrs client...")
        lhrs_socket.listen(1)
        
        
        while running:
            
            client_socket, address = lhrs_socket.accept()  # Gets a client socket object and address where coming from
            print(f"Connection from {address} has been established!")

            
            """
            Main Loop of LHRS Server
            """
            while running:
            
                time.sleep(stream_interval)
                
                """
                Compilation LHRS data into JSON String
                """
                json_string = {
                    "lat": lhrs.gps_lla().x,
                    "lon": lhrs.gps_lla().y,
                    "bear": lhrs.ypr().x
                }

                print(json_string)
                
                
                """
                String Creation from JSON w/ header insertion
                """
                json_string = json.dumps(json_string)  # Converts the dictionary to JSON
                msg = f"{len(json_string):<10}" + json_string  # Adds a header to the packet
                
                
                """
                Send data to lhrs client
                """
                try:
                    client_socket.send(bytes(msg, 'utf-8')) 
                except:
                    break #breaks out of main loop if error detected

            break #breaks out of middle loop due to error inside inner loop



if __name__ == '__main__':
    
    try:
        thread1 = threading.Thread(target=run_lhrs_server)
        thread1.start()
    
    except KeyboardInterrupt:
        print("stopping server...")
        running = False
        thread1.join()
        sys.exit()    
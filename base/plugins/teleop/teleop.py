from socket import socket
import pygame
import json
from pygame.joystick import Joystick

from threading import *

from plugins.teleop.Utils.Consts import DRIFT_VAL, MAX, NEUTRAL, UDP_IP, UDP_PORT, WATCHDOG_TIME
from plugins.teleop.Utils.ControllerUtils import ControllerTool
# from Utils.PacketUtils import PacketTool

"""
DriveArmCode.py: The file responsible for the Rovers Arm/Drive controls. Sends an encoded packet with all of the 
controller information to the target. Has an integrated watchdog system. Works for the following controllers...

CURRENTLY SUPPORTED CONTROLLERS:
    - XBOX360 (Windows)
    - PS4
    - Gamepad F310

VERSIONS OF LIBRARIES USED:
    - Python: 3.7.0
    - pygame: 2.0.2
"""

__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done"



# kill commands
defaultDriveMsg: str = "D_0_128_0_128"


class teleop_processor(Thread):
    def __init__(self, parent):
        Thread.__init__(self)

        # packetTool = PacketTool()
        self.controllerTool = ControllerTool(self)
        self.controllerCount = 1
        self.leftY = None
        self.rightY = None

        self.leftY_ = None 
        self.rightY_ = None
        
        self.parent = parent

    def set_status_bar_controller_state(self, msg):
        self.parent.set_status_bar_controller_state(msg)
    
    def status_bar_info_text(self, msg):
        self.parent.set_status_bar_controller_info(msg)
    
    def run(self):
        """
        The main loop - starts the program
        """

        pygame.init()
        clock = pygame.time.Clock()
        timerWatchdog = 0

        # sender: socket = packetTool.udp_init()
        controller: Joystick = self.controllerTool.getController()
        self.controllerCount = self.controllerTool.CONTROLLER_COUNT

        running = True

        lastMsg = {}  # used to stop spamming the output
        watchdogMsg = "?"

        while running:
            if pygame.joystick.get_count() < self.controllerCount:
                print("Disconnection detected - sending 'kill' message...")
                # will stop all DRIVE movement
                # sender.sendto(defaultDriveMsg.encode(), (UDP_IP, UDP_PORT))
                controller = self.controllerTool.getController()
                running = False

            else:
                
                self.parent.set_status_bar_controller_state("\tConnected")
                
                # The strings to be sent
                self.leftY: str = "0"
                self.rightY: str = "0"

                self.leftY = self.controllerTool.yoinkControllerReadings(
                    controller, 1)
                self.rightY = str(
                    self.controllerTool.yoinkControllerReadings(controller, 3))

                L2: str = self.controllerTool.yoinkBumperReadings(controller, 4)
                R2: str = self.controllerTool.yoinkBumperReadings(controller, 5)

                if int(R2) > MAX * .9:
                    self.controllerTool.SPEED.revUp()
                elif int(L2) > MAX * .9:
                    self.controllerTool.SPEED.revDown()

                msg = "D_"

                for event in pygame.event.get():
                    if event.type == pygame.JOYBUTTONDOWN:
                        btn = event.__getattribute__('button')

                        """
                        Mode - DRIVE

                        Controls:

                        Start - CHANGE MODE

                        LStick Y - Move left wheels 
                        RStick Y - Move right wheels

                        L1 - Gear Down -> Lowers Speed by a set amount
                        R1 - Gear Up -> Increases Speed by a set amount

                        L2 - Gear Down -> Lowers Speed (Rev)
                        R2 - Gear Up -> Increases Speed (Rev)

                        BTN 1 - Break

                        BTN 2 - 4 -> Different Speed Profiles 
                            BTN 2 - Zooming 
                            BTN 3 - Medium
                            BTN 4 - Slow
                        """

                        if btn == self.controllerTool.MAP.BTN1:
                            btn1 = "1"
                            self.controllerTool.SPEED.setSpeed(0)
                        if btn == self.controllerTool.MAP.BTN2:
                            btn2 = "1"
                            self.controllerTool.SPEED.setSpeed(0.75)
                        if btn == self.controllerTool.MAP.BTN3:
                            btn3 = "1"
                            self.controllerTool.SPEED.setSpeed(0.25)
                        if btn == self.controllerTool.MAP.BTN4:
                            btn4 = "1"
                            self.controllerTool.SPEED.setSpeed(0.10)

                        if btn == self.controllerTool.MAP.BTNL1:
                            L1 = "1"
                            self.controllerTool.SPEED.gearDown()
                        if btn == self.controllerTool.MAP.BTNR1:
                            R1 = "1"
                            self.controllerTool.SPEED.gearUp()

                        if btn == self.controllerTool.MAP.BTNSTART:
                            start = "1"

                    if event.type == pygame.JOYBUTTONUP:
                        btn = event.__getattribute__('button')

                        if btn == self.controllerTool.MAP.BTNLB:
                            leftBtn = "0"
                        if btn == self.controllerTool.MAP.BTNRB:
                            rightBtn = "0"
                        if btn == self.controllerTool.MAP.BTNDUP:
                            dUp = "0"
                        if btn == self.controllerTool.MAP.BTNDDOWN:
                            dDown = "0"
                        if btn == self.controllerTool.MAP.BTNDLEFT:
                            dLeft = "0"
                        if btn == self.controllerTool.MAP.BTNDRIGHT:
                            dRight = "0"
                        if btn == self.controllerTool.MAP.BTN1:
                            btn1 = "0"
                        if btn == self.controllerTool.MAP.BTN2:
                            btn2 = "0"
                        if btn == self.controllerTool.MAP.BTN3:
                            btn3 = "0"
                        if btn == self.controllerTool.MAP.BTN4:
                            btn4 = "0"
                        if btn == self.controllerTool.MAP.BTNL1:
                            L1 = "0"
                        if btn == self.controllerTool.MAP.BTNR1:
                            R1 = "0"
                        if btn == self.controllerTool.MAP.BTNBACK:
                            back = "0"
                        if btn == self.controllerTool.MAP.BTNSTART:
                            start = "0"
                        if btn == self.controllerTool.MAP.BTNHOME:
                            home = "0"

                # construct message

                # Joysticks
                # msg += "LeftPWM" + "_" + leftY + "_" + "RightPWM" + \
                #     "_" + rightY

                msg = {
                    "lpwm": self.leftY,
                    "rpwm": self.rightY,
                }
                self.leftY_, self.rightY_ = self.leftY, self.rightY
                if lastMsg != msg:
                    paren_controller_info_msg = f"  lpwm:{str(self.leftY_)}  rpwm: {str(self.rightY_)}"
                    self.parent.set_status_bar_controller_info("\t"+paren_controller_info_msg)
                    
                    msg = json.dumps(msg)
                    # only needs to print/send the message if there is a change
                    # sender.sendto(msg.encode(), (UDP_IP, UDP_PORT))
                    #print("\tData: " + msg)


                lastMsg = msg
                #clock.tick(120)

                # Watchdog code
                #timerWatchdog += clock.get_time()
                #if timerWatchdog > WATCHDOG_TIME:
                    # sender.sendto(watchdogMsg.encode(), (UDP_IP, UDP_PORT))
                    #timerWatchdog = 0

    def get_pwms(self):
        return self.leftY_, self.rightY_

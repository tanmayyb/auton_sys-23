import pygame
from pygame.joystick import Joystick

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from plugins.teleop.Utils.Consts import BUMPER_VAL, DEFAULT_DRIVE_SPEED, DRIFT_VAL, MAX, MIN, NEUTRAL
from plugins.teleop.Utils.ControllerMapping import Mapping

from plugins.teleop.Utils.DrivingSpeed import DrivingSpeed

__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done"

class ControllerTool:
    
    CONTROLLER_COUNT = 0
    SPEED: DrivingSpeed = DrivingSpeed(DEFAULT_DRIVE_SPEED)

    def __init__(self, parent):
        self.parent = parent        
        self.verbose = False
        # error checking
        if DRIFT_VAL >= 1 or DRIFT_VAL < 0:
            print("Error - DRIFT_VAl is out of bounds\nAborting...")
            exit(1)

        # error checking
        if BUMPER_VAL != -0.05:
            print("Error - BUMPER_VAl is out of bounds\nAborting...")
            exit(1)

    def getController(self) -> Joystick:
        """
        Will return a controller (Joystick class). If none are found, this function will wait until the user connects a
        valid controller. If several controllers are found, the user will be prompted to select the controller they wish
        to use by pressing a button on the preferred device
        :return: Controller (Joystick)
        """
        print("Initializing Hardware")

        pygame.joystick.init()

        totalJoysticks = pygame.joystick.get_count()

        ctr: Joystick
        if totalJoysticks == 0:
            ctr = self.__reconnectJoystick()

        if totalJoysticks > 1:
            ctr = self.__selectController(self.__getAllControllers())
        else:
            ctr = pygame.joystick.Joystick(0)

        # stores the number of currently connected controllers
        self.CONTROLLER_COUNT = pygame.joystick.get_count()

        # assigning button mappings
        self.__assigningButtonMappings(ctr.get_name())

        print("The following Controller will be used")
        self.__displayControllerInfo(ctr)
        print("The Controller is ready for use!")

        return ctr

    def __assigningButtonMappings(self, name: str):
        print("Attempting to map buttons for " + name + "...")
        if name == "Controller (XBOX 360 For Windows)":
            self.__mapXBOX360()
        elif name == "PS4 Controller":
            self.__mapPS4()
        elif name == "Controller (Gamepad F310)":
            self.__mapGamepadF310()
        elif name == "Xbox One S Controller":
            self.__mapXBOX360()
            
        else:
            msg = "ERROR - " + name + " is not supported"
            #print(msg)
            self.parent.status_bar_info_text(msg)
            
            print("Aborting Tool")
            exit(1)
        #print("Mapping successful!\n\tNOTE: If you notice any irregularities in the controls, it is LIKELY a mapping "
        #      "issue...")

    def __mapPS4(self):
        """
        These are the PS4 mappings
        :return:
        """
        BTN1 = 2  # Square
        BTN2 = 0  # X
        BTN3 = 3  # Triangle
        BTN4 = 1  # Circle

        BTNL1 = 9
        BTNR1 = 10

        BTNLB = 7
        BTNRB = 8

        BTNBACK = 4
        BTNSTART = 6
        BTNHOME = 5

        BTNDUP = 11
        BTNDDOWN = 12
        BTNDLEFT = 13
        BTNDRIGHT = 14

        self.MAP = Mapping(BTN1, BTN2, BTN3, BTN4, BTNL1, BTNR1, BTNLB, BTNRB, BTNBACK, BTNSTART, BTNHOME, BTNDUP,
                           BTNDDOWN, BTNDLEFT, BTNDRIGHT)

    def __mapGamepadF310(self):
        """
        These are the GamepadF310 mappings
        :return:
        """
        BTN1 = 2  # X
        BTN2 = 0  # A
        BTN3 = 3  # Y
        BTN4 = 1  # B

        BTNL1 = 4
        BTNR1 = 5

        BTNLB = 8
        BTNRB = 9

        BTNBACK = 6
        BTNSTART = 7
        BTNHOME = -1

        BTNDUP = -1
        BTNDDOWN = -1
        BTNDLEFT = -1
        BTNDRIGHT = -1

        self.MAP = Mapping(BTN1, BTN2, BTN3, BTN4, BTNL1, BTNR1, BTNLB, BTNRB, BTNBACK, BTNSTART, BTNHOME, BTNDUP,
                           BTNDDOWN, BTNDLEFT, BTNDRIGHT)

    def __mapXBOX360(self):
        """
        These are the xbox360 mappings
        :return:
        """
        BTN1 = 2  # X
        BTN2 = 0  # A
        BTN3 = 3  # Y
        BTN4 = 1  # B

        BTNL1 = 4
        BTNR1 = 5

        BTNLB = 8
        BTNRB = 9

        BTNBACK = 6
        BTNSTART = 7
        BTNHOME = 10

        BTNDUP = -1
        BTNDDOWN = -1
        BTNDLEFT = -1
        BTNDRIGHT = -1

        self.MAP = Mapping(BTN1, BTN2, BTN3, BTN4, BTNL1, BTNR1, BTNLB, BTNRB, BTNBACK, BTNSTART, BTNHOME, BTNDUP,
                           BTNDDOWN, BTNDLEFT, BTNDRIGHT)

    def __reconnectJoystick(self) -> Joystick:
        """
        A helper function used to diagnose and fix controller connection issues
        :return: Controller (Joystick)
        """

        if pygame.joystick.get_count() == 0:
            print("Connection Error - No Connected Joysticks Found")
            self.parent.set_status_bar_controller_state("\tDisconnected")
            i = 0
            while pygame.joystick.get_count() == 0:
                pygame.joystick.quit()
                pygame.joystick.init()
                pygame.time.wait(1000)
                self.parent.status_bar_info_text(self.__connectionMsg(0, i))
                i = self.__messageInfo(i)
            if pygame.joystick.get_count() > 0:
                self.parent.set_status_bar_controller_state("\tConnected")

                print("\tConnection found!")
                pygame.joystick.init()  # this MUST be called here
                return pygame.joystick.Joystick

    def __selectController(self, controllers: list) -> Joystick:
        """
        A helper function that will be called when more than one Joystick is detected - will return the Joystick that
        the user 'activates'
        :param controllers: A list containing all found controllers
        :return: Controller (Joystick)
        """

        print("Several Controllers Detected")

        for ctr in controllers:
            self.__displayControllerInfo(ctr)

        print("Press any button on the controller you wish to use...")
        i = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    ctrID = event.__getattribute__('instance_id')
                    print("Input detected")
                    return controllers[ctrID]
            pygame.time.wait(1000)
            print(self.__connectionMsg(1, i))
            i = self.__messageInfo(i)

    def __messageInfo(self, x: int) -> int:
        """
        Just a helper function used for 'message animation' - not very important
        :param x:
        :return: x++ or 0
        """
        if x < 3:
            return x + 1
        else:
            return 0

    def __connectionMsg(self, msgNum: int, x: int) -> str:
        """
        A helper function used to display a 'visual' connection error message
        :param msgNum:
        :param x:
        :return: message
        """
        msg = "\twaiting for controller "
        if msgNum == 0:
            msg += "connection"
        if msgNum == 1:
            msg += "input"
        for _ in range(x):
            msg += "."
        return msg

    def __displayControllerInfo(self, controller: Joystick):
        """
        A helper function used to display the given controllers information
        :param controller:
        """
        # found controller name/id
        name = controller.get_name()
        idValue = controller.get_id()

        # found controller 'detailed specs'
        numAxes = controller.get_numaxes()
        numBalls = controller.get_numballs()
        numButtons = controller.get_numbuttons()
        numHats = controller.get_numhats()
        if self.verbose == True:
            print("Controller Information")
            print("\tName: " + str(name))
            print("\tID: " + str(idValue))
            print("\t\tNumber of Axes: " + str(numAxes))
            print("\t\tNumber of Balls: " + str(numBalls))
            print("\t\tNumber of Buttons: " + str(numButtons))
            print("\t\tNumber of Hats: " + str(numHats))

    def __getAllControllers(self) -> list:
        """
        A helper that returns all controllers
        :return: All controllers
        """
        pygame.joystick.init()
        totalJoysticks = pygame.joystick.get_count()
        ctrList = []
        for i in range(totalJoysticks):
            ctr = pygame.joystick.Joystick(i)
            ctrList.append(ctr)
        return ctrList

    def mapDriveSpeed(self, x: float, mod: float = 0) -> float:
        """
        A function used to map the controllers min/max with the motor min/max values/speeds
        The mod parameter is used to adjust the 'normal' speed; used for corrections!
        :param x: Joystick Value => [-1, 1]
        :param mod: *OPTIONAL => PWM
        :return:
        """

        pwm = self.__mapSpeed(x, self.SPEED.speed())
        pwm += mod

        if MAX >= pwm >= MIN:
            return pwm
        print("ERROR - Drive PWM Value out of bounds")

    def __mapSpeed(self, x: float, speed: float) -> float:
        """
        A helper function used to map the controllers min/max with the motor min/max values/speeds
        :param x: Value to be changed
        :return: Changed value
        """

        outMax: float = MAX
        d: float = 1
        if x < 0:
            outMax = MIN
            d = -1
        return int((x - DRIFT_VAL) * ((outMax - NEUTRAL) * speed) / (d - DRIFT_VAL) + NEUTRAL)

    def __mapBumper(self, x: float) -> float:
        """
        A helper function used to map the bumpers (L2/R2) min/max with the motor min/max values/speeds
        :param x: Value to be changed
        :return: Changed value
        """
        return int((x - (-1 - BUMPER_VAL)) * (MAX - NEUTRAL) / (
            1 - (-1 - BUMPER_VAL)) + NEUTRAL)

    def yoinkControllerReadings(self, controller: Joystick, axis: int) -> str:
        """
        Used to obtain the value of the controller axis - returns the converted string required
        :param controller:
        :param axis:
        :return: converted speed
        """
        raw = controller.get_axis(axis)
        if abs(raw) > DRIFT_VAL:
            if axis % 2:
                return str(MAX - self.mapDriveSpeed(raw))
            return str(self.mapDriveSpeed(raw))
        return str(NEUTRAL)

    def getHatValues(self, controller: Joystick, axis: int) -> tuple:
        """
        Returns the number of 'hats' on a given controller
        :param controller:
        :param axis:
        :return:
        """
        return controller.get_hat(axis)

    def yoinkBumperReadings(self, controller: Joystick, axis: int) -> str:
        """
        Used to obtain the value of the L2/R2 axis - returns the converted string required
        :param controller:
        :param axis:
        :return: converted speed
        """
        raw = controller.get_axis(axis)
        if raw - 1 > BUMPER_VAL:
            return str(self.__mapBumper(raw))
        return str(NEUTRAL)

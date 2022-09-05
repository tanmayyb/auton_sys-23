__author__ = "Joshua Nelson"
__copyright__ = "Copyright 2022, R3 - Ryerson RAMS Robotics"
__credits__ = ["Joshua Nelson"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Joshua Nelson"
__status__ = "Done - Modify as needed"

# PWM constants
MIN: float = 0  # motor speed - min speed
NEUTRAL: float = 128  # motor speed - neutral
MAX: float = 255  # motor speed - max speed

# Packet constants
UDP_IP: str = "192.168.1.20"  # ESP's address
UDP_PORT: int = 8080  # port

# Controller constants
DRIFT_VAL: float = 0.1  # used to adjust for joystick drift - needs to be between 0.0 and 1
BUMPER_VAL: float = -0.05  # don't change this!

# Watchdog ping interval
WATCHDOG_TIME: int = 250

# Speed
DEFAULT_DRIVE_SPEED: float = .5


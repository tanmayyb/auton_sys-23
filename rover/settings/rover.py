"""
ROVER STATE DICT
"""
RVR_DICT = {
    'idle_standby':0,
    'miniwalk':1,
    'teleop':2,
    'approaching_aruco':3,
    'goal_reached':4,    
}

ROVER_STATE_PUB_TIMER_PERIOD = 0.5


"""
LED VARIABLES
"""
"""LED CODES"""
OFF_LED_CODE = 0
RED_LED_CODE = 1
GREEN_LED_CODE = 2
BLUE_LED_CODE = 3
LED_DICT = {
    'STANDBY': 0,
    'AUTONOMOUS MODE':1,
    'SUCCESS': 2,
    'TELEOP MODE': 3
}

"""FLASH GREEN SUBROUTINE"""
FLASH_LED_GREEN_TIMEOUT = 12.0
FLASH_LED_GREEN_ON_DURATION = 0.2
FLASH_LED_GREEN_OFF_DURATION = 0.2







RVR_INFO = ['idle_standby', 'miniwalk', 'teleop', 'approaching_aruco', 'goal_reached']
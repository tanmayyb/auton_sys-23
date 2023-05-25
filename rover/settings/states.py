import numpy as np

SM_DICT = {
    'idle_scan':0,
    'confirm_aruco':1,
    'approach':2,
    'reset':3,
    'interrupt_searchwalk': 4,
    'aruco_reached':5,
    'standby':6}

SM_INFO = ['READY/SCANNING','CONFIRMING...','APPROACHING','RESETING', 'INTERRUPTING SEARCHWALK','TAG REACHED', 'STANDBY']


RVR_DICT = {
    'idle/standby':0,
    'miniwalk':1,
    'teleop':3,
    
}

RVR_INFO = ['IDLE/STANDBY', 'MINIWALKING','', 'TELEOP']
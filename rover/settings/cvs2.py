import numpy as np

SM_DICT = {
    'idle_scan':0,
    'confirm_aruco':1,
    'approach':2,
    'reset':3,
    'interrupt_searchwalk': 4,
    'aruco_reached':5,
    'standby':6}

SM_INFO = ['READY/SCANNING','CONFIRMING...','APPROACHING','RESETING', 'INTERRUPTING SEARCHWALK','TGT REACHED', 'STANDBY']
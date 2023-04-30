"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

    - Calculation of shortest turning angle between arb and target bearing (miniwalk)
    - Cross track error (never used)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
from math import sin


def calculate_heading_error(current_bearing, target_bearing):
    
    """
    determine shortest angle and direction to turn
    https://math.stackexchange.com/questions/110080/shortest-way-to-achieve-target-angle
    """

    T = target_bearing
    C = current_bearing
    alpha = T-C
    beta = T-C + 360
    gamma = T-C - 360
    
    """
    https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    """
    angles = {alpha: abs(alpha), beta: abs(beta), gamma: abs(gamma)}
    heading_error = min(angles, key=angles.get)
        
    return heading_error

def cross_track_error(error_angle, current_distance):
    ct_error = sin(error_angle) * current_distance
    return ct_error

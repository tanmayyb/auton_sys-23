"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Turnings for Miniwalk and Approach Controllers
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

MINIWALK_PID_CONTROL_CONSTS = (0.6,  0.0, 0.1, 40) # good for kerr QUAD GRASS
MINIWALK_AUX_CONTROL_CONSTS = [20,                #drift_const[pwm]
                               [60.0, 11.0, 0.0]] #boost(range[deg], peak[pwm], deadzone[deg]) 

APPROACH_PID_CONTROL_CONSTS = (0.3, 0.0, 0.1, 15)
APPROACH_AUX_CONTROL_CONSTS = [0, 
                               [60.0, 11.0, 0.0]] 

#PID_TUNING_CONSTS = (0.1, 0.0, 0.0)
PID_TUNING_CONSTS = (0.3, 0.0, 0.1)
PID_OUTPUT_LIM_CONSTS = (0, 15)



"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Const Format
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


_AUX_CONTROL_CONSTS = [
                        DRIFT [pwm, <int>]
                        BOOST (  range[deg, <float>], 
                                peak[pwm, <float>], 
                                deadzone[deg, <float>])
                                ] 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

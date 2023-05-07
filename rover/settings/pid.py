"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Turnings for Miniwalk and Approach Controllers
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

MINIWALK_PID_CONTROL_CONSTS = [[0.6,  0.0, 0.1], 
                                30, 0.0]                    # good for kerr QUAD GRASS
MINIWALK_AUX_CONTROL_CONSTS = [20,                          #drift_const[pwm]
                               [60.0, 11.0, 0.0]]           #boost(range[deg], peak[pwm], deadzone[deg]) 

APPROACH_PID_CONTROL_CONSTS = [[0.3, 0.0, 0.1], 
                                15, 20.0]
APPROACH_AUX_CONTROL_CONSTS = [0, 
                               [60.0, 11.0, 0.0]] 



"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Const Format
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

PID_CONTROL_CONSTS = [  [   P                          [const, <float>],
                            I                          [const, <float>],
                            D                          [const, <float>],
                            PID CONTROLLER OUT LIM     [PWM, <int>]]
                            DEADZONE                   [deg, <float>]   ]
                            
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                                
AUX_CONTROL_CONSTS = [  DRIFT                      [pwm, <int>],
                        BOOST [     RANGE          [deg, <float>], 
                                    PEAK           [pwm, <float>], 
                                    DEADZONE       [deg, <float>]]] 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

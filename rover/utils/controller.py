"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Main Auth: Tanmay B.

    - Controller
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

from simple_pid import PID

class controller():
    def __init__(self, 
                 PID_CONTROL_CONSTS, 
                 AUX_CONTROL_CONSTS, 
                 sample_time=0.5):
    
        self.neutral_pwm = 127 

        self.drift_pwm = AUX_CONTROL_CONSTS[0]
        BOOST_CONTROL_CONST = AUX_CONTROL_CONSTS[1]

        self.init_pid_controller(PID_CONTROL_CONSTS, sample_time)
        self.init_boost_controller(BOOST_CONTROL_CONST)
        

    def init_pid_controller(self, PID_CONTROL_CONSTS, sample_time):
        self.Kp = PID_CONTROL_CONSTS[0][0]
        self.Ki = PID_CONTROL_CONSTS[0][1]
        self.Kd = PID_CONTROL_CONSTS[0][2]
        self.pid_out_lim = (-PID_CONTROL_CONSTS[1], 
                             PID_CONTROL_CONSTS[1])
        self.sample_time = sample_time
        self.setpoint = 0.0 
        self.pid = PID(self.Kp, 
                       self.Ki, 
                       self.Kd,
                       self.setpoint, 
                       self.sample_time, 
                       self.pid_out_lim)

        self.pid_usr_dz = PID_CONTROL_CONSTS[2]

    def init_boost_controller(self, BOOST_CONTROL_CONST):        
        self.boost_rng = BOOST_CONTROL_CONST[0]      
        self.boost_peak = BOOST_CONTROL_CONST[1]   
        self.boost_usr_dz = BOOST_CONTROL_CONST[2]   

    def do_pid(self, error):
        control = self.pid(error)
        
        """deadzone"""
        if self.pid_usr_dz !=0.0:
            if (abs(error) < self.pid_usr_dz):
                control = 0.0

        return int(control)

    def control(self, error):
        control = self.do_pid(error)
        boost = self.do_boost(error)
        
        """c2mm (controller to motor mapping) control_val->pwms"""
        left_pwm = self.neutral_pwm - control + self.drift_pwm + boost
        right_pwm = self.neutral_pwm + control + self.drift_pwm + boost

        return (left_pwm, right_pwm)


    def do_boost(self, error_in_degs):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Developed by:   Kevin Tran
        Integration:    Tanmay B.
        Date:           15 Sep 2022

        Code for 'boost' function of the rover
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        #Slope calculation for deadzone, basically calculates what slope should
        #the linear equation have such that at f(0) = peak value
        #Note: they are redundant when not in deadzone
        
        boost_pwm = 0.0

        """deadzone"""
        if (error_in_degs == 0.0):
            boost_pwm = self.boost_peak
        elif (error_in_degs > 0.0 and error_in_degs < +self.boost_rng):
            """left side slope with '+ve' value =  +p/er*error + p"""
            boost_pwm = -(self.boost_peak/self.boost_rng)*error_in_degs + self.boost_peak

        elif (error_in_degs < 0.0 and error_in_degs > -self.boost_rng):
            """right side slope with '-ve' value =  -p/er*error + p"""
            boost_pwm = +(self.boost_peak/self.boost_rng)*error_in_degs + self.boost_peak

        elif abs(error_in_degs) > +self.boost_rng:
            """default deadzone"""
            boost_pwm = 0.0     #deadzone the boost
        
        if abs(error_in_degs) < +self.boost_usr_dz:
            """dampen boost function induced overshoot"""
            boost_pwm = 0.0     #if the error is in 'center' deadzone area

        return int(boost_pwm)
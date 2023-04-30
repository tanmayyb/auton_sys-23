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
        self.Kp = PID_CONTROL_CONSTS[0]
        self.Ki = PID_CONTROL_CONSTS[1]
        self.Kd = PID_CONTROL_CONSTS[2]
        self.pid_out_lim = (-PID_CONTROL_CONSTS[3], 
                             PID_CONTROL_CONSTS[3])
        self.sample_time = sample_time
        self.setpoint = 0.0 
        self.pid = PID(self.Kp, 
                       self.Ki, 
                       self.Kd,
                       self.setpoint, 
                       self.sample_time, 
                       self.pid_out_lim)
        
    def init_boost_controller(self, BOOST_CONTROL_CONST):        
        self.boost_rng = BOOST_CONTROL_CONST[0]      
        self.boost_peak = BOOST_CONTROL_CONST[1]   
        self.boost_usr_dz = BOOST_CONTROL_CONST[2]   

    def control(self, error):
        control = int(self.pid(error))
        boost = self.boost_function(error)
        """c2mm (controller to motor mapping) control_val->pwms"""
        left_pwm = self.neutral_pwm - control + self.drift_pwm + boost
        right_pwm = self.neutral_pwm + control + self.drift_pwm + boost

        return (left_pwm, right_pwm)


    def boost_function(self, error_in_degs):
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

        #Deadzone area
        if (error_in_degs == 0.0):
            boost_pwm = self.boost_peak
        elif (error_in_degs > 0.0 and error_in_degs < +self.boost_rng):
            """left side slope with '+ve' value =  +p/er*error + p"""
            boost_pwm = -(self.boost_peak/self.boost_rng)*error_in_degs + self.boost_peak

        elif (error_in_degs < 0.0 and error_in_degs > -self.boost_rng):
            """right side slope with '-ve' value =  -p/er*error + p"""
            boost_pwm = +(self.boost_peak/self.boost_rng)*error_in_degs + self.boost_peak

        elif (error_in_degs > 0.0 and error_in_degs > + self.boost_rng or error_in_degs < 0.0 and error_in_degs < -self.boost_rng):
            """default deadzone"""
            boost_pwm = 0.0     #deadzone the boost
        
        """dampen boost function induced overshoot"""
        if(error_in_degs > 0.0 and error_in_degs < +self.boost_usr_dz or error_in_degs < 0.0 and error_in_degs > -self.boost_usr_dz):
            boost_pwm = 0.0     #if the error is in 'center' deadzone area

        return int(boost_pwm)
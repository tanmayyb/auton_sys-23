from simple_pid import PID
from pid.boost import boost_function

class pid_controller():
    def __init__(self, pid_const, control_const):
    
        self.neutral_pwm = 127 
        self.drift_pwm = control_const[0]
        self.pid_lim = control_const[1] #limit of how high pid control can get
        self.output_limits = (-self.pid_lim,self.pid_lim)
        
        
        self.setpoint = 0 
        self.sample_time = 0.5
        
        self.pid_error = None
        self.control = None
        self.boost = None

        
        self.Kp = pid_const[0]
        self.Ki = pid_const[1]
        self.Kd = pid_const[2]
        
        self.pid = PID(self.Kp, self.Ki, self.Kd,
                        self.setpoint, self.sample_time, self.output_limits)        
        


    def do_pid(self, error):
        control = self.pid(error)
        #update trackers
        self.pid_error  = error
        self.control  = control 
        return control

    def do_boost(self, error):
        boost = boost_function(error)
        self.boost = boost
        return boost
    
    def do_c2mm(self,  control, boost):
        left_pwm = self.neutral_pwm - int(control) + self.drift_pwm + boost
        right_pwm = self.neutral_pwm + int(control)+ self.drift_pwm + boost

        return (left_pwm, right_pwm)


    def get_pid_error(self):
        return self.pid_error
    def set_pid_error(self, error):
        self.pid_error  = error
    def set_control(self, control):
        self.control  = control
    def get_control(self):
        return self.control

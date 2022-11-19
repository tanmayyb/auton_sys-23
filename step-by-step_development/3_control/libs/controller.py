from simple_pid import PID

class pid_controller():
    def __init__(self, localiser, dims, pid_const=(0.170,  0.0, 0.1), control_const=(0, 100)):
        
        self.neutral_pwm = 0 
        self.drift_pwm = control_const[0]
        self.pid_lim = control_const[1] #limit of how high pid control can get
        self.output_limits = (-self.pid_lim,self.pid_lim)
        
        self.localiser = localiser
        
        self.setpoint = 0 
        self.sample_time = 0.5
        
        self.pid_error = None
        self.control = None
        self.boost = None

        self.Kp = pid_const[0]
        self.Ki = pid_const[1]
        self.Kd = pid_const[2]
        
        self.map_dim_x = dims[0]
        self.map_dim_y = dims[1]


        self.pid = PID(self.Kp, self.Ki, self.Kd,
                        self.setpoint, self.sample_time, self.output_limits)        
        
    def calc_error(self):
        cX = self.localiser.get_cX()
        if(len(cX) != 0):
            center_of_mass = sum(cX)/len(cX)
            unmapped_error_relative_to_midline = center_of_mass - self.map_dim_x/2
            #mapped_error = map_error(unmapped_error_relative_to_midline)
            #self.pid_error = mapped_error
            self.pid_error =unmapped_error_relative_to_midline
            return 1
        else:
            return None

    # def map_error(self, unmapped_error):
    #     #https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
    #     leftSpan = leftMax - leftMin
    #     rightSpan = rightMax - rightMin

    #     valueScaled = float(value - leftMin) / float(leftSpan)
    
    #     mapped_error = rightMin + (valueScaled * rightSpan)

    #     return mapped_error

    def do_pid(self):
        control = self.pid(self.pid_error)
        #update trackers
        self.control  = control
        #return self.control

    def get_pid_c2mm(self):
        if(self.calc_error() != None):
            self.do_pid()
            c2mm_vals = self.do_c2mm(self.control)
        else:
            return None
        return c2mm_vals
        
    
    def do_c2mm(self,  control):
        left_pwm = self.neutral_pwm - int(control) + self.drift_pwm 
        right_pwm = self.neutral_pwm + int(control)+ self.drift_pwm

        return (left_pwm, right_pwm)


    def get_pid_error(self):
        return self.pid_error
    def set_pid_error(self, error):
        self.pid_error  = error
    def set_control(self, control):
        self.control  = control
    def get_control(self):
        return self.control
"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Developed by:   Kevin Tran
Integration:    Tanmay B.
Date:           15 Sep 2022

Code for 'boost' function of the rover
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def boost_function(error_in_degs, consts=[60.0, 11.0, 0.0]):


        """
        MUST BE FLOAT
        """
        er = consts[0]       #error range [degr]
        peak = consts[1]     #peak value of boost function [pwm]
        deadzone = consts[2]

        #Slope calculation for deadzone, basically calculates what slope should
        #the linear equation have such that at f(0) = peak value
        #Note: they are redundant when not in deadzone
        
        boost_pwm = 0.0

        #Deadzone area
        if (error_in_degs == 0.0):
            boost_pwm = peak
        elif (error_in_degs > 0.0 and error_in_degs < +er):
            """
            left side slope with '+ve' value =  +p/er*error + p
            """
            boost_pwm = -(peak/er)*error_in_degs + peak
        elif (error_in_degs < 0.0 and error_in_degs > -er):
            """
            right side slope with '-ve' value =  -p/er*error + p
            """
            boost_pwm = +(peak/er)*error_in_degs + peak
        elif (error_in_degs > 0.0 and error_in_degs > +er or error_in_degs < 0.0 and error_in_degs < -er):
            """
            deadzone
            """
            boost_pwm = 0.0     #no boost

        return int(boost_pwm)
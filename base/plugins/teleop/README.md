--- Drive Auton Code ---
*Author: Joshua Nelson*

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**How To Run:**
Launch the DriveAutonCode.py file found within the DriveAutonCode directory. 

Ensure that pygame(version 2.0.2+) is installed. 

The program will only work if one of the following controller brands are used: XBOX360, PS4, or the Gamepad F310 controller. 

To add more controllers, go to the ControllerUtils.py file, navigate to the __assigningButtonMappings function, add another 
condition to check for __mapNEWNAMEHERE(), then create the new mapping function following the format used for the others 
(or just ask me :) ). 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Output:**
The program will send a string of the following form to the target: *"D_LeftPWM_128_RightPWM_128"*. The firmware can handle 
this request, so DO NOT trim the string by excluding the LeftPWM and RightPWM entries!

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Possible Pathing Issue:**
If you ever experience an error similar to *'Module "X" not found...'*, may God help you.

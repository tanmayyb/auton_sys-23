import cv2,sys
sys.path.append("..") 

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.localiser import aruco_localiser
from libs.overlay import overlay_on
from libs.controller import pid_controller
from libs.sender import teensy_sender

from settings.pid import *

def main():

    stream = streamer()
    frame_dims = stream.get_frame_dims()

    detector = aruco_detector()
    localiser = aruco_localiser(detector, dims=frame_dims)
    overlay_handler = overlay_on(detector, dims=frame_dims)

    pid = pid_controller(localiser, frame_dims, pid_const=PID_TUNING_CONSTS)
    teensy = teensy_sender()

    loop = True
    while loop:
        ret, frame = stream.get_frame()

        # detector detects 
        detector.detect_aruco_marker(frame)
        localiser.do_localisation()
        
        val = pid.get_pid_c2mm()        
        if(val != None):
            print(val, pid.fetch_error())
            teensy.send_to_teensy(val[0], val[1])
        # overlay asked to zip and overlay data
        frame = overlay_handler.put_overlay(frame,localiser=localiser, use_localiser=True, controller=pid, plot_center_of_mass=True)

        stream.display_frames(frame)
        loop = stream.check_for_exit_keypresses()


    #cleanup video pointers
    cv2.destroyAllWindows()
    stream.stop()

if __name__ == "__main__":
    main()
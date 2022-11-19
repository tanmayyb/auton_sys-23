import cv2,sys
sys.path.append("..") 

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.localiser import aruco_localiser
from libs.controller import pid_controller


from libs.overlay import overlay_on

def main():

    stream = streamer()
    frame_dims = stream.get_frame_dims()

    detector = aruco_detector()
    localiser = aruco_localiser(detector, dims=frame_dims)
    overlay_handler = overlay_on(detector, dims=frame_dims)

    pid = pid_controller(localiser, frame_dims)

    loop = True
    while loop:
        ret, frame = stream.get_frame()

        # detector detects 
        detector.detect_aruco_marker(frame)
        localiser.do_localisation()
        
        print(pid.get_pid_c2mm())

        # overlay asked to zip and overlay data
        frame = overlay_handler.put_overlay(frame,localiser=localiser, use_localiser=True)

        stream.display_frames(frame)
        loop = stream.check_for_exit_keypresses()


    #cleanup video pointers
    cv2.destroyAllWindows()
    stream.stop()

if __name__ == "__main__":
    main()
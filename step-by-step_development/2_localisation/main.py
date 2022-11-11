import cv2,sys
sys.path.append("..") 

from libs.streamer import streamer
from libs.detector import aruco_detector
from libs.overlay import overlayer

def main():

    detector = aruco_detector()
    stream = streamer()
    overlay_handler = overlay_on(detector)

    loop = True
    while loop:
        ret, frame = stream.get_frame()
        
        # detector detects 
        detector.detect_aruco_marker(frame)

        # overlay asked to zip and overlay data
        frame = overlay_handler.put_overlay(frame)

        stream.display_frames(frame)
        loop = stream.check_for_exit_keypresses()


    #cleanup video pointers
    cv2.destroyAllWindows()
    stream.stop()

if __name__ == "__main__":
    main()
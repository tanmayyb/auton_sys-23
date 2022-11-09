import cv2,sys
sys.path.append("..") 

from libs.streamer import streamer
from libs.frame_processor import aruco_detector

def main():

    detector = aruco_detector()
    stream = streamer()

    loop = True
    while loop:
        ret, frame = stream.get_frame()
        detect_params = detector.detect_aruco_marker(frame)
        detector.draw_bouding_boxes(frame, detect_params)

        
        stream.display_frames(frame)
        loop = stream.check_for_exit_keypresses()


    #cleanup video pointers
    cv2.destroyAllWindows()
    cap.stop()

if __name__ == "__main__":
    main()
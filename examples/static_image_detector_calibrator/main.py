import sys
sys.path.append("..") 

import cv2, time
from img.img import *
from libs.detection_handler import detection_handler


def main():
    
    detector = detection_handler()
    frame = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

    frame = cv2.resize(frame, IMAGE_RESIZE_DIMS)        
    response, frame = detector.detect_aruco_marker(frame)

    loop = True
    while loop:
        
        cv2.imshow(
            "static image aruco detection result: "+str(response),
            frame)
        key = cv2.waitKey(1) & 0xFF 

        if key == ord("m"):
            response, frame = detector.detect_aruco_marker(frame)

        #if q is pressed, break from while loop
        if key == ord("q"):
            break

    #cleanup video pointers
    cv2.destroyAllWindows()
    cap.stop()

if __name__ == "__main__":
    main()
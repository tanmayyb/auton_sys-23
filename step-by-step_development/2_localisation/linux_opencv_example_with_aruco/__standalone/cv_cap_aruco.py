from settings.video import *
from aruco_dict.aruco_dict import *

import cv2
from cv2 import CAP_GSTREAMER
from pipeline import *

import argparse
import time
import sys 


def create_argument_parser():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-t", "--type", type=str,
        default="DICT_4X4_50",  
        help="DICT_4X4_50")
    args = vars(ap.parse_args())

    # #verify supplied tag exists 
    # if ARUCO_DICT.get(args["type"], None) is None:
    #     print("[INFO] ArUCo tag of '{}' is not supported".format(
    #         args["type"]))
    #     sys.exit(0)
    return args


def load_arcuo_dict(args):
    # load the ArUCo dictionary, grab the ArUCo parameters
    print("[INFO] detecting '{}' tags...".format(args["type"]))
    arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
    arucoParams = cv2.aruco.DetectorParameters_create()

    #initialize video stream and allow camera sensor to warm up 
    print("[INFO] starting video stream...")
    #vs = VideoStream(src = 1).start()

    print("GST COMMAND:\n"+gst_command)
    return arucoDict, arucoParams


def detect_aruco_marker(frame, arucoDict, arucoParams):
    #detect markers in the current frame 
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict,
    parameters=arucoParams)
    flag = 0
    #parse the results ... the same from detectImg.py
    if len(corners) > 0:
        flag = 1 #tag detected
        ids = ids.flatten() #flatten the the ID List, all in one row of an array

        #loop over detected corners
        for (markerCorners,markerID) in zip (corners, ids): #zip combines the corners and id, essentially creates a relationship
            #extract marker corners
            corners = markerCorners.reshape((4,2)) #markerCorners as a 4x2 array 
            (topLeft, topRight, bottomRight, bottomLeft) = corners #1x1,2: topLeft, #2x1,2: topRight, etc 

            #convert each x-y pairs to integers 
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            
            #draw on frame
            #draw the boundary box
            cv2.line(frame, topLeft, topRight, (0,255,0),2)
            cv2.line(frame, topRight, bottomRight, (0,255,0),2)
            cv2.line(frame, bottomRight, bottomLeft, (0,255,0),2)
            cv2.line(frame, bottomLeft, topLeft, (0,255,0),2)

            #compute center
            cX = int((topLeft[0] + bottomRight[0])/2.0)
            cY = int((topLeft[1] + bottomRight[1])/2.0)
            #draw center
            cv2.circle(frame, (cX,cY),4,(0,255,0),-1)

            #draw markerID on frame
            cv2.putText(frame, str(markerID),(topLeft[0],topLeft[1]-15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
            #print("[INFO] ArUco marker ID: {}".format(markerID))


def main():
    flag = 0 #does not detect tag

    args = create_argument_parser()
    arucoDict, arucoParams = load_arcuo_dict(args)

    cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)

    loop = True
    while loop:
        #grab the frame from the threaded video stream and resize it to max width of 1000px
        ret, frame = cap.read()
        frame = cv2.resize(frame, VIDEO_RESIZE_DIMS)
        detect_aruco_marker(frame, arucoDict, arucoParams)
        
        #show output frame
        cv2.imshow("GST_Stream_for_Aruco",frame)
        key = cv2.waitKey(1) & 0xFF #wait for a key press for 1ms and then and then continue with video 
                                    #0xFF AND waitkey(1) gives you waitkey(1)

        #if q is pressed, break from while loop
        if key == ord("q"):
            break

    #cleanup video pointers
    cv2.destroyAllWindows()
    cap.stop()

if __name__ == "__main__":
    main()


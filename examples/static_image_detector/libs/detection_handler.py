import cv2, argparse
from settings.aruco_dict import *


class detection_handler():
    def __init__(self):
        self.args = self.create_argument_parser()
        self.arucoDict, self.arucoParams = self.load_arcuo_dict(self.args)

    def create_argument_parser(self):
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument(
            "-t", "--type", type=str,
            default="DICT_4X4_50",  
            help="DICT_4X4_50")
        args = vars(ap.parse_args())

        return args

    def load_arcuo_dict(self, args):
        # load the ArUCo dictionary, grab the ArUCo parameters
        print("[INFO] detecting '{}' tags...".format(args["type"]))
        arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
        arucoParams = cv2.aruco.DetectorParameters_create()
        return arucoDict, arucoParams

    def process_corners(self, corners):
        (topLeft, topRight, bottomRight, bottomLeft) = corners #1x1,2: topLeft, #2x1,2: topRight, etc 

        #convert each x-y pairs to integers 
        topLeft = (int(topLeft[0]), int(topLeft[1]))
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))

        return topLeft, topRight, bottomRight, bottomLeft

    def draw_corners(self, topLeft, topRight, bottomRight, bottomLeft):
        #draw on frame
        #draw the boundary box
        sw = 5 #strokeweight
        cv2.line(self.frame, topLeft, topRight, (0,255,0),sw)
        cv2.line(self.frame, topRight, bottomRight, (0,255,0),sw)
        cv2.line(self.frame, bottomRight, bottomLeft, (0,255,0),sw)
        cv2.line(self.frame, bottomLeft, topLeft, (0,255,0),sw)

    def process_center(self, topLeft, bottomRight):
        #compute center
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        return cX, cY

    def draw_center(self, cX, cY):
        cv2.circle(self.frame, (cX,cY),4,(0,255,0),-1)
    
    def draw_text(self, topLeft, markerID):
        fs = 2 #fontsize
        fw = 5 #fontweight
        cv2.putText(self.frame, 
            str(markerID),
            (topLeft[0],topLeft[1]-15),
            cv2.FONT_HERSHEY_SIMPLEX, fs, (0,255,0), fw)
        
    def detect_aruco_marker(self, frame):
        
        self.frame = frame
        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            self.frame, 
            self.arucoDict,
            parameters=self.arucoParams)
        
        flag = 0
        #parse the results ... the same from detectImg.py
        if len(corners) > 0:
            flag = 1 #tag detected
            ids = ids.flatten() #flatten the the ID List, all in one row of an array

            #loop over detected corners
            for (markerCorners,markerID) in zip (corners, ids): #zip combines the corners and id, essentially creates a relationship
                #extract marker corners
                corners = markerCorners.reshape((4,2)) #markerCorners as a 4x2 array 
                
                topLeft, topRight, bottomRight, bottomLeft = self.process_corners(corners)
                self.draw_corners(topLeft, topRight, bottomRight, bottomLeft)
                cX,cY = self.process_center(topLeft, bottomRight)
                self.draw_center(cX, cY)
                self.draw_text(topLeft, markerID)
                
                #print("[INFO] ArUco marker ID: {}".format(markerID))

        return flag, self.frame

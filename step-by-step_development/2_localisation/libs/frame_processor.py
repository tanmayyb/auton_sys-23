from settings.aruco_dict import *
import cv2, argparse, time, sys 


class aruco_detector():
    def __init__(self):
        self.args = self.create_argument_parser()
        self.arucoDict, self.arucoParams = self.load_arcuo_dict(self.args);
    
    def create_argument_parser(self):
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

    def load_arcuo_dict(self, args):
        # load the ArUCo dictionary, grab the ArUCo parameters
        #print("[INFO] detecting '{}' tags...".format(args["type"]))
        arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
        arucoParams = cv2.aruco.DetectorParameters_create()

        return arucoDict, arucoParams

    def detect_aruco_marker(self, frame):
        #detect markers in the current frame 
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, self.arucoDict,
        parameters=self.arucoParams)
        return (corners, ids, rejected)

    def draw_corners(self, frame, topLeft, topRight, bottomRight, bottomLeft):
        #convert each x-y pairs to integers 
        topLeft = (int(topLeft[0]), int(topLeft[1]))
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        
        sw = 5#stroke weight
        #draw the boundary box
        cv2.line(frame, topLeft, topRight, (0,255,0),sw)
        cv2.line(frame, topRight, bottomRight, (0,255,0),sw)
        cv2.line(frame, bottomRight, bottomLeft, (0,255,0),sw)
        cv2.line(frame, bottomLeft, topLeft, (0,255,0),sw)

        return frame, topLeft, topRight, bottomRight, bottomLeft
        
    def draw_center(self, frame, topLeft, bottomRight):
        #compute and draw center
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        cv2.circle(frame, (cX,cY),4,(0,255,0),-1)
        return frame, cX, cY

    def draw_texts(self, frame, topLeft, markerID):
        #draw markerID on frame
        cv2.putText(frame, str(markerID),(topLeft[0],topLeft[1]-15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    def draw_bouding_boxes(self,frame, detect_params):
        corners, ids, rejected = detect_params
        if len(corners) > 0:
            flag = 1 #tag detected
            ids = ids.flatten() #flatten the the ID List, all in one row of an array

            #loop over detected corners
            for (markerCorners,markerID) in zip (corners, ids): #zip combines the corners and id, essentially creates a relationship
                #extract marker corners
                corners = markerCorners.reshape((4,2)) #markerCorners as a 4x2 array 
                (topLeft, topRight, bottomRight, bottomLeft) = corners #1x1,2: topLeft, #2x1,2: topRight, etc 

                frame, topLeft, topRight, bottomRight, bottomLeft = self.draw_corners(frame, topLeft, topRight, bottomRight, bottomLeft)

                frame, cX, cY = self.draw_center(frame, topLeft, bottomRight)
                self.draw_texts(frame, topLeft, markerID)
        return frame

    def show_user_graphics(self, frame):
        height = frame.shape[0]
        width = frame.shape[1]
        frame = self.put_midline(frame, width, height)

        return frame

    def put_midline(self,frame, width, height):
        centerX = width/2.0
        topCenter = (int(centerX), 0)
        bottomCenter = (int(centerX), height)
        cv2.line(frame, topCenter, bottomCenter, (0,0,255), 5)
        return frame

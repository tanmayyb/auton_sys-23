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

                #convert each x-y pairs to integers 
                topLeft = (int(topLeft[0]), int(topLeft[1]))
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                
                #draw the boundary box
                cv2.line(frame, topLeft, topRight, (0,255,0),2)
                cv2.line(frame, topRight, bottomRight, (0,255,0),2)
                cv2.line(frame, bottomRight, bottomLeft, (0,255,0),2)
                cv2.line(frame, bottomLeft, topLeft, (0,255,0),2)

                #compute and draw center
                cX = int((topLeft[0] + bottomRight[0])/2.0)
                cY = int((topLeft[1] + bottomRight[1])/2.0)
                cv2.circle(frame, (cX,cY),4,(0,255,0),-1)

                #draw markerID on frame
                cv2.putText(frame, str(markerID),(topLeft[0],topLeft[1]-15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

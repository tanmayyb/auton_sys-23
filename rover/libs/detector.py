from settings.aruco_dict import *
import cv2, argparse, time, sys 

class aruco_detector():
    def __init__(self):
        self.args = self.create_argument_parser()
        self.arucoDict, self.arucoParams = self.load_arcuo_dict(self.args);
        self.marker_params = None
        self.aruco_detection_state = False

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
        #print("[INFO] detecting '{}' tags...".format(args["type"]))
        arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
        arucoParams = cv2.aruco.DetectorParameters_create()
        return arucoDict, arucoParams

    def do_aruco_marker_detection(self, frame):
        #detect markers in the current frame 
        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            frame, 
            self.arucoDict,
            parameters=self.arucoParams)

        self.marker_params = (corners, ids)

        self.aruco_detection_state = True if ids != None else False

    def is_aruco_detected(self):
        return self.aruco_detection_state

    def zip_markers(self, corners, ids):
        self.zipped_marker_data = zip(corners, ids)

    def get_marker_params(self):
        return self.marker_params
import cv2
import numpy as np
import utils.max_segment 
from settings.aruco import MIN_ARUCO_DIST
import time

class aruco_localiser():
    def __init__(self, detector, dims=None, fov=None):
        self.width = dims[0]
        self.height = dims[1]
        self.fov = fov
        self.detector = detector

        self.cX = []
        self.cY = []

        self.corners = None 
        self.ids = None

        self.center_of_mass = None


        self.intrinsic_camera_matrix_coeff = np.array(((933.15867, 0, 657.59),(0,933.1586, 400.36993),(0,0,1)))
        self.intrinsic_camera_distortion_coeff = np.array((-0.43948,0.18514,0,0))

        self.approached_aruco = None

    def do_localisation(self):
        self.get_and_compute_center_params()
    
    def get_and_compute_center_params(self):
        self.corners, self.ids = self.detector.get_marker_params()
        self.computer_centers(self.corners, self.ids)
        for corners in self.corners:
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(
                corners, 
                22.0, 
                self.intrinsic_camera_matrix_coeff,
                self.intrinsic_camera_distortion_coeff)   
            if len(tvec) > 0: 
                distance = tvec[0][0][2]
                self.approached_aruco = True if distance < MIN_ARUCO_DIST else False 
                #print("aruco approached? ", self.approached_aruco)           

    '''
        output of print(corners, ids):

        [array([[[1106.,  626.],
                [ 936.,  598.],
                [ 980.,  432.],
                [1147.,  447.]]], dtype=float32), 
                array([[[524., 451.],
                    [472., 219.],
                    [673., 188.],
                    [723., 405.]]], dtype=float32)] 
                    
        [[4] [1]]

    '''
    
    def calculate_approach_error(self):
        cX = self.cX_array
        if(len(cX) != 0):
            self.center_of_mass = float(sum(cX))/float(len(cX))
            unmapped_error = self.center_of_mass - self.width/2.0
            mapped_error = self.map_error(unmapped_error)
            self.pid_error = mapped_error
            return mapped_error
        else:
            self.center_of_mass = None
            return None

    def map_error(self, unmapped_error):
        mapped_error = (self.fov/self.width)*unmapped_error
        return mapped_error

    def computer_centers(self, corners,  ids):
        
        self.cX_array  = []
        self.cY_array = []
        if(corners):
            for tag in corners:
                topLeft = tag[0][1]
                bottomRight = tag[0][3]
                #print(topLeft, topRight)
                cX, cY = self.compute_marker_center(topLeft, bottomRight)
                self.cX_array.append(cX)
                self.cY_array.append(cY)
            #print(corners, ids)
            #print(self.cX_array)
    
    def get_center_of_mass(self):
        return self.center_of_mass
    
    def fetch_center_arrays(self):
        return self.cX_array, self.cY_array

    def get_cX(self):
        return self.cX_array

    def compute_marker_center(self, topLeft, bottomRight):
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        return cX, cY
    
    def compute_aruco_dist_measure(self):
        """
        find the magnitude of the largest segment (edge/diagonal)
        """ 
        #find max seg given list of points
        #scale max seg acc. to some ratio
        #if greater than required ratio flag in cvs2 (ask to stop if in single approach mode)
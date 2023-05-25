import cv2
from settings.aruco import *
#import utils.max_segment 

class aruco_processor():
    def __init__(self, detector, dims=None, fov=None):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Cam Info
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.width = dims[0]
        self.height = dims[1]
        self.fov = fov
        self.detector = detector
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Main Variables
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.corners = None 
        self.ids = None

        self.cX_array  = []
        self.cY_array = []
        self.distances_array = []
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Derived Variables
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        self.center_of_mass = None
        self.mean_distance_of_aruco_markers = None
        self.min_aruco_distance_approached = None

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    main functions
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def do_aruco_processing(self):
        self.corners, self.ids = self.detector.get_marker_params()
        if(self.corners):
            self.compute_ar_tags()
        else:
            self.min_aruco_distance_approached = False

    def compute_ar_tags(self):
        self.cX_array  = []
        self.cY_array = []
        self.distances_array = []
        for ar_tag in self.corners:
            self.compute_marker_center(ar_tag)
            self.compute_marker_distances(ar_tag)
        self.process_aruco_mean_distances()



    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    computer centers and distances to aruco tags
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def compute_marker_center(self, ar_tag):
        topLeft = ar_tag[0][1]
        bottomRight = ar_tag[0][3]
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        self.cX_array.append(cX)
        self.cY_array.append(cY)
    
    def compute_marker_distances(self, ar_tag):
        rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(
            ar_tag, 
            ARUCO_MARKER_SIZE_IN_CM, 
            MATRIX_COEFF,
            DISTORTION_COEFF)   
        if len(tvec) > 0: 
            self.distances_array.append(tvec[0][0][2])
            
    

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    calulate approach error and find mean of distances
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
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
    
    def process_aruco_mean_distances(self):
        self.mean_distance_of_aruco_markers = float(sum(self.distances_array))/float(len(self.distances_array))
        if self.mean_distance_of_aruco_markers < MIN_ARUCO_APPROACH_DIST:
            self.min_aruco_distance_approached = True
        else: 
            self.min_aruco_distance_approached = False

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    getter and fetcher functions
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    def get_center_of_mass(self):
        return self.center_of_mass
    
    def fetch_center_arrays(self):
        return self.cX_array, self.cY_array

    def get_cX(self):
        return self.cX_array
    
    def get_min_aruco_distance_approached(self):
        return self.min_aruco_distance_approached

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Format of Corners and IDs
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
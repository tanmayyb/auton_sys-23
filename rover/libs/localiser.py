import cv2


class aruco_localiser():
    def __init__(self, detector, dims=None):
        self.width = dims[0]
        self.height = dims[1]
        self.detector = detector

        self.cX = []
        self.cY = []

        self.corners = None 
        self.ids = None

    def do_localisation(self):
        self.get_and_compute_center_params()
    
    def get_and_compute_center_params(self):
        self.corners, self.ids = self.detector.get_marker_params()
        self.computer_centers(self.corners, self.ids)

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
    
    def find_xpos_relative_to_midline(self):
        pass
    
    def fetch_center_arrays(self):
        return self.cX_array, self.cY_array

    def get_cX(self):
        return self.cX_array

    def compute_marker_center(self, topLeft, bottomRight):
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        return cX, cY
import cv2


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
    
    def calculate_approach_error(self):
        cX = self.cX_array
        if(len(cX) != 0):
            self.center_of_mass = sum(cX)/len(cX)
            unmapped_error = self.center_of_mass - self.width/2
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
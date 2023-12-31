import cv2

class overlay_on():
    def __init__(self, detector=None, processor=None, dims=None):
        self.frame = None
        self.width = dims[0]
        self.height = dims[1]
        self.detector = detector
        self.processor = processor

    def convert_corners_to_ints(self, topLeft, topRight, bottomRight, bottomLeft):
        topLeft = (int(topLeft[0]), int(topLeft[1]))
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        return topLeft, topRight, bottomRight, bottomLeft

    def load_marker_params(self):
        self.marker_params = self.detector.get_marker_params()

    def put_overlay(self, 
                    frame, 
                    draw_bounding_box=True, 
                    processor=None, 
                    use_processor=False, 
                    plot_center_of_mass=False, 
                    state_text=None):
        
        self.frame = frame
        self.processor = processor
        self.load_marker_params() #fetch corners from marker
        self.put_overlay_for_each_marker(enable=draw_bounding_box)
        self.put_processor_overlay(enable=use_processor)
        self.draw_midline()
        self.put_center_of_mass_overlay(enable=plot_center_of_mass)
        self.put_state_text(state_text)

        return self.frame

    def put_center_of_mass_overlay(self, enable):
        if enable:
            center_of_mass = self.processor.get_center_of_mass()
            if(center_of_mass != None):
                cv2.circle(self.frame, (int(center_of_mass), int(self.height/2)),10,(0,255,255),-1)


    def put_processor_overlay(self, enable):
        if enable:
            cX, cY  = self.processor.fetch_center_arrays()
            if(cX and cY):
                for center_of_each_tag in zip(cX, cY):
                    sw = 4
                    COLOR = (0, 0, 255) #BGR
                    #line from midline to the tag                    
                    cv2.line(self.frame, 
                    (int(self.width/2.0), center_of_each_tag[1]), 
                    (center_of_each_tag[0], center_of_each_tag[1]), 
                    COLOR, sw)
                #print(cX, cY)

    def put_overlay_for_each_marker(self, enable):
        if enable:
            frame = self.frame
            corners, ids = self.marker_params

            if len(corners) > 0:
                ids = ids.flatten() #flatten the the ID List, all in one row of an array
                
                for (markerCorners,markerID) in zip (corners, ids): #zip combines the corners and id, essentially creates a relationship
                    corners = markerCorners.reshape((4,2)) #markerCorners as a 4x2 array 
                    
                    (topLeft, topRight, bottomRight, bottomLeft) = corners #1x1,2: topLeft, #2x1,2: topRight, etc 
                    
                    topLeft, topRight, bottomRight, bottomLeft = self.convert_corners_to_ints(topLeft, topRight, bottomRight, bottomLeft)
                    self.draw_bounding_box(topLeft, topRight, bottomRight, bottomLeft)
                    self.draw_texts(topLeft, markerID)
                    self.draw_center(topLeft, bottomRight)

            self.frame = frame

    def draw_bounding_box(self, topLeft, topRight, bottomRight, bottomLeft):
        sw = 5#stroke weight
        cv2.line(self.frame, topLeft, topRight, (0,255,0),sw)
        cv2.line(self.frame, topRight, bottomRight, (0,255,0),sw)
        cv2.line(self.frame, bottomRight, bottomLeft, (0,255,0),sw)
        cv2.line(self.frame, bottomLeft, topLeft, (0,255,0),sw)


    def compute_marker_center(self, topLeft, bottomRight):
        cX = int((topLeft[0] + bottomRight[0])/2.0)
        cY = int((topLeft[1] + bottomRight[1])/2.0)
        return cX, cY

    def draw_center(self, topLeft, bottomRight):
        cX,cY = self.compute_marker_center(topLeft, bottomRight)
        cv2.circle(self.frame, (cX,cY),4,(0,255,0),-1)
        

    def draw_midline(self):
        centerX = self.width/2.0
        topCenter = (int(centerX), 0)
        bottomCenter = (int(centerX), self.height)
        COLOR = (255, 0, 0)
        cv2.line(self.frame, topCenter, bottomCenter, COLOR, 5)
        

    def draw_texts(self, topLeft, markerID):
        #draw markerID on frame
        cv2.putText(self.frame, str(markerID),(topLeft[0],topLeft[1]-15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    def put_state_text(self, text):
        cv2.putText(self.frame, str(text), (20,30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
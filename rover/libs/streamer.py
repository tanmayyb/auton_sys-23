import cv2
from settings.pipeline import *
from settings.video import *

class streamer():
    def __init__(self):
        self.cap = self.start_stream()

    def start_stream(self):
        print("\n[INFO] starting gst pipeline with command:\n"+gst_in_command+"\n")
        cap = cv2.VideoCapture(gst_in_command, cv2.CAP_GSTREAMER)
        return cap

    def get_frame(self):
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, VIDEO_RESIZE_DIMS)

        return ret, frame

    def get_info(self):
        return VIDEO_RESIZE_DIMS, FOV

    def display_frames(self, frame):
        cv2.imshow("GST_Stream_for_Aruco",frame)

    def check_for_exit_keypresses(self):
        key = cv2.waitKey(1) & 0xFF #wait for a key press for 1ms and then and then continue with video 
                                    #0xFF AND waitkey(1) gives you waitkey(1)
        if key == ord("q"):
            return 0
        return 1

    def stop(self):
        self.cap.stop()

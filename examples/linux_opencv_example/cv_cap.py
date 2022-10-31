import cv2
from cv2 import CAP_GSTREAMER

# WORKING: cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink")

# Define the source as shared memory (shmsrc) and point to the socket. !
# Set the caps (raw (not encoded) frame video/x-raw, format as BGR or RGB (opencv format of grabbed cameras)) and define the properties of the camera !
# And sink the grabbed data to the appsink
# cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! appsink")

from pipeline import *

print(gst_command)

cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)

#if not cap.isOpened():
 #   print("Cannot capture from camera. Exiting.")
 #   quit()


while True:

    ret, frame = cap.read()

    if ret == False:
        #print("empty")
        pass
    else:
        cv2.imshow("GST_Stream",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

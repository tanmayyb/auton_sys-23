import cv2
from cv2 import CAP_GSTREAMER

# WORKING: cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink")

# Define the source as shared memory (shmsrc) and point to the socket. !
# Set the caps (raw (not encoded) frame video/x-raw, format as BGR or RGB (opencv format of grabbed cameras)) and define the properties of the camera !
# And sink the grabbed data to the appsink
# cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! appsink")

from pipeline import gst_command

## Update

#default working command
#gst-launch-1.0 -e -v udpsrc port=8080 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink

#gst_command = "udpsrc port=8080 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink"

#! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink
gst_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, clock-rate=90000, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"

#cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR, width=640, height=480, pixel-aspect-ratio=1/1, framerate=30/1 ! \
#     decodebin ! videoconvert ! appsink")
#

cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)

#if not cap.isOpened():
 #   print("Cannot capture from camera. Exiting.")
 #   quit()


while True:

    ret, frame = cap.read()

    if ret == False:
         print("empty")
    else:
        cv2.imshow("FrameREAD",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# gst-launch-1.0 v4l2src ! x264enc ! shmsink socket-path=/tmp/foo sync=true wait-for-connection=false shm-size=10000000

# gst-launch-1.0 shmsrc socket-path=/tmp/foo ! h264parse ! avdec_h264 ! videoconvert ! ximagesink

# gst-launch-1.0 shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! videoconvert ! ximagesink
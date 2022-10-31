## Update

#default working command
#gst-launch-1.0 -e -v udpsrc port=8080 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink

#gst_command = "udpsrc port=8080 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink"


'''
Linux
'''

#! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink
gst_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, clock-rate=90000, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"

#cap = cv2.VideoCapture("shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR, width=640, height=480, pixel-aspect-ratio=1/1, framerate=30/1 ! \
#     decodebin ! videoconvert ! appsink")
#



# gst-launch-1.0 v4l2src ! x264enc ! shmsink socket-path=/tmp/foo sync=true wait-for-connection=false shm-size=10000000

# gst-launch-1.0 shmsrc socket-path=/tmp/foo ! h264parse ! avdec_h264 ! videoconvert ! ximagesink

# gst-launch-1.0 shmsrc socket-path=/tmp/foo ! video/x-raw, format=BGR ,width=1920,height=1080,framerate=30/1 ! videoconvert ! ximagesink
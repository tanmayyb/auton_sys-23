#pipeline: lin_vrx_1.0
gst_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"

"""
PIPELINES
"""

"""win_vtx_1.0"""
#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.111:8080
#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.74:8080
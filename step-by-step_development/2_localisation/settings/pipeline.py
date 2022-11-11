#pipeline: lin_vrx_1.0
gst_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"

#pipeline
#gst-launch-1.0 -v ksvideosrc device-index=1 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.246:8080
from enum import Enum
class CamName(Enum):
    Gucc = "gucc"

"""
%%%%%%%%%%%%%%%%%%%%%
User Settings
%%%%%%%%%%%%%%%%%%%%%
"""
CAM = CamName.Gucc
STREAM_CVS2_OUT_TO_USER = True

"""
%%%%%%%%%%%%%%%%%%%%%
Pipeline TX/RX Logics 
%%%%%%%%%%%%%%%%%%%%%
"""
gst_in_command = None
gst_out_command = None

if CAM == CamName.Gucc:
    #pipeline for Gucc Cam: lin_vrx_1.0
    gst_in_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"
    print("Calibration check gstreamer command:\n", )
    if STREAM_CVS2_OUT_TO_USER == False:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081"
    else:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081,172.17.255.10:8081,172.17.255.9:8081"
        usr_rx_pipeline = None
        usr_rx_pipeline = "gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink"
        print("Enter this pipeline on <172.17.255.9/10:8081> to see the cvs2 output:\n", usr_rx_pipeline)


"""
PIPELINES
"""
"""win_vtx_1.0"""
#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.111:8080
#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.74:8080


#Gucc Cam

#Tx:
#gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080,172.17.255.10:8080
#Autovideo sink rx:
#gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
#gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
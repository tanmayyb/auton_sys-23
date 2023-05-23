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
SHOW_CALIBRATION_PIPELINE = True
"""
%%%%%%%%%%%%%%%%%%%%%
Pipeline TX/RX Logics 
%%%%%%%%%%%%%%%%%%%%%
"""
gst_in_command = None
gst_out_command = None


print("\nCam Chosen:", CAM)

if CAM == CamName.Gucc:
    #pipeline for Gucc Cam: lin_vrx_1.0    
    if SHOW_CALIBRATION_PIPELINE: 
        usr_tx_pipeline = "gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080,172.17.255.9:8080"
        cvs2_calibration_pipeline = "gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink"
    else: 
        usr_tx_pipeline = "gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080"        

    print("\nUSR TRIGGERED I/O PIPELINES:")
    print("INPUT CVS2 PIPELINE [USER INITIATED]:\n", usr_tx_pipeline )
    if SHOW_CALIBRATION_PIPELINE: print("CALIBRATION PIPELINE:\n", cvs2_calibration_pipeline)

    gst_in_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"
    
    if STREAM_CVS2_OUT_TO_USER == False:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081"
    else:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081,172.17.255.10:8081,172.17.255.9:8081"
        usr_rx_pipeline = "gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink"
        
        print("WATCH CVS2 OUTPUT [USER INITIATED]:\n", usr_rx_pipeline)

    print("\nCVS2'S I/O PIPELINE:")
    print("CVS2 SRC CMMND:\n", gst_in_command)
    print("CVS2 SINK CMMND:\n", gst_out_command)

        

"""
PIPELINES
"""


"""

calibrate/test camera stream
_____________________________

ssh into xav:
```
ssh xav@172.16.255.25
gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080,172.17.255.<ip>:8080
```

view your camera on ip for calibration
______________________________________

on base computer:
```
gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
```
"""


#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.111:8080
#gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=192.168.137.74:8080


#Gucc Cam

#Tx:
#gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080,172.17.255.10:8080
#Autovideo sink rx:
#gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
#gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
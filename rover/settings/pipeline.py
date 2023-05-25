from enum import Enum


gst_in_command = None
gst_out_command = None


"""
%%%%%%%%%%%%%%%%%%%%%
User Settings
%%%%%%%%%%%%%%%%%%%%%
"""

class CamName(Enum):
    Gucc = "gucc"
    Test_Webcam = "Tanmay's Personal Test Webcam"

CAM = CamName.Gucc
STREAM_CVS2_OUT_TO_USER = True
SHOW_CALIBRATION_PIPELINE = True
WATCH_CALIBRATION_IP_ADDRESSES = ',172.17.255.10:8080'
WATCH_CVS2_OUTPUT_IP_ADDRESSES = ',172.17.255.10:8081'


"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
PRINT INSTRUCTIONS AND CHOSEN OPTIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
def print_info():

    print("\nCam Chosen: ", CAM)
    print("STREAM_CVS2_OUT_TO_USER: ", STREAM_CVS2_OUT_TO_USER)
    print("SHOW_CALIBRATION_PIPELINE: ", SHOW_CALIBRATION_PIPELINE)
    print("WATCH_CVS2_OUTPUT_IP_ADDRESSES: ", WATCH_CVS2_OUTPUT_IP_ADDRESSES)


    print("\n\nUSR TRIGGERED I/O PIPELINES [USER INITIATED]:")
    print("INPUT TO CVS2 PIPELINE [USER INITIATED]:\n", usr_tx_pipeline )
    if SHOW_CALIBRATION_PIPELINE: print("\nUSR RX CALIBRATION PIPELINE [USER INITIATED]:\n", cvs2_calibration_pipeline)
    if STREAM_CVS2_OUT_TO_USER: print("\nUSR RX WATCH CVS2 OUTPUT [USER INITIATED]:\n", usr_rx_pipeline)


    print("\n\nCVS2'S I/O PIPELINES: [NOT USR INITIATED]")
    print("CVS2 SRC CMMND:\n", gst_in_command)
    print("\nCVS2 SINK CMMND:\n", gst_out_command)


"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
PIPELINE PROFILE FOR EACH CAM 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
if CAM == CamName.Gucc:
    usr_tx_pipeline = "gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080"
    if SHOW_CALIBRATION_PIPELINE:   usr_tx_pipeline = 'gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=127.0.0.0:8080'+str(WATCH_CALIBRATION_IP_ADDRESSES)
    
    cvs2_calibration_pipeline = "gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink"

    gst_in_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"
    
    if STREAM_CVS2_OUT_TO_USER == False:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081"
    else:
        gst_out_command = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081'+str(WATCH_CVS2_OUTPUT_IP_ADDRESSES)
        usr_rx_pipeline = "gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink"
        
    print_info()


if CAM == CamName.Test_Webcam:
    #pipeline for Gucc Cam: lin_vrx_1.0    
        
    usr_tx_pipeline = 'gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=127.0.0.0:8080'
    if SHOW_CALIBRATION_PIPELINE:   usr_tx_pipeline = 'gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=127.0.0.0:8080'+str(WATCH_CALIBRATION_IP_ADDRESSES)

    cvs2_calibration_pipeline = "gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink"

    gst_in_command = "udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"
    
    if STREAM_CVS2_OUT_TO_USER == False:
        gst_out_command = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081"
    else:
        gst_out_command = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! multiudpsink clients=127.0.0.1:8081'+str(WATCH_CVS2_OUTPUT_IP_ADDRESSES)
        usr_rx_pipeline = "gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink"
        
    print_info()

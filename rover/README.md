# Rover Systems


## Usage
Assuming following commands have been entered from your base station computer:

```
ssh xav@xav
cd github/auton_sys-23 && . utils/install/setup.bash
```
Run:
```
python3 rover/manager.py
python3 rover/rover.py

python3 rover/cvs2.py
python3 rover/sensors.py
python3 rover/teensy.py
```

## GST Pipelines for Cameras

The current camera in use for Auton ARUCO is called `"GUCC"`.

### Stream camera to CVS2

<b> "Gucc" </b>
```
TX: 
SYSTEM LOOPBACK(for CVS2) + BASESTATION(debugging):

gst-launch-1.0 -vvv v4l2src device=/dev/video0 ! 'image/jpeg, width=1280, height=720, framerate=60/1' ! jpegparse ! rtpjpegpay ! multiudpsink clients=127.0.0.1:8080,172.17.255.10:8080

RX:
AUTOVIDEOSINK:

gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=60/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink

CVS2:APPIN:

```
### Watch output stream (tbd)
```
gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
gst-launch-1.0 udpsrc port=8081 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
```

Windows Cam Streaming (tbd)
```
#win
gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=10.0.0.52:8080
#linux
gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=127.0.0.0:8080
gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=172.17.255.149:8080
gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=172.17.255.149:8080
```

## Useful debugging commands

Turn cvs2 ON/OFF
```
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: True"
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: False"    
```
Send searchwalk goal to action manager
```
ros2 topic pub /searchwalk rover_utils/msg/SearchWalk "{coords:{ x: 43.6587021, y: -79.3792810, z: 0.0}, search_radius: 10.0, search_pattern: 0, enable_cv: True, enable_oa: False, loop_searchwalk: False}"
```


Cameras:
```
v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext      -to know format of a cam's stream

```

ROS 2 Nodes:
```

```


## System Specific Parameters
These are in place because of the eccentricity of the system that we are using.
```
1.  rover/sensors.py/ln17: sudoPassword = 'xav'     (because xavier pass=xav)
2.  rover/libs/sender.py: self.UDP_IP = "172.16.10.1" (because teensy ip)
3.  rover/libs/sender.py: ln
```


### Stream camera to CVS2
```
gst-launch-1.0 -v ksvideosrc device-index=0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=172.17.255.149:8080
gst-launch-1.0 -v v4l2src device=/dev/video0 ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=172.17.255.149:8080
```
### Watch output stream
```
gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, media=video, payload=26, encoding-name=JPEG, framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink
gst-launch-1.0 udpsrc port=8080 ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink
```

#### Turn cvs2 ON/OFF
```
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: True"
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: False"    
```
#### Send searchwalk goal to action manager
```
ros2 topic pub /searchwalk rover_utils/msg/SearchWalk "{coords:{ x: 43.6587021, y: -79.3792810, z: 0.0}, search_radius: 10.0, search_pattern: 0, enable_cv: True, enable_oa: False, loop_searchwalk: False}"
```
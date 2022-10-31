
Glossary:
```
<index> = device index e.g. = 0
<ip> = client ip e.g. = 10.0.0.52
<port> = client ip's port e.g. = 8080
```


## Windows
### Windows as VTX

#### simple local view
Pipeline 0.0
```
gst-launch-1.0 -v ksvideosrc device-index=<index> ! video/x-raw,width=640, height=480,framerate=30/1 ! videoconvert ! autovideosink
```

#### simple multi-udp send
pipeline: win_vtx_1.0
```
gst-launch-1.0 -v ksvideosrc device-index=<index> ! "image/jpeg,width=640, height=480,framerate=30/1" ! rtpjpegpay ! multiudpsink clients=<ip>:<port>,<ip>:<port>
```
### Windows as VRX

### view udp natively
pipeline: win_vrx_1.0
```
gst-launch-1.0 -e -v udpsrc port=8080 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink 
```


## Linux

### Linux as VTX




### Linux as VRX

#### View udp natively
pipeline: lin_vrx_1.0
```
gst-launch-1.0 -e -v  udpsrc port=8080 ! "application/x-rtp, encoding-name=JPEG,payload=26" ! rtpjpegdepay ! jpegparse ! jpegdec ! videoconvert ! autovideosink
```
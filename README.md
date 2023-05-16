
```
This branch does not have a stable CVS2. The CVS2 has trouble Approaching targets, filtering false positives, and getting cancelled by the client.
The miniWalk and MultiWalk work fine.
```

<p align="center"> 
  <img src="https://github-readme-quotes.herokuapp.com/quote?quotesUrl=https://github.com/teamr3/public-quotes/blob/master/auton_sys-23/99threads.json">
</p>

# auton_sys-23

Auton Mission Repo for URC 2023


## Contributors:

| Name             | Email                    | Role                  |
| ---------------- | ------------------------ | --------------------- |
| Tanmay Bishnoi   | tbishnoi@torontomu.ca    | Lead Engineer         |
| Ryan             | 	r1le@torontomu.ca       | Support Engineer         |
| Eleanor          | email@ryerson.ca         | Support Engineer         |


## Capabilities
Listed below are the features/capabilities of the current system:
1.  Miniwalk
2.  Multiwalk (Search pattern)
3.  ARUCO detection, centering, and approach

## About Usage:

The software has two indepedent but connected components: `base` and `rover` systems. <b> The instructions to run both of them  sit in their respective folders.</b>
The `utils/install` contains a `setup.bash` to enable custom ROS 2 interfaces for this repo. Any terminal running our nodes will need to enter the following command on startup.

```
. utils/install/setup.bash
```
(written here w.r.t root of the directory)


## Devices Setup




## Networking
Current Networking Setup
```
tanmay's winPC
ip:			172.17.255.9

tanmay's ROS-VM 
ip:			172.17.255.10

Xavier
ip: 			172.16.255.25
default dns: 	172.16.255.1

subnet on all devices
255.240.0.0
```


## Installations/Dependencies
```
<add ros2 installs>
<add cv2 install>
<add gstreamer install>
<add vnpy installation>

sudo apt-get install python3-pil python3-pil.imagetk
pip install tkintermapview
pip install pygame
pip install tkinter
```

## Prototyping Documentation
UI:</br>
https://www.figma.com/file/ip6mJr0MV8HCT5906CQ1Ye/Auton-ROS-GUI?node-id=0%3A1


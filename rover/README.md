
#### Turn cvs2 ON/OFF
```
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: True"
ros2 topic pub /set_cvs2_state std_msgs/Bool "data: False"    
```
#### Send searchwalk goal to action manager
```
ros2 topic pub /searchwalk rover_utils/msg/SearchWalk "{coords:{ x: 43.6587021, y: -79.3792810, z: 0.0}, search_radius: 10.0, search_pattern: 0, enable_cv: True, enable_oa: False, loop_searchwalk: False}"

```
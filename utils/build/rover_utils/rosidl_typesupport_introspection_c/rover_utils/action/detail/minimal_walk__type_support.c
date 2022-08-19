// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
#include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rover_utils/action/detail/minimal_walk__functions.h"
#include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `coords`
#include "geometry_msgs/msg/point.h"
// Member `coords`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_Goal__init(message_memory);
}

void MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_Goal__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_member_array[3] = {
  {
    "coords",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Goal, coords),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "use_guidance",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Goal, use_guidance),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "signal_and_wait",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Goal, signal_and_wait),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_Goal",  // message name
  3,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_Goal),
  MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_member_array,  // message members
  MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_type_support_handle = {
  0,
  &MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Goal)() {
  MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_Goal__rosidl_typesupport_introspection_c__MinimalWalk_Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_Result__init(message_memory);
}

void MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_Result__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_member_array[1] = {
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Result, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_Result",  // message name
  1,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_Result),
  MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_member_array,  // message members
  MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_type_support_handle = {
  0,
  &MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Result)() {
  if (!MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_Result__rosidl_typesupport_introspection_c__MinimalWalk_Result_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_Feedback__init(message_memory);
}

void MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_Feedback__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_member_array[2] = {
  {
    "d2t",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Feedback, d2t),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "he",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_Feedback, he),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_Feedback",  // message name
  2,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_Feedback),
  MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_member_array,  // message members
  MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_type_support_handle = {
  0,
  &MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Feedback)() {
  if (!MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_Feedback__rosidl_typesupport_introspection_c__MinimalWalk_Feedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `goal`
#include "rover_utils/action/minimal_walk.h"
// Member `goal`
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_SendGoal_Request__init(message_memory);
}

void MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_SendGoal_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_SendGoal_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_SendGoal_Request, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_SendGoal_Request",  // message name
  2,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_SendGoal_Request),
  MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_member_array,  // message members
  MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_type_support_handle = {
  0,
  &MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Request)() {
  MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Goal)();
  if (!MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_SendGoal_Request__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_SendGoal_Response__init(message_memory);
}

void MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_SendGoal_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_member_array[2] = {
  {
    "accepted",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_SendGoal_Response, accepted),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_SendGoal_Response, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_SendGoal_Response",  // message name
  2,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_SendGoal_Response),
  MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_member_array,  // message members
  MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_type_support_handle = {
  0,
  &MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Response)() {
  MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_SendGoal_Response__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_members = {
  "rover_utils__action",  // service namespace
  "MinimalWalk_SendGoal",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Request_message_type_support_handle,
  NULL  // response message
  // rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_Response_message_type_support_handle
};

static rosidl_service_type_support_t rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_type_support_handle = {
  0,
  &rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal)() {
  if (!rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_type_support_handle.typesupport_identifier) {
    rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Response)()->data;
  }

  return &rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_SendGoal_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_GetResult_Request__init(message_memory);
}

void MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_GetResult_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_member_array[1] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_GetResult_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_GetResult_Request",  // message name
  1,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_GetResult_Request),
  MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_member_array,  // message members
  MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_type_support_handle = {
  0,
  &MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Request)() {
  MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  if (!MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_GetResult_Request__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `result`
// already included above
// #include "rover_utils/action/minimal_walk.h"
// Member `result`
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_GetResult_Response__init(message_memory);
}

void MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_GetResult_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_GetResult_Response, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_GetResult_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_GetResult_Response",  // message name
  2,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_GetResult_Response),
  MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_member_array,  // message members
  MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_type_support_handle = {
  0,
  &MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Response)() {
  MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Result)();
  if (!MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_GetResult_Response__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_members = {
  "rover_utils__action",  // service namespace
  "MinimalWalk_GetResult",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Request_message_type_support_handle,
  NULL  // response message
  // rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_Response_message_type_support_handle
};

static rosidl_service_type_support_t rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_type_support_handle = {
  0,
  &rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult)() {
  if (!rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_type_support_handle.typesupport_identifier) {
    rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Response)()->data;
  }

  return &rover_utils__action__detail__minimal_walk__rosidl_typesupport_introspection_c__MinimalWalk_GetResult_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `feedback`
// already included above
// #include "rover_utils/action/minimal_walk.h"
// Member `feedback`
// already included above
// #include "rover_utils/action/detail/minimal_walk__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__action__MinimalWalk_FeedbackMessage__init(message_memory);
}

void MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_fini_function(void * message_memory)
{
  rover_utils__action__MinimalWalk_FeedbackMessage__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_FeedbackMessage, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "feedback",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__action__MinimalWalk_FeedbackMessage, feedback),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_members = {
  "rover_utils__action",  // message namespace
  "MinimalWalk_FeedbackMessage",  // message name
  2,  // number of fields
  sizeof(rover_utils__action__MinimalWalk_FeedbackMessage),
  MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_member_array,  // message members
  MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_type_support_handle = {
  0,
  &MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_FeedbackMessage)() {
  MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Feedback)();
  if (!MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_type_support_handle.typesupport_identifier) {
    MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MinimalWalk_FeedbackMessage__rosidl_typesupport_introspection_c__MinimalWalk_FeedbackMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

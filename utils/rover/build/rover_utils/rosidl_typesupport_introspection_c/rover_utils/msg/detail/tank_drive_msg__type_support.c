// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "rover_utils/msg/detail/tank_drive_msg__rosidl_typesupport_introspection_c.h"
#include "rover_utils/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "rover_utils/msg/detail/tank_drive_msg__functions.h"
#include "rover_utils/msg/detail/tank_drive_msg__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  rover_utils__msg__TankDriveMsg__init(message_memory);
}

void TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_fini_function(void * message_memory)
{
  rover_utils__msg__TankDriveMsg__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_member_array[2] = {
  {
    "lpwm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__msg__TankDriveMsg, lpwm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rpwm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils__msg__TankDriveMsg, rpwm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_members = {
  "rover_utils__msg",  // message namespace
  "TankDriveMsg",  // message name
  2,  // number of fields
  sizeof(rover_utils__msg__TankDriveMsg),
  TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_member_array,  // message members
  TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_type_support_handle = {
  0,
  &TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, msg, TankDriveMsg)() {
  if (!TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_type_support_handle.typesupport_identifier) {
    TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TankDriveMsg__rosidl_typesupport_introspection_c__TankDriveMsg_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

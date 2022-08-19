// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "rover_utils/msg/detail/tank_drive_msg__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace rover_utils
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TankDriveMsg_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) rover_utils::msg::TankDriveMsg(_init);
}

void TankDriveMsg_fini_function(void * message_memory)
{
  auto typed_message = static_cast<rover_utils::msg::TankDriveMsg *>(message_memory);
  typed_message->~TankDriveMsg();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TankDriveMsg_message_member_array[2] = {
  {
    "lpwm",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils::msg::TankDriveMsg, lpwm),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "rpwm",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(rover_utils::msg::TankDriveMsg, rpwm),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TankDriveMsg_message_members = {
  "rover_utils::msg",  // message namespace
  "TankDriveMsg",  // message name
  2,  // number of fields
  sizeof(rover_utils::msg::TankDriveMsg),
  TankDriveMsg_message_member_array,  // message members
  TankDriveMsg_init_function,  // function to initialize message memory (memory has to be allocated)
  TankDriveMsg_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TankDriveMsg_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TankDriveMsg_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace rover_utils


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<rover_utils::msg::TankDriveMsg>()
{
  return &::rover_utils::msg::rosidl_typesupport_introspection_cpp::TankDriveMsg_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, rover_utils, msg, TankDriveMsg)() {
  return &::rover_utils::msg::rosidl_typesupport_introspection_cpp::TankDriveMsg_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

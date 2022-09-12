// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice
#include "rover_utils/msg/detail/tank_drive_msg__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rover_utils/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "rover_utils/msg/detail/tank_drive_msg__struct.h"
#include "rover_utils/msg/detail/tank_drive_msg__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TankDriveMsg__ros_msg_type = rover_utils__msg__TankDriveMsg;

static bool _TankDriveMsg__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TankDriveMsg__ros_msg_type * ros_message = static_cast<const _TankDriveMsg__ros_msg_type *>(untyped_ros_message);
  // Field name: lpwm
  {
    cdr << ros_message->lpwm;
  }

  // Field name: rpwm
  {
    cdr << ros_message->rpwm;
  }

  return true;
}

static bool _TankDriveMsg__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TankDriveMsg__ros_msg_type * ros_message = static_cast<_TankDriveMsg__ros_msg_type *>(untyped_ros_message);
  // Field name: lpwm
  {
    cdr >> ros_message->lpwm;
  }

  // Field name: rpwm
  {
    cdr >> ros_message->rpwm;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rover_utils
size_t get_serialized_size_rover_utils__msg__TankDriveMsg(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TankDriveMsg__ros_msg_type * ros_message = static_cast<const _TankDriveMsg__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name lpwm
  {
    size_t item_size = sizeof(ros_message->lpwm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rpwm
  {
    size_t item_size = sizeof(ros_message->rpwm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TankDriveMsg__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_rover_utils__msg__TankDriveMsg(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_rover_utils
size_t max_serialized_size_rover_utils__msg__TankDriveMsg(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: lpwm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rpwm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _TankDriveMsg__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_rover_utils__msg__TankDriveMsg(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_TankDriveMsg = {
  "rover_utils::msg",
  "TankDriveMsg",
  _TankDriveMsg__cdr_serialize,
  _TankDriveMsg__cdr_deserialize,
  _TankDriveMsg__get_serialized_size,
  _TankDriveMsg__max_serialized_size
};

static rosidl_message_type_support_t _TankDriveMsg__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TankDriveMsg,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, msg, TankDriveMsg)() {
  return &_TankDriveMsg__type_support;
}

#if defined(__cplusplus)
}
#endif

// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice
#include "rover_utils/msg/detail/tank_drive_msg__rosidl_typesupport_fastrtps_cpp.hpp"
#include "rover_utils/msg/detail/tank_drive_msg__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace rover_utils
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rover_utils
cdr_serialize(
  const rover_utils::msg::TankDriveMsg & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: lpwm
  cdr << ros_message.lpwm;
  // Member: rpwm
  cdr << ros_message.rpwm;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rover_utils
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  rover_utils::msg::TankDriveMsg & ros_message)
{
  // Member: lpwm
  cdr >> ros_message.lpwm;

  // Member: rpwm
  cdr >> ros_message.rpwm;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rover_utils
get_serialized_size(
  const rover_utils::msg::TankDriveMsg & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: lpwm
  {
    size_t item_size = sizeof(ros_message.lpwm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: rpwm
  {
    size_t item_size = sizeof(ros_message.rpwm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_rover_utils
max_serialized_size_TankDriveMsg(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: lpwm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: rpwm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _TankDriveMsg__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const rover_utils::msg::TankDriveMsg *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TankDriveMsg__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<rover_utils::msg::TankDriveMsg *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TankDriveMsg__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const rover_utils::msg::TankDriveMsg *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TankDriveMsg__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_TankDriveMsg(full_bounded, 0);
}

static message_type_support_callbacks_t _TankDriveMsg__callbacks = {
  "rover_utils::msg",
  "TankDriveMsg",
  _TankDriveMsg__cdr_serialize,
  _TankDriveMsg__cdr_deserialize,
  _TankDriveMsg__get_serialized_size,
  _TankDriveMsg__max_serialized_size
};

static rosidl_message_type_support_t _TankDriveMsg__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TankDriveMsg__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace rover_utils

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_rover_utils
const rosidl_message_type_support_t *
get_message_type_support_handle<rover_utils::msg::TankDriveMsg>()
{
  return &rover_utils::msg::typesupport_fastrtps_cpp::_TankDriveMsg__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, rover_utils, msg, TankDriveMsg)() {
  return &rover_utils::msg::typesupport_fastrtps_cpp::_TankDriveMsg__handle;
}

#ifdef __cplusplus
}
#endif

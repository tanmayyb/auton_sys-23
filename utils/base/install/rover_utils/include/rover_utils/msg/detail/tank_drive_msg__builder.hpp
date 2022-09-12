// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__BUILDER_HPP_
#define ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__BUILDER_HPP_

#include "rover_utils/msg/detail/tank_drive_msg__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace rover_utils
{

namespace msg
{

namespace builder
{

class Init_TankDriveMsg_rpwm
{
public:
  explicit Init_TankDriveMsg_rpwm(::rover_utils::msg::TankDriveMsg & msg)
  : msg_(msg)
  {}
  ::rover_utils::msg::TankDriveMsg rpwm(::rover_utils::msg::TankDriveMsg::_rpwm_type arg)
  {
    msg_.rpwm = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::msg::TankDriveMsg msg_;
};

class Init_TankDriveMsg_lpwm
{
public:
  Init_TankDriveMsg_lpwm()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TankDriveMsg_rpwm lpwm(::rover_utils::msg::TankDriveMsg::_lpwm_type arg)
  {
    msg_.lpwm = std::move(arg);
    return Init_TankDriveMsg_rpwm(msg_);
  }

private:
  ::rover_utils::msg::TankDriveMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::msg::TankDriveMsg>()
{
  return rover_utils::msg::builder::Init_TankDriveMsg_lpwm();
}

}  // namespace rover_utils

#endif  // ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__BUILDER_HPP_

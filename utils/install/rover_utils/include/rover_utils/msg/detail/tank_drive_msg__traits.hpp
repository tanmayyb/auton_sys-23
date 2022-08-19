// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__TRAITS_HPP_
#define ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__TRAITS_HPP_

#include "rover_utils/msg/detail/tank_drive_msg__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::msg::TankDriveMsg>()
{
  return "rover_utils::msg::TankDriveMsg";
}

template<>
inline const char * name<rover_utils::msg::TankDriveMsg>()
{
  return "rover_utils/msg/TankDriveMsg";
}

template<>
struct has_fixed_size<rover_utils::msg::TankDriveMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rover_utils::msg::TankDriveMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rover_utils::msg::TankDriveMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__TRAITS_HPP_

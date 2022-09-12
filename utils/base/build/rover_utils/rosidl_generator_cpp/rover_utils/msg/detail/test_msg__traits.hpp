// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rover_utils:msg/TestMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TEST_MSG__TRAITS_HPP_
#define ROVER_UTILS__MSG__DETAIL__TEST_MSG__TRAITS_HPP_

#include "rover_utils/msg/detail/test_msg__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'point'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::msg::TestMsg>()
{
  return "rover_utils::msg::TestMsg";
}

template<>
inline const char * name<rover_utils::msg::TestMsg>()
{
  return "rover_utils/msg/TestMsg";
}

template<>
struct has_fixed_size<rover_utils::msg::TestMsg>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<rover_utils::msg::TestMsg>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<rover_utils::msg::TestMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROVER_UTILS__MSG__DETAIL__TEST_MSG__TRAITS_HPP_

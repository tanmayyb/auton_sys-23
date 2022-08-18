// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rover_utils:msg/TestMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TEST_MSG__BUILDER_HPP_
#define ROVER_UTILS__MSG__DETAIL__TEST_MSG__BUILDER_HPP_

#include "rover_utils/msg/detail/test_msg__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace rover_utils
{

namespace msg
{

namespace builder
{

class Init_TestMsg_my_float
{
public:
  explicit Init_TestMsg_my_float(::rover_utils::msg::TestMsg & msg)
  : msg_(msg)
  {}
  ::rover_utils::msg::TestMsg my_float(::rover_utils::msg::TestMsg::_my_float_type arg)
  {
    msg_.my_float = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::msg::TestMsg msg_;
};

class Init_TestMsg_point
{
public:
  Init_TestMsg_point()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TestMsg_my_float point(::rover_utils::msg::TestMsg::_point_type arg)
  {
    msg_.point = std::move(arg);
    return Init_TestMsg_my_float(msg_);
  }

private:
  ::rover_utils::msg::TestMsg msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::msg::TestMsg>()
{
  return rover_utils::msg::builder::Init_TestMsg_point();
}

}  // namespace rover_utils

#endif  // ROVER_UTILS__MSG__DETAIL__TEST_MSG__BUILDER_HPP_

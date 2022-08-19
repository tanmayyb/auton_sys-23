// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from rover_utils:msg/TestMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_HPP_
#define ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'point'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__rover_utils__msg__TestMsg __attribute__((deprecated))
#else
# define DEPRECATED__rover_utils__msg__TestMsg __declspec(deprecated)
#endif

namespace rover_utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TestMsg_
{
  using Type = TestMsg_<ContainerAllocator>;

  explicit TestMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : point(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->my_float = 0.0f;
    }
  }

  explicit TestMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : point(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->my_float = 0.0f;
    }
  }

  // field types and members
  using _point_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _point_type point;
  using _my_float_type =
    float;
  _my_float_type my_float;

  // setters for named parameter idiom
  Type & set__point(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->point = _arg;
    return *this;
  }
  Type & set__my_float(
    const float & _arg)
  {
    this->my_float = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    rover_utils::msg::TestMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const rover_utils::msg::TestMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<rover_utils::msg::TestMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<rover_utils::msg::TestMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      rover_utils::msg::TestMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<rover_utils::msg::TestMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      rover_utils::msg::TestMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<rover_utils::msg::TestMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<rover_utils::msg::TestMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<rover_utils::msg::TestMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__rover_utils__msg__TestMsg
    std::shared_ptr<rover_utils::msg::TestMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__rover_utils__msg__TestMsg
    std::shared_ptr<rover_utils::msg::TestMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TestMsg_ & other) const
  {
    if (this->point != other.point) {
      return false;
    }
    if (this->my_float != other.my_float) {
      return false;
    }
    return true;
  }
  bool operator!=(const TestMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TestMsg_

// alias to use template instance with default allocator
using TestMsg =
  rover_utils::msg::TestMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace rover_utils

#endif  // ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_HPP_

// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__STRUCT_HPP_
#define ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__rover_utils__msg__TankDriveMsg __attribute__((deprecated))
#else
# define DEPRECATED__rover_utils__msg__TankDriveMsg __declspec(deprecated)
#endif

namespace rover_utils
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TankDriveMsg_
{
  using Type = TankDriveMsg_<ContainerAllocator>;

  explicit TankDriveMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lpwm = 0l;
      this->rpwm = 0l;
    }
  }

  explicit TankDriveMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lpwm = 0l;
      this->rpwm = 0l;
    }
  }

  // field types and members
  using _lpwm_type =
    int32_t;
  _lpwm_type lpwm;
  using _rpwm_type =
    int32_t;
  _rpwm_type rpwm;

  // setters for named parameter idiom
  Type & set__lpwm(
    const int32_t & _arg)
  {
    this->lpwm = _arg;
    return *this;
  }
  Type & set__rpwm(
    const int32_t & _arg)
  {
    this->rpwm = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    rover_utils::msg::TankDriveMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const rover_utils::msg::TankDriveMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      rover_utils::msg::TankDriveMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      rover_utils::msg::TankDriveMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__rover_utils__msg__TankDriveMsg
    std::shared_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__rover_utils__msg__TankDriveMsg
    std::shared_ptr<rover_utils::msg::TankDriveMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TankDriveMsg_ & other) const
  {
    if (this->lpwm != other.lpwm) {
      return false;
    }
    if (this->rpwm != other.rpwm) {
      return false;
    }
    return true;
  }
  bool operator!=(const TankDriveMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TankDriveMsg_

// alias to use template instance with default allocator
using TankDriveMsg =
  rover_utils::msg::TankDriveMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace rover_utils

#endif  // ROVER_UTILS__MSG__DETAIL__TANK_DRIVE_MSG__STRUCT_HPP_

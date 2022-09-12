// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rover_utils:msg/TestMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_H_
#define ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'point'
#include "geometry_msgs/msg/detail/point__struct.h"

// Struct defined in msg/TestMsg in the package rover_utils.
typedef struct rover_utils__msg__TestMsg
{
  geometry_msgs__msg__Point point;
  float my_float;
} rover_utils__msg__TestMsg;

// Struct for a sequence of rover_utils__msg__TestMsg.
typedef struct rover_utils__msg__TestMsg__Sequence
{
  rover_utils__msg__TestMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__msg__TestMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROVER_UTILS__MSG__DETAIL__TEST_MSG__STRUCT_H_

// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rover_utils:msg/TankDriveMsg.idl
// generated code does not contain a copyright notice
#include "rover_utils/msg/detail/tank_drive_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
rover_utils__msg__TankDriveMsg__init(rover_utils__msg__TankDriveMsg * msg)
{
  if (!msg) {
    return false;
  }
  // lpwm
  // rpwm
  return true;
}

void
rover_utils__msg__TankDriveMsg__fini(rover_utils__msg__TankDriveMsg * msg)
{
  if (!msg) {
    return;
  }
  // lpwm
  // rpwm
}

rover_utils__msg__TankDriveMsg *
rover_utils__msg__TankDriveMsg__create()
{
  rover_utils__msg__TankDriveMsg * msg = (rover_utils__msg__TankDriveMsg *)malloc(sizeof(rover_utils__msg__TankDriveMsg));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__msg__TankDriveMsg));
  bool success = rover_utils__msg__TankDriveMsg__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__msg__TankDriveMsg__destroy(rover_utils__msg__TankDriveMsg * msg)
{
  if (msg) {
    rover_utils__msg__TankDriveMsg__fini(msg);
  }
  free(msg);
}


bool
rover_utils__msg__TankDriveMsg__Sequence__init(rover_utils__msg__TankDriveMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__msg__TankDriveMsg * data = NULL;
  if (size) {
    data = (rover_utils__msg__TankDriveMsg *)calloc(size, sizeof(rover_utils__msg__TankDriveMsg));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__msg__TankDriveMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__msg__TankDriveMsg__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
rover_utils__msg__TankDriveMsg__Sequence__fini(rover_utils__msg__TankDriveMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__msg__TankDriveMsg__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

rover_utils__msg__TankDriveMsg__Sequence *
rover_utils__msg__TankDriveMsg__Sequence__create(size_t size)
{
  rover_utils__msg__TankDriveMsg__Sequence * array = (rover_utils__msg__TankDriveMsg__Sequence *)malloc(sizeof(rover_utils__msg__TankDriveMsg__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__msg__TankDriveMsg__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__msg__TankDriveMsg__Sequence__destroy(rover_utils__msg__TankDriveMsg__Sequence * array)
{
  if (array) {
    rover_utils__msg__TankDriveMsg__Sequence__fini(array);
  }
  free(array);
}

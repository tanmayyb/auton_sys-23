// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from rover_utils:msg/TestMsg.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__MSG__DETAIL__TEST_MSG__FUNCTIONS_H_
#define ROVER_UTILS__MSG__DETAIL__TEST_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "rover_utils/msg/rosidl_generator_c__visibility_control.h"

#include "rover_utils/msg/detail/test_msg__struct.h"

/// Initialize msg/TestMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * rover_utils__msg__TestMsg
 * )) before or use
 * rover_utils__msg__TestMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
bool
rover_utils__msg__TestMsg__init(rover_utils__msg__TestMsg * msg);

/// Finalize msg/TestMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
void
rover_utils__msg__TestMsg__fini(rover_utils__msg__TestMsg * msg);

/// Create msg/TestMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * rover_utils__msg__TestMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
rover_utils__msg__TestMsg *
rover_utils__msg__TestMsg__create();

/// Destroy msg/TestMsg message.
/**
 * It calls
 * rover_utils__msg__TestMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
void
rover_utils__msg__TestMsg__destroy(rover_utils__msg__TestMsg * msg);


/// Initialize array of msg/TestMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * rover_utils__msg__TestMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
bool
rover_utils__msg__TestMsg__Sequence__init(rover_utils__msg__TestMsg__Sequence * array, size_t size);

/// Finalize array of msg/TestMsg messages.
/**
 * It calls
 * rover_utils__msg__TestMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
void
rover_utils__msg__TestMsg__Sequence__fini(rover_utils__msg__TestMsg__Sequence * array);

/// Create array of msg/TestMsg messages.
/**
 * It allocates the memory for the array and calls
 * rover_utils__msg__TestMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
rover_utils__msg__TestMsg__Sequence *
rover_utils__msg__TestMsg__Sequence__create(size_t size);

/// Destroy array of msg/TestMsg messages.
/**
 * It calls
 * rover_utils__msg__TestMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_rover_utils
void
rover_utils__msg__TestMsg__Sequence__destroy(rover_utils__msg__TestMsg__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // ROVER_UTILS__MSG__DETAIL__TEST_MSG__FUNCTIONS_H_

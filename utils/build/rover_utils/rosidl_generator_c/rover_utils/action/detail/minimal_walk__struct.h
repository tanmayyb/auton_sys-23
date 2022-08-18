// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__STRUCT_H_
#define ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_Goal
{
  int32_t goal_var;
} rover_utils__action__MinimalWalk_Goal;

// Struct for a sequence of rover_utils__action__MinimalWalk_Goal.
typedef struct rover_utils__action__MinimalWalk_Goal__Sequence
{
  rover_utils__action__MinimalWalk_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_Goal__Sequence;


// Constants defined in the message

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_Result
{
  int32_t result;
} rover_utils__action__MinimalWalk_Result;

// Struct for a sequence of rover_utils__action__MinimalWalk_Result.
typedef struct rover_utils__action__MinimalWalk_Result__Sequence
{
  rover_utils__action__MinimalWalk_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_Result__Sequence;


// Constants defined in the message

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_Feedback
{
  int32_t feedback;
} rover_utils__action__MinimalWalk_Feedback;

// Struct for a sequence of rover_utils__action__MinimalWalk_Feedback.
typedef struct rover_utils__action__MinimalWalk_Feedback__Sequence
{
  rover_utils__action__MinimalWalk_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "rover_utils/action/detail/minimal_walk__struct.h"

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  rover_utils__action__MinimalWalk_Goal goal;
} rover_utils__action__MinimalWalk_SendGoal_Request;

// Struct for a sequence of rover_utils__action__MinimalWalk_SendGoal_Request.
typedef struct rover_utils__action__MinimalWalk_SendGoal_Request__Sequence
{
  rover_utils__action__MinimalWalk_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} rover_utils__action__MinimalWalk_SendGoal_Response;

// Struct for a sequence of rover_utils__action__MinimalWalk_SendGoal_Response.
typedef struct rover_utils__action__MinimalWalk_SendGoal_Response__Sequence
{
  rover_utils__action__MinimalWalk_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} rover_utils__action__MinimalWalk_GetResult_Request;

// Struct for a sequence of rover_utils__action__MinimalWalk_GetResult_Request.
typedef struct rover_utils__action__MinimalWalk_GetResult_Request__Sequence
{
  rover_utils__action__MinimalWalk_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_GetResult_Response
{
  int8_t status;
  rover_utils__action__MinimalWalk_Result result;
} rover_utils__action__MinimalWalk_GetResult_Response;

// Struct for a sequence of rover_utils__action__MinimalWalk_GetResult_Response.
typedef struct rover_utils__action__MinimalWalk_GetResult_Response__Sequence
{
  rover_utils__action__MinimalWalk_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"

// Struct defined in action/MinimalWalk in the package rover_utils.
typedef struct rover_utils__action__MinimalWalk_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  rover_utils__action__MinimalWalk_Feedback feedback;
} rover_utils__action__MinimalWalk_FeedbackMessage;

// Struct for a sequence of rover_utils__action__MinimalWalk_FeedbackMessage.
typedef struct rover_utils__action__MinimalWalk_FeedbackMessage__Sequence
{
  rover_utils__action__MinimalWalk_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} rover_utils__action__MinimalWalk_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__STRUCT_H_

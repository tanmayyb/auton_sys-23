// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice
#include "rover_utils/action/detail/minimal_walk__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
rover_utils__action__MinimalWalk_Goal__init(rover_utils__action__MinimalWalk_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // goal_var
  return true;
}

void
rover_utils__action__MinimalWalk_Goal__fini(rover_utils__action__MinimalWalk_Goal * msg)
{
  if (!msg) {
    return;
  }
  // goal_var
}

rover_utils__action__MinimalWalk_Goal *
rover_utils__action__MinimalWalk_Goal__create()
{
  rover_utils__action__MinimalWalk_Goal * msg = (rover_utils__action__MinimalWalk_Goal *)malloc(sizeof(rover_utils__action__MinimalWalk_Goal));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_Goal));
  bool success = rover_utils__action__MinimalWalk_Goal__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_Goal__destroy(rover_utils__action__MinimalWalk_Goal * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_Goal__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_Goal__Sequence__init(rover_utils__action__MinimalWalk_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_Goal * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_Goal *)calloc(size, sizeof(rover_utils__action__MinimalWalk_Goal));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_Goal__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_Goal__Sequence__fini(rover_utils__action__MinimalWalk_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_Goal__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_Goal__Sequence *
rover_utils__action__MinimalWalk_Goal__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_Goal__Sequence * array = (rover_utils__action__MinimalWalk_Goal__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_Goal__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_Goal__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_Goal__Sequence__destroy(rover_utils__action__MinimalWalk_Goal__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_Goal__Sequence__fini(array);
  }
  free(array);
}


bool
rover_utils__action__MinimalWalk_Result__init(rover_utils__action__MinimalWalk_Result * msg)
{
  if (!msg) {
    return false;
  }
  // result
  return true;
}

void
rover_utils__action__MinimalWalk_Result__fini(rover_utils__action__MinimalWalk_Result * msg)
{
  if (!msg) {
    return;
  }
  // result
}

rover_utils__action__MinimalWalk_Result *
rover_utils__action__MinimalWalk_Result__create()
{
  rover_utils__action__MinimalWalk_Result * msg = (rover_utils__action__MinimalWalk_Result *)malloc(sizeof(rover_utils__action__MinimalWalk_Result));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_Result));
  bool success = rover_utils__action__MinimalWalk_Result__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_Result__destroy(rover_utils__action__MinimalWalk_Result * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_Result__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_Result__Sequence__init(rover_utils__action__MinimalWalk_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_Result * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_Result *)calloc(size, sizeof(rover_utils__action__MinimalWalk_Result));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_Result__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_Result__Sequence__fini(rover_utils__action__MinimalWalk_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_Result__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_Result__Sequence *
rover_utils__action__MinimalWalk_Result__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_Result__Sequence * array = (rover_utils__action__MinimalWalk_Result__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_Result__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_Result__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_Result__Sequence__destroy(rover_utils__action__MinimalWalk_Result__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_Result__Sequence__fini(array);
  }
  free(array);
}


bool
rover_utils__action__MinimalWalk_Feedback__init(rover_utils__action__MinimalWalk_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // feedback
  return true;
}

void
rover_utils__action__MinimalWalk_Feedback__fini(rover_utils__action__MinimalWalk_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // feedback
}

rover_utils__action__MinimalWalk_Feedback *
rover_utils__action__MinimalWalk_Feedback__create()
{
  rover_utils__action__MinimalWalk_Feedback * msg = (rover_utils__action__MinimalWalk_Feedback *)malloc(sizeof(rover_utils__action__MinimalWalk_Feedback));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_Feedback));
  bool success = rover_utils__action__MinimalWalk_Feedback__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_Feedback__destroy(rover_utils__action__MinimalWalk_Feedback * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_Feedback__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_Feedback__Sequence__init(rover_utils__action__MinimalWalk_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_Feedback * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_Feedback *)calloc(size, sizeof(rover_utils__action__MinimalWalk_Feedback));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_Feedback__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_Feedback__Sequence__fini(rover_utils__action__MinimalWalk_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_Feedback__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_Feedback__Sequence *
rover_utils__action__MinimalWalk_Feedback__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_Feedback__Sequence * array = (rover_utils__action__MinimalWalk_Feedback__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_Feedback__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_Feedback__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_Feedback__Sequence__destroy(rover_utils__action__MinimalWalk_Feedback__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_Feedback__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"

bool
rover_utils__action__MinimalWalk_SendGoal_Request__init(rover_utils__action__MinimalWalk_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    rover_utils__action__MinimalWalk_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!rover_utils__action__MinimalWalk_Goal__init(&msg->goal)) {
    rover_utils__action__MinimalWalk_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
rover_utils__action__MinimalWalk_SendGoal_Request__fini(rover_utils__action__MinimalWalk_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  rover_utils__action__MinimalWalk_Goal__fini(&msg->goal);
}

rover_utils__action__MinimalWalk_SendGoal_Request *
rover_utils__action__MinimalWalk_SendGoal_Request__create()
{
  rover_utils__action__MinimalWalk_SendGoal_Request * msg = (rover_utils__action__MinimalWalk_SendGoal_Request *)malloc(sizeof(rover_utils__action__MinimalWalk_SendGoal_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_SendGoal_Request));
  bool success = rover_utils__action__MinimalWalk_SendGoal_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_SendGoal_Request__destroy(rover_utils__action__MinimalWalk_SendGoal_Request * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_SendGoal_Request__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__init(rover_utils__action__MinimalWalk_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_SendGoal_Request * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_SendGoal_Request *)calloc(size, sizeof(rover_utils__action__MinimalWalk_SendGoal_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_SendGoal_Request__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__fini(rover_utils__action__MinimalWalk_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_SendGoal_Request__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_SendGoal_Request__Sequence *
rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_SendGoal_Request__Sequence * array = (rover_utils__action__MinimalWalk_SendGoal_Request__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_SendGoal_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__destroy(rover_utils__action__MinimalWalk_SendGoal_Request__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_SendGoal_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
rover_utils__action__MinimalWalk_SendGoal_Response__init(rover_utils__action__MinimalWalk_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    rover_utils__action__MinimalWalk_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
rover_utils__action__MinimalWalk_SendGoal_Response__fini(rover_utils__action__MinimalWalk_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

rover_utils__action__MinimalWalk_SendGoal_Response *
rover_utils__action__MinimalWalk_SendGoal_Response__create()
{
  rover_utils__action__MinimalWalk_SendGoal_Response * msg = (rover_utils__action__MinimalWalk_SendGoal_Response *)malloc(sizeof(rover_utils__action__MinimalWalk_SendGoal_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_SendGoal_Response));
  bool success = rover_utils__action__MinimalWalk_SendGoal_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_SendGoal_Response__destroy(rover_utils__action__MinimalWalk_SendGoal_Response * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_SendGoal_Response__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__init(rover_utils__action__MinimalWalk_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_SendGoal_Response * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_SendGoal_Response *)calloc(size, sizeof(rover_utils__action__MinimalWalk_SendGoal_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_SendGoal_Response__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__fini(rover_utils__action__MinimalWalk_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_SendGoal_Response__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_SendGoal_Response__Sequence *
rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_SendGoal_Response__Sequence * array = (rover_utils__action__MinimalWalk_SendGoal_Response__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_SendGoal_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__destroy(rover_utils__action__MinimalWalk_SendGoal_Response__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_SendGoal_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
rover_utils__action__MinimalWalk_GetResult_Request__init(rover_utils__action__MinimalWalk_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    rover_utils__action__MinimalWalk_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
rover_utils__action__MinimalWalk_GetResult_Request__fini(rover_utils__action__MinimalWalk_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

rover_utils__action__MinimalWalk_GetResult_Request *
rover_utils__action__MinimalWalk_GetResult_Request__create()
{
  rover_utils__action__MinimalWalk_GetResult_Request * msg = (rover_utils__action__MinimalWalk_GetResult_Request *)malloc(sizeof(rover_utils__action__MinimalWalk_GetResult_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_GetResult_Request));
  bool success = rover_utils__action__MinimalWalk_GetResult_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_GetResult_Request__destroy(rover_utils__action__MinimalWalk_GetResult_Request * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_GetResult_Request__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_GetResult_Request__Sequence__init(rover_utils__action__MinimalWalk_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_GetResult_Request * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_GetResult_Request *)calloc(size, sizeof(rover_utils__action__MinimalWalk_GetResult_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_GetResult_Request__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_GetResult_Request__Sequence__fini(rover_utils__action__MinimalWalk_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_GetResult_Request__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_GetResult_Request__Sequence *
rover_utils__action__MinimalWalk_GetResult_Request__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_GetResult_Request__Sequence * array = (rover_utils__action__MinimalWalk_GetResult_Request__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_GetResult_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_GetResult_Request__Sequence__destroy(rover_utils__action__MinimalWalk_GetResult_Request__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_GetResult_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `result`
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"

bool
rover_utils__action__MinimalWalk_GetResult_Response__init(rover_utils__action__MinimalWalk_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!rover_utils__action__MinimalWalk_Result__init(&msg->result)) {
    rover_utils__action__MinimalWalk_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
rover_utils__action__MinimalWalk_GetResult_Response__fini(rover_utils__action__MinimalWalk_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  rover_utils__action__MinimalWalk_Result__fini(&msg->result);
}

rover_utils__action__MinimalWalk_GetResult_Response *
rover_utils__action__MinimalWalk_GetResult_Response__create()
{
  rover_utils__action__MinimalWalk_GetResult_Response * msg = (rover_utils__action__MinimalWalk_GetResult_Response *)malloc(sizeof(rover_utils__action__MinimalWalk_GetResult_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_GetResult_Response));
  bool success = rover_utils__action__MinimalWalk_GetResult_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_GetResult_Response__destroy(rover_utils__action__MinimalWalk_GetResult_Response * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_GetResult_Response__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_GetResult_Response__Sequence__init(rover_utils__action__MinimalWalk_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_GetResult_Response * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_GetResult_Response *)calloc(size, sizeof(rover_utils__action__MinimalWalk_GetResult_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_GetResult_Response__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_GetResult_Response__Sequence__fini(rover_utils__action__MinimalWalk_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_GetResult_Response__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_GetResult_Response__Sequence *
rover_utils__action__MinimalWalk_GetResult_Response__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_GetResult_Response__Sequence * array = (rover_utils__action__MinimalWalk_GetResult_Response__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_GetResult_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_GetResult_Response__Sequence__destroy(rover_utils__action__MinimalWalk_GetResult_Response__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_GetResult_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "rover_utils/action/detail/minimal_walk__functions.h"

bool
rover_utils__action__MinimalWalk_FeedbackMessage__init(rover_utils__action__MinimalWalk_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    rover_utils__action__MinimalWalk_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!rover_utils__action__MinimalWalk_Feedback__init(&msg->feedback)) {
    rover_utils__action__MinimalWalk_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
rover_utils__action__MinimalWalk_FeedbackMessage__fini(rover_utils__action__MinimalWalk_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  rover_utils__action__MinimalWalk_Feedback__fini(&msg->feedback);
}

rover_utils__action__MinimalWalk_FeedbackMessage *
rover_utils__action__MinimalWalk_FeedbackMessage__create()
{
  rover_utils__action__MinimalWalk_FeedbackMessage * msg = (rover_utils__action__MinimalWalk_FeedbackMessage *)malloc(sizeof(rover_utils__action__MinimalWalk_FeedbackMessage));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(rover_utils__action__MinimalWalk_FeedbackMessage));
  bool success = rover_utils__action__MinimalWalk_FeedbackMessage__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
rover_utils__action__MinimalWalk_FeedbackMessage__destroy(rover_utils__action__MinimalWalk_FeedbackMessage * msg)
{
  if (msg) {
    rover_utils__action__MinimalWalk_FeedbackMessage__fini(msg);
  }
  free(msg);
}


bool
rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__init(rover_utils__action__MinimalWalk_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rover_utils__action__MinimalWalk_FeedbackMessage * data = NULL;
  if (size) {
    data = (rover_utils__action__MinimalWalk_FeedbackMessage *)calloc(size, sizeof(rover_utils__action__MinimalWalk_FeedbackMessage));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = rover_utils__action__MinimalWalk_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        rover_utils__action__MinimalWalk_FeedbackMessage__fini(&data[i - 1]);
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
rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__fini(rover_utils__action__MinimalWalk_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      rover_utils__action__MinimalWalk_FeedbackMessage__fini(&array->data[i]);
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

rover_utils__action__MinimalWalk_FeedbackMessage__Sequence *
rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__create(size_t size)
{
  rover_utils__action__MinimalWalk_FeedbackMessage__Sequence * array = (rover_utils__action__MinimalWalk_FeedbackMessage__Sequence *)malloc(sizeof(rover_utils__action__MinimalWalk_FeedbackMessage__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__destroy(rover_utils__action__MinimalWalk_FeedbackMessage__Sequence * array)
{
  if (array) {
    rover_utils__action__MinimalWalk_FeedbackMessage__Sequence__fini(array);
  }
  free(array);
}

// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
#include "rover_utils/action/detail/minimal_walk__struct.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_Goal_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_Goal_type_support_ids_t;

static const _MinimalWalk_Goal_type_support_ids_t _MinimalWalk_Goal_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_Goal_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_Goal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_Goal_type_support_symbol_names_t _MinimalWalk_Goal_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_Goal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Goal)),
  }
};

typedef struct _MinimalWalk_Goal_type_support_data_t
{
  void * data[3];
} _MinimalWalk_Goal_type_support_data_t;

static _MinimalWalk_Goal_type_support_data_t _MinimalWalk_Goal_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_Goal_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_Goal_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_Goal_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_Goal_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_Goal_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_Goal_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_Goal)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_Goal_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_Result_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_Result_type_support_ids_t;

static const _MinimalWalk_Result_type_support_ids_t _MinimalWalk_Result_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_Result_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_Result_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_Result_type_support_symbol_names_t _MinimalWalk_Result_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_Result)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Result)),
  }
};

typedef struct _MinimalWalk_Result_type_support_data_t
{
  void * data[3];
} _MinimalWalk_Result_type_support_data_t;

static _MinimalWalk_Result_type_support_data_t _MinimalWalk_Result_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_Result_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_Result_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_Result_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_Result_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_Result_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_Result_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_Result)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_Result_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_Feedback_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_Feedback_type_support_ids_t;

static const _MinimalWalk_Feedback_type_support_ids_t _MinimalWalk_Feedback_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_Feedback_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_Feedback_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_Feedback_type_support_symbol_names_t _MinimalWalk_Feedback_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_Feedback)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_Feedback)),
  }
};

typedef struct _MinimalWalk_Feedback_type_support_data_t
{
  void * data[3];
} _MinimalWalk_Feedback_type_support_data_t;

static _MinimalWalk_Feedback_type_support_data_t _MinimalWalk_Feedback_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_Feedback_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_Feedback_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_Feedback_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_Feedback_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_Feedback_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_Feedback_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_Feedback)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_Feedback_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_SendGoal_Request_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_SendGoal_Request_type_support_ids_t;

static const _MinimalWalk_SendGoal_Request_type_support_ids_t _MinimalWalk_SendGoal_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_SendGoal_Request_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_SendGoal_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_SendGoal_Request_type_support_symbol_names_t _MinimalWalk_SendGoal_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_SendGoal_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Request)),
  }
};

typedef struct _MinimalWalk_SendGoal_Request_type_support_data_t
{
  void * data[3];
} _MinimalWalk_SendGoal_Request_type_support_data_t;

static _MinimalWalk_SendGoal_Request_type_support_data_t _MinimalWalk_SendGoal_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_SendGoal_Request_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_SendGoal_Request_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_SendGoal_Request_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_SendGoal_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_SendGoal_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_SendGoal_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_SendGoal_Request)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_SendGoal_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_SendGoal_Response_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_SendGoal_Response_type_support_ids_t;

static const _MinimalWalk_SendGoal_Response_type_support_ids_t _MinimalWalk_SendGoal_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_SendGoal_Response_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_SendGoal_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_SendGoal_Response_type_support_symbol_names_t _MinimalWalk_SendGoal_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_SendGoal_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal_Response)),
  }
};

typedef struct _MinimalWalk_SendGoal_Response_type_support_data_t
{
  void * data[3];
} _MinimalWalk_SendGoal_Response_type_support_data_t;

static _MinimalWalk_SendGoal_Response_type_support_data_t _MinimalWalk_SendGoal_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_SendGoal_Response_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_SendGoal_Response_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_SendGoal_Response_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_SendGoal_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_SendGoal_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_SendGoal_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_SendGoal_Response)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_SendGoal_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_SendGoal_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_SendGoal_type_support_ids_t;

static const _MinimalWalk_SendGoal_type_support_ids_t _MinimalWalk_SendGoal_service_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_SendGoal_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_SendGoal_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_SendGoal_type_support_symbol_names_t _MinimalWalk_SendGoal_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_SendGoal)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_SendGoal)),
  }
};

typedef struct _MinimalWalk_SendGoal_type_support_data_t
{
  void * data[3];
} _MinimalWalk_SendGoal_type_support_data_t;

static _MinimalWalk_SendGoal_type_support_data_t _MinimalWalk_SendGoal_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_SendGoal_service_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_SendGoal_service_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_SendGoal_service_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_SendGoal_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t MinimalWalk_SendGoal_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_SendGoal_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_SendGoal)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_SendGoal_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_GetResult_Request_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_GetResult_Request_type_support_ids_t;

static const _MinimalWalk_GetResult_Request_type_support_ids_t _MinimalWalk_GetResult_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_GetResult_Request_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_GetResult_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_GetResult_Request_type_support_symbol_names_t _MinimalWalk_GetResult_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_GetResult_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Request)),
  }
};

typedef struct _MinimalWalk_GetResult_Request_type_support_data_t
{
  void * data[3];
} _MinimalWalk_GetResult_Request_type_support_data_t;

static _MinimalWalk_GetResult_Request_type_support_data_t _MinimalWalk_GetResult_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_GetResult_Request_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_GetResult_Request_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_GetResult_Request_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_GetResult_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_GetResult_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_GetResult_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_GetResult_Request)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_GetResult_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_GetResult_Response_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_GetResult_Response_type_support_ids_t;

static const _MinimalWalk_GetResult_Response_type_support_ids_t _MinimalWalk_GetResult_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_GetResult_Response_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_GetResult_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_GetResult_Response_type_support_symbol_names_t _MinimalWalk_GetResult_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_GetResult_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult_Response)),
  }
};

typedef struct _MinimalWalk_GetResult_Response_type_support_data_t
{
  void * data[3];
} _MinimalWalk_GetResult_Response_type_support_data_t;

static _MinimalWalk_GetResult_Response_type_support_data_t _MinimalWalk_GetResult_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_GetResult_Response_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_GetResult_Response_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_GetResult_Response_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_GetResult_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_GetResult_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_GetResult_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_GetResult_Response)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_GetResult_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_GetResult_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_GetResult_type_support_ids_t;

static const _MinimalWalk_GetResult_type_support_ids_t _MinimalWalk_GetResult_service_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_GetResult_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_GetResult_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_GetResult_type_support_symbol_names_t _MinimalWalk_GetResult_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_GetResult)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_GetResult)),
  }
};

typedef struct _MinimalWalk_GetResult_type_support_data_t
{
  void * data[3];
} _MinimalWalk_GetResult_type_support_data_t;

static _MinimalWalk_GetResult_type_support_data_t _MinimalWalk_GetResult_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_GetResult_service_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_GetResult_service_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_GetResult_service_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_GetResult_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t MinimalWalk_GetResult_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_GetResult_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_GetResult)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_GetResult_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rover_utils/msg/rosidl_typesupport_c__visibility_control.h"
// already included above
// #include "rover_utils/action/detail/minimal_walk__struct.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace rover_utils
{

namespace action
{

namespace rosidl_typesupport_c
{

typedef struct _MinimalWalk_FeedbackMessage_type_support_ids_t
{
  const char * typesupport_identifier[3];
} _MinimalWalk_FeedbackMessage_type_support_ids_t;

static const _MinimalWalk_FeedbackMessage_type_support_ids_t _MinimalWalk_FeedbackMessage_message_typesupport_ids = {
  {
    "rosidl_typesupport_connext_c",  // ::rosidl_typesupport_connext_c::typesupport_identifier,
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _MinimalWalk_FeedbackMessage_type_support_symbol_names_t
{
  const char * symbol_name[3];
} _MinimalWalk_FeedbackMessage_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _MinimalWalk_FeedbackMessage_type_support_symbol_names_t _MinimalWalk_FeedbackMessage_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_connext_c, rover_utils, action, MinimalWalk_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, rover_utils, action, MinimalWalk_FeedbackMessage)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, rover_utils, action, MinimalWalk_FeedbackMessage)),
  }
};

typedef struct _MinimalWalk_FeedbackMessage_type_support_data_t
{
  void * data[3];
} _MinimalWalk_FeedbackMessage_type_support_data_t;

static _MinimalWalk_FeedbackMessage_type_support_data_t _MinimalWalk_FeedbackMessage_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _MinimalWalk_FeedbackMessage_message_typesupport_map = {
  3,
  "rover_utils",
  &_MinimalWalk_FeedbackMessage_message_typesupport_ids.typesupport_identifier[0],
  &_MinimalWalk_FeedbackMessage_message_typesupport_symbol_names.symbol_name[0],
  &_MinimalWalk_FeedbackMessage_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t MinimalWalk_FeedbackMessage_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_MinimalWalk_FeedbackMessage_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace action

}  // namespace rover_utils

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, rover_utils, action, MinimalWalk_FeedbackMessage)() {
  return &::rover_utils::action::rosidl_typesupport_c::MinimalWalk_FeedbackMessage_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "action_msgs/msg/goal_status_array.h"
#include "action_msgs/srv/cancel_goal.h"
#include "rover_utils/action/minimal_walk.h"
#include "rover_utils/action/detail/minimal_walk__type_support.h"

static rosidl_action_type_support_t _rover_utils__action__MinimalWalk__typesupport_c;

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_C_EXPORT_rover_utils
const rosidl_action_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__ACTION_SYMBOL_NAME(
  rosidl_typesupport_c, rover_utils, action, MinimalWalk)()
{
  // Thread-safe by always writing the same values to the static struct
  _rover_utils__action__MinimalWalk__typesupport_c.goal_service_type_support =
    ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(
    rosidl_typesupport_c, rover_utils, action, MinimalWalk_SendGoal)();
  _rover_utils__action__MinimalWalk__typesupport_c.result_service_type_support =
    ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(
    rosidl_typesupport_c, rover_utils, action, MinimalWalk_GetResult)();
  _rover_utils__action__MinimalWalk__typesupport_c.cancel_service_type_support =
    ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(
    rosidl_typesupport_c, action_msgs, srv, CancelGoal)();
  _rover_utils__action__MinimalWalk__typesupport_c.feedback_message_type_support =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c, rover_utils, action, MinimalWalk_FeedbackMessage)();
  _rover_utils__action__MinimalWalk__typesupport_c.status_message_type_support =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c, action_msgs, msg, GoalStatusArray)();

  return &_rover_utils__action__MinimalWalk__typesupport_c;
}

#ifdef __cplusplus
}
#endif

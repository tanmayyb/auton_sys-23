// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__TRAITS_HPP_
#define ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__TRAITS_HPP_

#include "rover_utils/action/detail/minimal_walk__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_Goal>()
{
  return "rover_utils::action::MinimalWalk_Goal";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_Goal>()
{
  return "rover_utils/action/MinimalWalk_Goal";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_Result>()
{
  return "rover_utils::action::MinimalWalk_Result";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_Result>()
{
  return "rover_utils/action/MinimalWalk_Result";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_Result>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_Feedback>()
{
  return "rover_utils::action::MinimalWalk_Feedback";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_Feedback>()
{
  return "rover_utils/action/MinimalWalk_Feedback";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "rover_utils/action/detail/minimal_walk__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_SendGoal_Request>()
{
  return "rover_utils::action::MinimalWalk_SendGoal_Request";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_SendGoal_Request>()
{
  return "rover_utils/action/MinimalWalk_SendGoal_Request";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<rover_utils::action::MinimalWalk_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<rover_utils::action::MinimalWalk_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_SendGoal_Response>()
{
  return "rover_utils::action::MinimalWalk_SendGoal_Response";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_SendGoal_Response>()
{
  return "rover_utils/action/MinimalWalk_SendGoal_Response";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_SendGoal>()
{
  return "rover_utils::action::MinimalWalk_SendGoal";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_SendGoal>()
{
  return "rover_utils/action/MinimalWalk_SendGoal";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<rover_utils::action::MinimalWalk_SendGoal_Request>::value &&
    has_fixed_size<rover_utils::action::MinimalWalk_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<rover_utils::action::MinimalWalk_SendGoal_Request>::value &&
    has_bounded_size<rover_utils::action::MinimalWalk_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<rover_utils::action::MinimalWalk_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<rover_utils::action::MinimalWalk_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<rover_utils::action::MinimalWalk_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_GetResult_Request>()
{
  return "rover_utils::action::MinimalWalk_GetResult_Request";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_GetResult_Request>()
{
  return "rover_utils/action/MinimalWalk_GetResult_Request";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "rover_utils/action/detail/minimal_walk__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_GetResult_Response>()
{
  return "rover_utils::action::MinimalWalk_GetResult_Response";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_GetResult_Response>()
{
  return "rover_utils/action/MinimalWalk_GetResult_Response";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<rover_utils::action::MinimalWalk_Result>::value> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<rover_utils::action::MinimalWalk_Result>::value> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_GetResult>()
{
  return "rover_utils::action::MinimalWalk_GetResult";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_GetResult>()
{
  return "rover_utils/action/MinimalWalk_GetResult";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<rover_utils::action::MinimalWalk_GetResult_Request>::value &&
    has_fixed_size<rover_utils::action::MinimalWalk_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<rover_utils::action::MinimalWalk_GetResult_Request>::value &&
    has_bounded_size<rover_utils::action::MinimalWalk_GetResult_Response>::value
  >
{
};

template<>
struct is_service<rover_utils::action::MinimalWalk_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<rover_utils::action::MinimalWalk_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<rover_utils::action::MinimalWalk_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "rover_utils/action/detail/minimal_walk__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<rover_utils::action::MinimalWalk_FeedbackMessage>()
{
  return "rover_utils::action::MinimalWalk_FeedbackMessage";
}

template<>
inline const char * name<rover_utils::action::MinimalWalk_FeedbackMessage>()
{
  return "rover_utils/action/MinimalWalk_FeedbackMessage";
}

template<>
struct has_fixed_size<rover_utils::action::MinimalWalk_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<rover_utils::action::MinimalWalk_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<rover_utils::action::MinimalWalk_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<rover_utils::action::MinimalWalk_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<rover_utils::action::MinimalWalk_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<rover_utils::action::MinimalWalk>
  : std::true_type
{
};

template<>
struct is_action_goal<rover_utils::action::MinimalWalk_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<rover_utils::action::MinimalWalk_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<rover_utils::action::MinimalWalk_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__TRAITS_HPP_

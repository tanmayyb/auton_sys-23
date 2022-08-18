// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from rover_utils:action/MinimalWalk.idl
// generated code does not contain a copyright notice

#ifndef ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__BUILDER_HPP_
#define ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__BUILDER_HPP_

#include "rover_utils/action/detail/minimal_walk__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_Goal_goal_var
{
public:
  Init_MinimalWalk_Goal_goal_var()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::rover_utils::action::MinimalWalk_Goal goal_var(::rover_utils::action::MinimalWalk_Goal::_goal_var_type arg)
  {
    msg_.goal_var = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_Goal>()
{
  return rover_utils::action::builder::Init_MinimalWalk_Goal_goal_var();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_Result_result
{
public:
  Init_MinimalWalk_Result_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::rover_utils::action::MinimalWalk_Result result(::rover_utils::action::MinimalWalk_Result::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_Result>()
{
  return rover_utils::action::builder::Init_MinimalWalk_Result_result();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_Feedback_feedback
{
public:
  Init_MinimalWalk_Feedback_feedback()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::rover_utils::action::MinimalWalk_Feedback feedback(::rover_utils::action::MinimalWalk_Feedback::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_Feedback>()
{
  return rover_utils::action::builder::Init_MinimalWalk_Feedback_feedback();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_SendGoal_Request_goal
{
public:
  explicit Init_MinimalWalk_SendGoal_Request_goal(::rover_utils::action::MinimalWalk_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::rover_utils::action::MinimalWalk_SendGoal_Request goal(::rover_utils::action::MinimalWalk_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_SendGoal_Request msg_;
};

class Init_MinimalWalk_SendGoal_Request_goal_id
{
public:
  Init_MinimalWalk_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MinimalWalk_SendGoal_Request_goal goal_id(::rover_utils::action::MinimalWalk_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MinimalWalk_SendGoal_Request_goal(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_SendGoal_Request>()
{
  return rover_utils::action::builder::Init_MinimalWalk_SendGoal_Request_goal_id();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_SendGoal_Response_stamp
{
public:
  explicit Init_MinimalWalk_SendGoal_Response_stamp(::rover_utils::action::MinimalWalk_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::rover_utils::action::MinimalWalk_SendGoal_Response stamp(::rover_utils::action::MinimalWalk_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_SendGoal_Response msg_;
};

class Init_MinimalWalk_SendGoal_Response_accepted
{
public:
  Init_MinimalWalk_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MinimalWalk_SendGoal_Response_stamp accepted(::rover_utils::action::MinimalWalk_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_MinimalWalk_SendGoal_Response_stamp(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_SendGoal_Response>()
{
  return rover_utils::action::builder::Init_MinimalWalk_SendGoal_Response_accepted();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_GetResult_Request_goal_id
{
public:
  Init_MinimalWalk_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::rover_utils::action::MinimalWalk_GetResult_Request goal_id(::rover_utils::action::MinimalWalk_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_GetResult_Request>()
{
  return rover_utils::action::builder::Init_MinimalWalk_GetResult_Request_goal_id();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_GetResult_Response_result
{
public:
  explicit Init_MinimalWalk_GetResult_Response_result(::rover_utils::action::MinimalWalk_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::rover_utils::action::MinimalWalk_GetResult_Response result(::rover_utils::action::MinimalWalk_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_GetResult_Response msg_;
};

class Init_MinimalWalk_GetResult_Response_status
{
public:
  Init_MinimalWalk_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MinimalWalk_GetResult_Response_result status(::rover_utils::action::MinimalWalk_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_MinimalWalk_GetResult_Response_result(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_GetResult_Response>()
{
  return rover_utils::action::builder::Init_MinimalWalk_GetResult_Response_status();
}

}  // namespace rover_utils


namespace rover_utils
{

namespace action
{

namespace builder
{

class Init_MinimalWalk_FeedbackMessage_feedback
{
public:
  explicit Init_MinimalWalk_FeedbackMessage_feedback(::rover_utils::action::MinimalWalk_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::rover_utils::action::MinimalWalk_FeedbackMessage feedback(::rover_utils::action::MinimalWalk_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_FeedbackMessage msg_;
};

class Init_MinimalWalk_FeedbackMessage_goal_id
{
public:
  Init_MinimalWalk_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MinimalWalk_FeedbackMessage_feedback goal_id(::rover_utils::action::MinimalWalk_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MinimalWalk_FeedbackMessage_feedback(msg_);
  }

private:
  ::rover_utils::action::MinimalWalk_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::rover_utils::action::MinimalWalk_FeedbackMessage>()
{
  return rover_utils::action::builder::Init_MinimalWalk_FeedbackMessage_goal_id();
}

}  // namespace rover_utils

#endif  // ROVER_UTILS__ACTION__DETAIL__MINIMAL_WALK__BUILDER_HPP_

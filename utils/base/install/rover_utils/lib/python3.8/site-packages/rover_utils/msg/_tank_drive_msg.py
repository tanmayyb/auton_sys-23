# generated from rosidl_generator_py/resource/_idl.py.em
# with input from rover_utils:msg/TankDriveMsg.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TankDriveMsg(type):
    """Metaclass of message 'TankDriveMsg'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('rover_utils')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'rover_utils.msg.TankDriveMsg')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__tank_drive_msg
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__tank_drive_msg
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__tank_drive_msg
            cls._TYPE_SUPPORT = module.type_support_msg__msg__tank_drive_msg
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__tank_drive_msg

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TankDriveMsg(metaclass=Metaclass_TankDriveMsg):
    """Message class 'TankDriveMsg'."""

    __slots__ = [
        '_lpwm',
        '_rpwm',
    ]

    _fields_and_field_types = {
        'lpwm': 'int32',
        'rpwm': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.lpwm = kwargs.get('lpwm', int())
        self.rpwm = kwargs.get('rpwm', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.lpwm != other.lpwm:
            return False
        if self.rpwm != other.rpwm:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def lpwm(self):
        """Message field 'lpwm'."""
        return self._lpwm

    @lpwm.setter
    def lpwm(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'lpwm' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'lpwm' field must be an integer in [-2147483648, 2147483647]"
        self._lpwm = value

    @property
    def rpwm(self):
        """Message field 'rpwm'."""
        return self._rpwm

    @rpwm.setter
    def rpwm(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'rpwm' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'rpwm' field must be an integer in [-2147483648, 2147483647]"
        self._rpwm = value

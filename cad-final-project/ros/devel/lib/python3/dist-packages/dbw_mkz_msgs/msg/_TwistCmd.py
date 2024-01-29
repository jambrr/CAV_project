# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dbw_mkz_msgs/TwistCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class TwistCmd(genpy.Message):
  _md5sum = "ef873397d04f1a8acdfa4bcab4392286"
  _type = "dbw_mkz_msgs/TwistCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Twist twist
float32 accel_limit # m/s^2, zero = no limit
float32 decel_limit # m/s^2, zero = no limit

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['twist','accel_limit','decel_limit']
  _slot_types = ['geometry_msgs/Twist','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       twist,accel_limit,decel_limit

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TwistCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      if self.accel_limit is None:
        self.accel_limit = 0.
      if self.decel_limit is None:
        self.decel_limit = 0.
    else:
      self.twist = geometry_msgs.msg.Twist()
      self.accel_limit = 0.
      self.decel_limit = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6d2f().pack(_x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel_limit, _x.decel_limit))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel_limit, _x.decel_limit,) = _get_struct_6d2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6d2f().pack(_x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel_limit, _x.decel_limit))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel_limit, _x.decel_limit,) = _get_struct_6d2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6d2f = None
def _get_struct_6d2f():
    global _struct_6d2f
    if _struct_6d2f is None:
        _struct_6d2f = struct.Struct("<6d2f")
    return _struct_6d2f

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dbw_mkz_msgs/ThrottleCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ThrottleCmd(genpy.Message):
  _md5sum = "d75259a1444adebea30e45b37542c415"
  _type = "dbw_mkz_msgs/ThrottleCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Throttle pedal
# Options defined below
float32 pedal_cmd
uint8 pedal_cmd_type

# Enable
bool enable

# Clear driver overrides
bool clear

# Ignore driver overrides
bool ignore

# Watchdog counter (optional)
uint8 count

uint8 CMD_NONE=0
uint8 CMD_PEDAL=1   # Unitless, range 0.15 to 0.80
uint8 CMD_PERCENT=2 # Percent of maximum throttle, range 0 to 1
"""
  # Pseudo-constants
  CMD_NONE = 0
  CMD_PEDAL = 1
  CMD_PERCENT = 2

  __slots__ = ['pedal_cmd','pedal_cmd_type','enable','clear','ignore','count']
  _slot_types = ['float32','uint8','bool','bool','bool','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pedal_cmd,pedal_cmd_type,enable,clear,ignore,count

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ThrottleCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.pedal_cmd is None:
        self.pedal_cmd = 0.
      if self.pedal_cmd_type is None:
        self.pedal_cmd_type = 0
      if self.enable is None:
        self.enable = False
      if self.clear is None:
        self.clear = False
      if self.ignore is None:
        self.ignore = False
      if self.count is None:
        self.count = 0
    else:
      self.pedal_cmd = 0.
      self.pedal_cmd_type = 0
      self.enable = False
      self.clear = False
      self.ignore = False
      self.count = 0

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
      buff.write(_get_struct_f5B().pack(_x.pedal_cmd, _x.pedal_cmd_type, _x.enable, _x.clear, _x.ignore, _x.count))
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
      end = 0
      _x = self
      start = end
      end += 9
      (_x.pedal_cmd, _x.pedal_cmd_type, _x.enable, _x.clear, _x.ignore, _x.count,) = _get_struct_f5B().unpack(str[start:end])
      self.enable = bool(self.enable)
      self.clear = bool(self.clear)
      self.ignore = bool(self.ignore)
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
      buff.write(_get_struct_f5B().pack(_x.pedal_cmd, _x.pedal_cmd_type, _x.enable, _x.clear, _x.ignore, _x.count))
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
      end = 0
      _x = self
      start = end
      end += 9
      (_x.pedal_cmd, _x.pedal_cmd_type, _x.enable, _x.clear, _x.ignore, _x.count,) = _get_struct_f5B().unpack(str[start:end])
      self.enable = bool(self.enable)
      self.clear = bool(self.clear)
      self.ignore = bool(self.ignore)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f5B = None
def _get_struct_f5B():
    global _struct_f5B
    if _struct_f5B is None:
        _struct_f5B = struct.Struct("<f5B")
    return _struct_f5B

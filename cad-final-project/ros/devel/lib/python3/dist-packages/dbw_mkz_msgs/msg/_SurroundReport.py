# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dbw_mkz_msgs/SurroundReport.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SurroundReport(genpy.Message):
  _md5sum = "17a8c9ed72da4f55d44d6d71483cf0e3"
  _type = "dbw_mkz_msgs/SurroundReport"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

# Cross Traffic Alert (CTA)
bool cta_left_alert
bool cta_right_alert
bool cta_left_enabled
bool cta_right_enabled

# Blind Spot Information System (BLIS)
bool blis_left_alert
bool blis_right_alert
bool blis_left_enabled
bool blis_right_enabled

# Sonar Sensors
bool sonar_enabled
bool sonar_fault

# Sonar ranges in meters, zero is no-detection
float32[12] sonar

# Sonar index enumeration
uint8 FRONT_LEFT_SIDE=0
uint8 FRONT_LEFT_CORNER=1
uint8 FRONT_LEFT_CENTER=2
uint8 FRONT_RIGHT_CENTER=3
uint8 FRONT_RIGHT_CORNER=4
uint8 FRONT_RIGHT_SIDE=5
uint8 REAR_LEFT_SIDE=6
uint8 REAR_LEFT_CORNER=7
uint8 REAR_LEFT_CENTER=8
uint8 REAR_RIGHT_CENTER=9
uint8 REAR_RIGHT_CORNER=10
uint8 REAR_RIGHT_SIDE=11

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  FRONT_LEFT_SIDE = 0
  FRONT_LEFT_CORNER = 1
  FRONT_LEFT_CENTER = 2
  FRONT_RIGHT_CENTER = 3
  FRONT_RIGHT_CORNER = 4
  FRONT_RIGHT_SIDE = 5
  REAR_LEFT_SIDE = 6
  REAR_LEFT_CORNER = 7
  REAR_LEFT_CENTER = 8
  REAR_RIGHT_CENTER = 9
  REAR_RIGHT_CORNER = 10
  REAR_RIGHT_SIDE = 11

  __slots__ = ['header','cta_left_alert','cta_right_alert','cta_left_enabled','cta_right_enabled','blis_left_alert','blis_right_alert','blis_left_enabled','blis_right_enabled','sonar_enabled','sonar_fault','sonar']
  _slot_types = ['std_msgs/Header','bool','bool','bool','bool','bool','bool','bool','bool','bool','bool','float32[12]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,cta_left_alert,cta_right_alert,cta_left_enabled,cta_right_enabled,blis_left_alert,blis_right_alert,blis_left_enabled,blis_right_enabled,sonar_enabled,sonar_fault,sonar

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SurroundReport, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.cta_left_alert is None:
        self.cta_left_alert = False
      if self.cta_right_alert is None:
        self.cta_right_alert = False
      if self.cta_left_enabled is None:
        self.cta_left_enabled = False
      if self.cta_right_enabled is None:
        self.cta_right_enabled = False
      if self.blis_left_alert is None:
        self.blis_left_alert = False
      if self.blis_right_alert is None:
        self.blis_right_alert = False
      if self.blis_left_enabled is None:
        self.blis_left_enabled = False
      if self.blis_right_enabled is None:
        self.blis_right_enabled = False
      if self.sonar_enabled is None:
        self.sonar_enabled = False
      if self.sonar_fault is None:
        self.sonar_fault = False
      if self.sonar is None:
        self.sonar = [0.] * 12
    else:
      self.header = std_msgs.msg.Header()
      self.cta_left_alert = False
      self.cta_right_alert = False
      self.cta_left_enabled = False
      self.cta_right_enabled = False
      self.blis_left_alert = False
      self.blis_right_alert = False
      self.blis_left_enabled = False
      self.blis_right_enabled = False
      self.sonar_enabled = False
      self.sonar_fault = False
      self.sonar = [0.] * 12

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_10B().pack(_x.cta_left_alert, _x.cta_right_alert, _x.cta_left_enabled, _x.cta_right_enabled, _x.blis_left_alert, _x.blis_right_alert, _x.blis_left_enabled, _x.blis_right_enabled, _x.sonar_enabled, _x.sonar_fault))
      buff.write(_get_struct_12f().pack(*self.sonar))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.cta_left_alert, _x.cta_right_alert, _x.cta_left_enabled, _x.cta_right_enabled, _x.blis_left_alert, _x.blis_right_alert, _x.blis_left_enabled, _x.blis_right_enabled, _x.sonar_enabled, _x.sonar_fault,) = _get_struct_10B().unpack(str[start:end])
      self.cta_left_alert = bool(self.cta_left_alert)
      self.cta_right_alert = bool(self.cta_right_alert)
      self.cta_left_enabled = bool(self.cta_left_enabled)
      self.cta_right_enabled = bool(self.cta_right_enabled)
      self.blis_left_alert = bool(self.blis_left_alert)
      self.blis_right_alert = bool(self.blis_right_alert)
      self.blis_left_enabled = bool(self.blis_left_enabled)
      self.blis_right_enabled = bool(self.blis_right_enabled)
      self.sonar_enabled = bool(self.sonar_enabled)
      self.sonar_fault = bool(self.sonar_fault)
      start = end
      end += 48
      self.sonar = _get_struct_12f().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_10B().pack(_x.cta_left_alert, _x.cta_right_alert, _x.cta_left_enabled, _x.cta_right_enabled, _x.blis_left_alert, _x.blis_right_alert, _x.blis_left_enabled, _x.blis_right_enabled, _x.sonar_enabled, _x.sonar_fault))
      buff.write(self.sonar.tostring())
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.cta_left_alert, _x.cta_right_alert, _x.cta_left_enabled, _x.cta_right_enabled, _x.blis_left_alert, _x.blis_right_alert, _x.blis_left_enabled, _x.blis_right_enabled, _x.sonar_enabled, _x.sonar_fault,) = _get_struct_10B().unpack(str[start:end])
      self.cta_left_alert = bool(self.cta_left_alert)
      self.cta_right_alert = bool(self.cta_right_alert)
      self.cta_left_enabled = bool(self.cta_left_enabled)
      self.cta_right_enabled = bool(self.cta_right_enabled)
      self.blis_left_alert = bool(self.blis_left_alert)
      self.blis_right_alert = bool(self.blis_right_alert)
      self.blis_left_enabled = bool(self.blis_left_enabled)
      self.blis_right_enabled = bool(self.blis_right_enabled)
      self.sonar_enabled = bool(self.sonar_enabled)
      self.sonar_fault = bool(self.sonar_fault)
      start = end
      end += 48
      self.sonar = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=12)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10B = None
def _get_struct_10B():
    global _struct_10B
    if _struct_10B is None:
        _struct_10B = struct.Struct("<10B")
    return _struct_10B
_struct_12f = None
def _get_struct_12f():
    global _struct_12f
    if _struct_12f is None:
        _struct_12f = struct.Struct("<12f")
    return _struct_12f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I

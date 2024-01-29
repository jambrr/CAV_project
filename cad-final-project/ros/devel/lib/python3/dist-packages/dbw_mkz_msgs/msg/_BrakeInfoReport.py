# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dbw_mkz_msgs/BrakeInfoReport.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import dbw_mkz_msgs.msg
import std_msgs.msg

class BrakeInfoReport(genpy.Message):
  _md5sum = "fc88af128b5b3213ea25ab325a9b3bbb"
  _type = "dbw_mkz_msgs/BrakeInfoReport"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

# Wheel torques (Nm)
float32 brake_torque_request
float32 brake_torque_actual
float32 wheel_torque_actual

# Vehicle Acceleration (m/s^2)
float32 accel_over_ground

# Hill Start Assist
HillStartAssist hsa

# Anti-lock Brakes
bool abs_active
bool abs_enabled

# Stability Control
bool stab_active
bool stab_enabled

# Traction Control
bool trac_active
bool trac_enabled

# Parking Brake
ParkingBrake parking_brake

# Misc
bool stationary

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

================================================================================
MSG: dbw_mkz_msgs/HillStartAssist
uint8 status
uint8 mode

uint8 STAT_INACTIVE=0
uint8 STAT_FINDING_GRADIENT=1
uint8 STAT_ACTIVE_PRESSED=2
uint8 STAT_ACTIVE_RELEASED=3
uint8 STAT_FAST_RELEASE=4
uint8 STAT_SLOW_RELEASE=5
uint8 STAT_FAILED=6
uint8 STAT_UNDEFINED=7

uint8 MODE_OFF=0
uint8 MODE_AUTO=1
uint8 MODE_MANUAL=2
uint8 MODE_UNDEFINED=3

================================================================================
MSG: dbw_mkz_msgs/ParkingBrake
uint8 status

uint8 OFF=0
uint8 TRANS=1
uint8 ON=2
uint8 FAULT=3
"""
  __slots__ = ['header','brake_torque_request','brake_torque_actual','wheel_torque_actual','accel_over_ground','hsa','abs_active','abs_enabled','stab_active','stab_enabled','trac_active','trac_enabled','parking_brake','stationary']
  _slot_types = ['std_msgs/Header','float32','float32','float32','float32','dbw_mkz_msgs/HillStartAssist','bool','bool','bool','bool','bool','bool','dbw_mkz_msgs/ParkingBrake','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,brake_torque_request,brake_torque_actual,wheel_torque_actual,accel_over_ground,hsa,abs_active,abs_enabled,stab_active,stab_enabled,trac_active,trac_enabled,parking_brake,stationary

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BrakeInfoReport, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.brake_torque_request is None:
        self.brake_torque_request = 0.
      if self.brake_torque_actual is None:
        self.brake_torque_actual = 0.
      if self.wheel_torque_actual is None:
        self.wheel_torque_actual = 0.
      if self.accel_over_ground is None:
        self.accel_over_ground = 0.
      if self.hsa is None:
        self.hsa = dbw_mkz_msgs.msg.HillStartAssist()
      if self.abs_active is None:
        self.abs_active = False
      if self.abs_enabled is None:
        self.abs_enabled = False
      if self.stab_active is None:
        self.stab_active = False
      if self.stab_enabled is None:
        self.stab_enabled = False
      if self.trac_active is None:
        self.trac_active = False
      if self.trac_enabled is None:
        self.trac_enabled = False
      if self.parking_brake is None:
        self.parking_brake = dbw_mkz_msgs.msg.ParkingBrake()
      if self.stationary is None:
        self.stationary = False
    else:
      self.header = std_msgs.msg.Header()
      self.brake_torque_request = 0.
      self.brake_torque_actual = 0.
      self.wheel_torque_actual = 0.
      self.accel_over_ground = 0.
      self.hsa = dbw_mkz_msgs.msg.HillStartAssist()
      self.abs_active = False
      self.abs_enabled = False
      self.stab_active = False
      self.stab_enabled = False
      self.trac_active = False
      self.trac_enabled = False
      self.parking_brake = dbw_mkz_msgs.msg.ParkingBrake()
      self.stationary = False

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
      buff.write(_get_struct_4f10B().pack(_x.brake_torque_request, _x.brake_torque_actual, _x.wheel_torque_actual, _x.accel_over_ground, _x.hsa.status, _x.hsa.mode, _x.abs_active, _x.abs_enabled, _x.stab_active, _x.stab_enabled, _x.trac_active, _x.trac_enabled, _x.parking_brake.status, _x.stationary))
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
      if self.hsa is None:
        self.hsa = dbw_mkz_msgs.msg.HillStartAssist()
      if self.parking_brake is None:
        self.parking_brake = dbw_mkz_msgs.msg.ParkingBrake()
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
      end += 26
      (_x.brake_torque_request, _x.brake_torque_actual, _x.wheel_torque_actual, _x.accel_over_ground, _x.hsa.status, _x.hsa.mode, _x.abs_active, _x.abs_enabled, _x.stab_active, _x.stab_enabled, _x.trac_active, _x.trac_enabled, _x.parking_brake.status, _x.stationary,) = _get_struct_4f10B().unpack(str[start:end])
      self.abs_active = bool(self.abs_active)
      self.abs_enabled = bool(self.abs_enabled)
      self.stab_active = bool(self.stab_active)
      self.stab_enabled = bool(self.stab_enabled)
      self.trac_active = bool(self.trac_active)
      self.trac_enabled = bool(self.trac_enabled)
      self.stationary = bool(self.stationary)
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
      buff.write(_get_struct_4f10B().pack(_x.brake_torque_request, _x.brake_torque_actual, _x.wheel_torque_actual, _x.accel_over_ground, _x.hsa.status, _x.hsa.mode, _x.abs_active, _x.abs_enabled, _x.stab_active, _x.stab_enabled, _x.trac_active, _x.trac_enabled, _x.parking_brake.status, _x.stationary))
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
      if self.hsa is None:
        self.hsa = dbw_mkz_msgs.msg.HillStartAssist()
      if self.parking_brake is None:
        self.parking_brake = dbw_mkz_msgs.msg.ParkingBrake()
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
      end += 26
      (_x.brake_torque_request, _x.brake_torque_actual, _x.wheel_torque_actual, _x.accel_over_ground, _x.hsa.status, _x.hsa.mode, _x.abs_active, _x.abs_enabled, _x.stab_active, _x.stab_enabled, _x.trac_active, _x.trac_enabled, _x.parking_brake.status, _x.stationary,) = _get_struct_4f10B().unpack(str[start:end])
      self.abs_active = bool(self.abs_active)
      self.abs_enabled = bool(self.abs_enabled)
      self.stab_active = bool(self.stab_active)
      self.stab_enabled = bool(self.stab_enabled)
      self.trac_active = bool(self.trac_active)
      self.trac_enabled = bool(self.trac_enabled)
      self.stationary = bool(self.stationary)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4f10B = None
def _get_struct_4f10B():
    global _struct_4f10B
    if _struct_4f10B is None:
        _struct_4f10B = struct.Struct("<4f10B")
    return _struct_4f10B

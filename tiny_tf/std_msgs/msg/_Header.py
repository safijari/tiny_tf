# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/Header.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct



class Header():
  _md5sum = "2176decaecbce78abc3b96ef049fabed"
  _type = "std_msgs/Header"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Standard metadata for higher-level stamped data types.
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
  __slots__ = ['seq','stamp','frame_id']
  _slot_types = ['uint32','time','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       seq,stamp,frame_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Header, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.seq is None:
        self.seq = 0
      if self.stamp is None:
        self.stamp = 0 # Time is unused in tiny_tf
      if self.frame_id is None:
        self.frame_id = ''
    else:
      self.seq = 0
      self.stamp = 0 # Time is unused in tiny_tf
      self.frame_id = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/Int64.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct


class Int64():
  _md5sum = "34add168574510e6e17f5d23ecc077ef"
  _type = "std_msgs/Int64"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int64 data"""
  __slots__ = ['data']
  _slot_types = ['int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Int64, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.data is None:
        self.data = 0
    else:
      self.data = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
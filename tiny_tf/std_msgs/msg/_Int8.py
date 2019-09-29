# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/Int8.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct


class Int8():
  _md5sum = "27ffa0c9c4b8fb8492252bcad9e5c57b"
  _type = "std_msgs/Int8"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 data
"""
  __slots__ = ['data']
  _slot_types = ['int8']

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
      super(Int8, self).__init__(*args, **kwds)
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
# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/Empty.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct


class Empty():
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "std_msgs/Empty"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Empty, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
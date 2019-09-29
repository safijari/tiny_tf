# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/ColorRGBA.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct


class ColorRGBA():
  _md5sum = "a29a96539573343b1310c73607334b00"
  _type = "std_msgs/ColorRGBA"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 r
float32 g
float32 b
float32 a
"""
  __slots__ = ['r','g','b','a']
  _slot_types = ['float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       r,g,b,a

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ColorRGBA, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.r is None:
        self.r = 0.
      if self.g is None:
        self.g = 0.
      if self.b is None:
        self.b = 0.
      if self.a is None:
        self.a = 0.
    else:
      self.r = 0.
      self.g = 0.
      self.b = 0.
      self.a = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
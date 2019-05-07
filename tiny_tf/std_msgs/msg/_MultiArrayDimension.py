# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/MultiArrayDimension.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct


class MultiArrayDimension():
  _md5sum = "4cd0c83a8683deae40ecdac60e53bfa8"
  _type = "std_msgs/MultiArrayDimension"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension"""
  __slots__ = ['label','size','stride']
  _slot_types = ['string','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       label,size,stride

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MultiArrayDimension, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.label is None:
        self.label = ''
      if self.size is None:
        self.size = 0
      if self.stride is None:
        self.stride = 0
    else:
      self.label = ''
      self.size = 0
      self.stride = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
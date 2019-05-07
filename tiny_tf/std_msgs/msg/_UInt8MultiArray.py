# This Python file uses the following encoding: utf-8
"""Based on a ROS-generated file from std_msgs/UInt8MultiArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False

import struct

import std_msgs.msg

class UInt8MultiArray():
  _md5sum = "82373f1612381bb6ee473b5cd6f5d89c"
  _type = "std_msgs/UInt8MultiArray"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
uint8[]           data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = "height"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = "width"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = "channel"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension"""
  __slots__ = ['layout','data']
  _slot_types = ['std_msgs/MultiArrayLayout','uint8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       layout,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UInt8MultiArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.layout is None:
        self.layout = std_msgs.msg.MultiArrayLayout()
      if self.data is None:
        self.data = b''
    else:
      self.layout = std_msgs.msg.MultiArrayLayout()
      self.data = b''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types
#!/usr/bin/env python

import transformer as tf
import transformations as tf_transformations
import numpy as np
import geometry_msgs.msg

from math import pi


def set_transformations(tree):
  '''This sets up a TF tree for testing.'''

  # Define a little robot
  ts = geometry_msgs.msg.TransformStamped()
  ts.header.frame_id = "world"
  ts.child_frame_id = "robot_wrist"
  ts.transform.translation.z = 1.0
  ts.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(0, pi*90/180, 0))
  tree.setTransform(ts)

  ts.header.frame_id = "robot_wrist"
  ts.child_frame_id = "robot_tooltip"
  ts.transform.translation.z = 0.1
  ts.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(0, 0, 0))
  tree.setTransform(ts)

  ts.header.frame_id = "robot_wrist"
  ts.child_frame_id = "robot_camera"
  ts.transform.translation = geometry_msgs.msg.Point(x=-0.1, y=0.0, z=0.05)
  ts.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(0, pi*20/180, 0))
  tree.setTransform(ts)

  # Define a shelf
  ts.header.frame_id = "world"
  ts.child_frame_id = "shelf"
  ts.transform.translation = geometry_msgs.msg.Point(1.0, 0.0, 0.0)
  ts.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(0, 0, 0))
  tree.setTransform(ts)

  # Define some objects in the shelf
  points = [ [0.0, 0.0, 0.5], [0.0, 0.0, 1.0], [0.0, 0.0, 1.5]]
  rpys = [ [pi, pi*45/180, 0], [0, pi, pi*45/180], [pi*45/180, 0, pi]]

  ts.header.frame_id = "shelf"
  for i in range(len(points)):
      ts.transform.translation = geometry_msgs.msg.Point(*points[i])
      ts.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(*rpys[i]))
      ts.child_frame_id = "object_frame_" + str(i+1)
      tree.setTransform(ts)
  return  

def test_transformations(tree):
  ## Transform a pose
  ps = geometry_msgs.msg.PoseStamped()
  ps.pose.orientation.w = 1.0    # == no rotation
  ps.header.frame_id = "robot_tooltip"

  ps_new = tree.transformPose("world", ps)
  print("Robot tooltip position in the world frame:")
  print(str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z))
  print(str(ps_new.pose.orientation.x) + ", " + str(ps_new.pose.orientation.y)  + ", " + str(ps_new.pose.orientation.z)  + ", " + str(ps_new.pose.orientation.w))
  rpy = tf_transformations.euler_from_quaternion([ps_new.pose.orientation.x, ps_new.pose.orientation.y, ps_new.pose.orientation.z, ps_new.pose.orientation.w])
  print("In Euler angles (rad): " + str(rpy[0]) + ", " + str(rpy[1])  + ", " + str(rpy[2]))
  
  ps_new = tree.transformPose("robot_camera", ps)
  print("Robot tooltip position, as seen by the camera / in the camera frame:")
  print(str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z))
  print(str(ps_new.pose.orientation.x) + ", " + str(ps_new.pose.orientation.y)  + ", " + str(ps_new.pose.orientation.z)  + ", " + str(ps_new.pose.orientation.w))
  rpy = tf_transformations.euler_from_quaternion([ps_new.pose.orientation.x, ps_new.pose.orientation.y, ps_new.pose.orientation.z, ps_new.pose.orientation.w])
  print("In Euler angles (rad): " + str(rpy[0]) + ", " + str(rpy[1])  + ", " + str(rpy[2]))

  ps.header.frame_id = "object_frame_3"
  ps_new = tree.transformPose("robot_camera", ps)
  print("object_frame_3 position, as seen by the camera / in the camera frame:")
  print(str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z))
  
  ## Transform a point
  pt = geometry_msgs.msg.PointStamped()
  pt.point.z = 0.5
  pt.header.frame_id = "shelf"

  pt_new = tree.transformPoint("world", pt)
  print("z = 0.5 on the shelf, in world coordinates:")
  print(str(pt_new.point.x) + ", " + str(pt_new.point.y)  + ", " + str(pt_new.point.z))

  pt.point.z = 0.0
  pt.header.frame_id = "object_frame_2"
  pt_new = tree.transformPoint("robot_wrist", pt)
  point_array = np.array([pt_new.point.x, pt_new.point.y, pt_new.point.z])
  print("Distance of object_frame_2 to robot_wrist:" + str(np.norm(point_array)))
  return

if __name__ == '__main__':
  tree = tf.Transformer()
  set_transformations(tree)
  test_transformations(tree)
  print("============ Done!")
  
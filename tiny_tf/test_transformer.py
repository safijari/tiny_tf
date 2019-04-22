#!/usr/bin/env python

import transformer as tf
import transformations as tf_transformations
import numpy as np
import geometry_msgs.msg

from math import pi

class TFTest():
  def transformTargetPoseFromTipLinkToEE(self, tree, ps, robot_name, end_effector_link):
    """
    Example of a function using TF copied from another project.
    """
    print("Received a pose to transform to EE link:")
    print(str(ps.pose.position.x) + ", " + str(ps.pose.position.y)  + ", " + str(ps.pose.position.z))
    print(str(ps.pose.orientation.x) + ", " + str(ps.pose.orientation.y)  + ", " + str(ps.pose.orientation.z)  + ", " + str(ps.pose.orientation.w))

    # t = tree.lookupTransform(end_effector_link, robot_name + "_tool0")
    t = tree.lookup_transform(end_effector_link, robot_name + "_tool0")

    m = geometry_msgs.msg.TransformStamped()
    m.header.frame_id = ps.header.frame_id
    m.child_frame_id = "temp_goal_pose"
    m.transform.translation.x = ps.pose.position.x
    m.transform.translation.y = ps.pose.position.y
    m.transform.translation.z = ps.pose.position.z
    m.transform.rotation.x = ps.pose.orientation.x
    m.transform.rotation.y = ps.pose.orientation.y
    m.transform.rotation.z = ps.pose.orientation.z
    m.transform.rotation.w = ps.pose.orientation.w
    tree.setTransform(m)

    # m.header.frame_id = "temp_goal_pose"
    # m.child_frame_id = "temp_wrist_pose"
    # m.transform.translation.x = t[0][0]
    # m.transform.translation.y = t[0][1]
    # m.transform.translation.z = t[0][2]
    # m.transform.rotation.x = t[1][0]
    # m.transform.rotation.y = t[1][1]
    # m.transform.rotation.z = t[1][2]
    # m.transform.rotation.w = t[1][3]
    # tree.setTransform(m)

    m.header.frame_id = "temp_goal_pose"
    m.child_frame_id = "temp_wrist_pose"
    m.transform.translation.x = t.x
    m.transform.translation.y = t.y
    m.transform.translation.z = t.z
    m.transform.rotation.x = t.qx
    m.transform.rotation.y = t.qy
    m.transform.rotation.z = t.qz
    m.transform.rotation.w = t.qw
    tree.setTransform(m)

    ps_wrist = geometry_msgs.msg.PoseStamped()
    ps_wrist.header.frame_id = "temp_wrist_pose"
    ps_wrist.pose.orientation.w = 1.0

    ps_new = tree.transformPose(ps.header.frame_id, ps_wrist)

    print("New pose:")
    print(str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z))
    print(str(ps_new.pose.orientation.x) + ", " + str(ps_new.pose.orientation.y)  + ", " + str(ps_new.pose.orientation.z)  + ", " + str(ps_new.pose.orientation.w))

    return ps_new

  def set_transformations(self, tree):
    '''This sets up a TF tree for testing.'''

    m = geometry_msgs.msg.TransformStamped()
    m.header.frame_id = "world"
    m.child_frame_id = "robot_tool0"
    m.transform.translation.z = 5.0
    m.transform.rotation.w = 1.0
    tree.setTransform(m)

    self.points = [ [0.0,0.0,1.0], [0.0,0.0,1.0], [0.0,0.0,1.0],
                [0.0,1.0,0.0], [0.0,1.0,0.0], [0.0,1.0,0.0],
                [1.0,0.0,0.0], [1.0,0.0,0.0], [1.0,0.0,0.0],
                [1.0,0.0,1.0], [1.0,0.0,1.0], [1.0,0.0,1.0],
                [0.0,1.0,2.0], [0.0,1.0,2.0], [0.0,1.0,2.0]]
    self.rpys = [ [pi, pi*45/180, pi/2], [pi/2, pi, pi*45/180], [pi*45/180, pi/2, pi], 
                [0, pi*555/180, pi/2], [pi/2, 0, pi*555/180], [pi*555/180, pi/2, 0],
                [pi*30/180, pi*45/180, pi/2], [pi/2, pi*30/180, pi*45/180], [pi*45/180, pi/2, pi*30/180],
                [0, pi*15/180, 0], [0, 0, pi*15/180], [pi*15/180, 0, 0],
                [pi/2, pi/2, pi/2], [pi, pi, pi], [2*pi, 2*pi, 2*pi] ]

    for i in range(len(self.points)):
        m.transform.translation = geometry_msgs.msg.Point(*self.points[i])
        m.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(*self.rpys[i]))
        m.child_frame_id = "frame" + str(i)
        tree.setTransform(m)

    m.header.frame_id = "frame5"
    for i in range(len(self.points)):
        m.transform.translation = geometry_msgs.msg.Point(*self.points[i])
        m.transform.rotation = geometry_msgs.msg.Quaternion(*tf_transformations.quaternion_from_euler(*self.rpys[i]))
        m.child_frame_id = "frame" + str(i + len(self.points))
        tree.setTransform(m)
    return  

  def test_transformations(self, tree):
    ps = geometry_msgs.msg.PoseStamped()
    ps.pose.orientation.w = 1.0

    for i in range(len(self.points) * 2):
        ps.header.frame_id = "frame"+str(i)
        ps_new = tree.transformPose("world", ps)
        print("Pose nr. " + str(i) + ": " \
                + str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z) + "; " \
                + str(ps_new.pose.orientation.x) + ", " + str(ps_new.pose.orientation.y)  + ", " + str(ps_new.pose.orientation.z)  + ", " + str(ps_new.pose.orientation.w))

    ps.header.frame_id = "world"
    ps.pose.position.z = 8.0
    ps_new = self.transformTargetPoseFromTipLinkToEE(tree, ps, "robot", "frame0")
    print("Pose nr. " + str(len(self.points) * 2) + ": " \
                + str(ps_new.pose.position.x) + ", " + str(ps_new.pose.position.y)  + ", " + str(ps_new.pose.position.z) + "; " \
                + str(ps_new.pose.orientation.x) + ", " + str(ps_new.pose.orientation.y)  + ", " + str(ps_new.pose.orientation.z)  + ", " + str(ps_new.pose.orientation.w))
    return

if __name__ == '__main__':
  c = TFTest()
  tree = tf.Transformer()
  c.set_transformations(tree)
  c.test_transformations(tree)
  print("============ Done!")
  
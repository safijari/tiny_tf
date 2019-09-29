from tf import *
import numpy as np
import transformations as tft
from collections import namedtuple
import geometry_msgs


class Transformer(TFTree):
    """
    This class implements the same interfaces as the ROS tf.TransformListener().
    """
    def __init__(self):
        super(Transformer, self).__init__()

    def setTransform(self, transform_stamped):
        """
        For geometry_msgs.msg.TransformStamped
        """
        xform = Transform(transform_stamped.transform.translation.x,
            transform_stamped.transform.translation.y,
            transform_stamped.transform.translation.z,
            transform_stamped.transform.rotation.x,
            transform_stamped.transform.rotation.y,
            transform_stamped.transform.rotation.z,
            transform_stamped.transform.rotation.w)
        parent = transform_stamped.header.frame_id
        child = transform_stamped.child_frame_id
        self.add_transform(parent, child, xform)

    def transformPoint(self, target_frame, point_stamped):
        """
        point_stamped is a geometry_msgs.msg.PointStamped object.
        Returns a PointStamped transformed to target_frame.
        """
        t = self.lookup_transform(point_stamped.header.frame_id, target_frame)
        p = self.transform_point(point_stamped.point.x, point_stamped.point.y, point_stamped.point.z, target_frame, point_stamped.header.frame_id)
        ps_out = geometry_msgs.msg.PointStamped()
        ps_out.header.frame_id = target_frame
        ps_out.point.x = p[0]
        ps_out.point.y = p[1]
        ps_out.point.z = p[2]
        return ps_out

    def transformPose(self, target_frame, pose_stamped):
        """
        pose_stamped is a geometry_msgs.msg.PoseStamped object
        Returns a PoseStamped transformed to target_frame.
        """
        t = self.lookup_transform(pose_stamped.header.frame_id, target_frame)
        p = self.transform_pose(pose_stamped.pose.position.x, pose_stamped.pose.position.y, pose_stamped.pose.position.z, 
                                    pose_stamped.pose.orientation.x, pose_stamped.pose.orientation.y, pose_stamped.pose.orientation.z, pose_stamped.pose.orientation.w, 
                                    target_frame, pose_stamped.header.frame_id)
        ps_out = geometry_msgs.msg.PoseStamped()
        ps_out.header.frame_id = target_frame
        ps_out.pose.position.x = p[0]
        ps_out.pose.position.y = p[1]
        ps_out.pose.position.z = p[2]
        ps_out.pose.orientation.x = p[3]
        ps_out.pose.orientation.y = p[4]
        ps_out.pose.orientation.z = p[5]
        ps_out.pose.orientation.w = p[6]
        return ps_out

    def lookupTransform(self, base_frame, target_frame):
        """
        Returns a TransformStamped from base_frame to target_frame
        """
        # TODO
        # t = geometry_msgs.msg.TransformStamped()
        return self.lookup_transform(base_frame, target_frame)
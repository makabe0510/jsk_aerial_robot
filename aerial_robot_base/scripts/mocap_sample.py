#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PoseStamped

# グローバルに最新のPoseを保持
latest_pose = None

def pose_callback(msg):
    """
    /quadrotor/mocap/pose からPoseStampedメッセージを受け取るコールバック
    """
    global latest_pose
    latest_pose = msg

def main():
    rospy.init_node('quadrotor_pose_reader', anonymous=True)

    # サブスクライバの作成
    rospy.Subscriber('/quadrotor/mocap/pose', PoseStamped, pose_callback)

    rate = rospy.Rate(10)  # 10 Hz

    rospy.loginfo("quadrotor_pose_reader node started. Waiting for /quadrotor/mocap/pose ...")

    while not rospy.is_shutdown():
        if latest_pose is not None:
            # 1秒ごとに最新のPoseを読み出して表示
            p = latest_pose.pose.position
            o = latest_pose.pose.orientation
            rospy.loginfo(
                "time: %.3f, position: [%.3f, %.3f, %.3f], orientation: [%.3f, %.3f, %.3f, %.3f]" %
                (latest_pose.header.stamp.to_sec(),
                 p.x, p.y, p.z,
                 o.x, o.y, o.z, o.w)
            )
        else:
            rospy.loginfo("Waiting for first PoseStamped message...")

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

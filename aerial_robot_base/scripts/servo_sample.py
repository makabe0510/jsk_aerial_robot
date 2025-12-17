#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from spinal.msg import ServoControlCmd

def main():
    rospy.init_node('servo_target_publisher_toggle')

    pub = rospy.Publisher(
        '/quadrotor/servo/target_states',
        ServoControlCmd,
        queue_size=10
    )

    rate = rospy.Rate(0.5)  # 0.5 Hz = 2秒ごと

    angles = [7500, 7600]
    idx = 0

    rospy.loginfo("Publishing alternating servo commands (7500 <-> 7600) at 1 Hz")

    while not rospy.is_shutdown():
        msg = ServoControlCmd()
        msg.index = [0]
        msg.angles = [angles[idx]]

        pub.publish(msg)

        rospy.loginfo(f"Published angle: {angles[idx]}")

        idx = (idx + 1) % 2
        rate.sleep()

if __name__ == '__main__':
    main()

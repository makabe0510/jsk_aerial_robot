#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from spinal.msg import ServoTorqueCmd

def main():
    rospy.init_node('servo_torque_toggle_publisher')

    pub = rospy.Publisher(
        '/quadrotor/servo/torque_enable',
        ServoTorqueCmd,
        queue_size=10
    )

    rate = rospy.Rate(0.5)  # 0.5 Hz = 2秒ごと

    torque_values = [0, 1]
    idx = 0

    rospy.loginfo("Publishing torque_enable toggle (0 <-> 1) every 2 seconds")

    while not rospy.is_shutdown():
        msg = ServoTorqueCmd()
        msg.index = [0]
        msg.torque_enable = [torque_values[idx]]

        pub.publish(msg)
        rospy.loginfo(f"Published torque_enable: {torque_values[idx]}")

        idx = (idx + 1) % 2
        rate.sleep()

if __name__ == '__main__':
    main()

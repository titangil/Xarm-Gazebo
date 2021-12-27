#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def pubjoint():
	pub = rospy.Publisher('joint_states', JointState, queue_size=10)
	rospy.init_node('joint_state_publisher')
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		hello_str = JointState()
		hello_str.header = Header()
		hello_str.header.stamp = rospy.Time.now()
		hello_str.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5']
		hello_str.position = [0.6, 0.5418, -1.7297, -3.1017, 0.6]
		hello_str.velocity = []
		hello_str.effort = []
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
    try:
        pubjoint()
    except rospy.ROSInterruptException:
        pass

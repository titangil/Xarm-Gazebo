#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Header
import time


def pubjoint1(x):
	pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
	
	
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)
	
def pubjoint2(x):
	pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=1)
	
	
	
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)

def pubjoint3(x):
	pub = rospy.Publisher('/rrbot/joint3_position_controller/command', Float64, queue_size=10)
	
	#rate = rospy.Rate(100) # 10hz
	#while not rospy.is_shutdown():
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)
	#rate.sleep()

def pubjoint4(x):
	pub = rospy.Publisher('/rrbot/joint4_position_controller/command', Float64, queue_size=10)
	

	#while not rospy.is_shutdown():
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)
	#rate.sleep()

def pubjoint5(x):
	pub = rospy.Publisher('/rrbot/joint5_position_controller/command', Float64, queue_size=10)
	
	#rate = rospy.Rate(100) # 10hz
	#while not rospy.is_shutdown():
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)
	#rate.sleep()

def pubjoint6(x):
	pub = rospy.Publisher('/rrbot/joint6_position_controller/command', Float64, queue_size=10)
	
	#rate = rospy.Rate(100) # 10hz
	#while not rospy.is_shutdown():
	hello_str = Float64()
	hello_str.data = (x)

	pub.publish(hello_str)
	#rate.sleep()
#--------------------------------------
def grip_close():
	pubjoint5(-0.027)
	pubjoint6(0.04)


def grip_open():
	pubjoint5(0)
	pubjoint6(0.0)
#--------------------------------------

def defaultpos():
	pubjoint1(-0.6)
	pubjoint2(-0.09)
	pubjoint3(0)
	pubjoint4(-0.8)
#------------------------------
def fourthground_d():
	pubjoint1(0.2)
	pubjoint2(-0.09)
	pubjoint3(0)
	pubjoint4(-0.8)

def fourthground():
	pubjoint1(0.2)
	pubjoint2(-0.39)
	pubjoint3(-0.76)
	pubjoint4(-0.8)


def fourthblockpose():
	pubjoint1(-0.6)
	pubjoint2(-0.09)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def fourthblockdrop():
	pubjoint1(-0.6)
	pubjoint2(-0.035)
	pubjoint3(-0.76)
	pubjoint4(-0.8)


def fourthblockpose_offset():
	pubjoint1(-0.6)
	pubjoint2(-0.11)
	pubjoint3(-0.76)
	pubjoint4(-0.8)




#---------------------------------

def thirdground_d():
	pubjoint1(0.6)
	pubjoint2(-0.09)
	pubjoint3(0)
	pubjoint4(-0.8)

def thirdground():
	pubjoint1(0.6)
	pubjoint2(-0.39)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def thirdblockpose():

	pubjoint1(-0.6)
	pubjoint2(-0.19)
	pubjoint3(-0.76)
	pubjoint4(-0.8)


def thirdblockdrop():
	pubjoint1(-0.6)
	pubjoint2(-0.365)
	pubjoint3(-0.3)
	pubjoint4(-1.21)

#---------------------------------------

def secondground_d():
	pubjoint1(1)
	pubjoint2(-0.09)
	pubjoint3(0)
	pubjoint4(-0.8)

def secondground():
	pubjoint1(1)
	pubjoint2(-0.39)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def secondblockpose():
	pubjoint1(-0.6)
	pubjoint2(-0.29)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def secondblockdrop():
	pubjoint1(-0.6)
	pubjoint2(-0.23)
	pubjoint3(-0.8)
	pubjoint4(-0.8)

#---------------------------------

def firstground_d():
	pubjoint1(1.4)
	pubjoint2(-0.09)
	pubjoint3(0)
	pubjoint4(-0.8)

def firstground():
	pubjoint1(1.4)
	pubjoint2(-0.39)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def firstblockpose():
	pubjoint1(-0.6)
	pubjoint2(-0.39)
	pubjoint3(-0.76)
	pubjoint4(-0.8)

def firstblockdrop():
	pubjoint1(-0.6)
	pubjoint2(-0.23)
	pubjoint3(-0.8)
	pubjoint4(-0.8)




	
if __name__ == '__main__':
	while not rospy.is_shutdown():
		
		rospy.init_node('joint_state_publisher')


       #----------------------
		
		grip_open()
		defaultpos()				#start up
		time.sleep(3)

		#------------------------
		
		fourthblockpose()
		time.sleep(10)
		grip_close()
		time.sleep(0.1)
		defaultpos()
		#fourthblockpose_offset()
		time.sleep(1)
		defaultpos()
		time.sleep(7)
		fourthground_d()
		time.sleep(2)
		fourthground()         #  Pick and Place 4th block
		time.sleep(6)
		grip_open()
		time.sleep(2)
		fourthground_d()
		time.sleep(6)
		defaultpos()
		time.sleep(2)
		#-------------------
		thirdblockpose()
		time.sleep(10)
		grip_close()
		time.sleep(0.1)
		defaultpos()
		time.sleep(7)
		thirdground_d()
		time.sleep(4)
		thirdground()         #  Pick and Place 3rd block
		time.sleep(6)
		grip_open()
		time.sleep(2)
		thirdground_d()
		time.sleep(6)
		defaultpos()
		time.sleep(2)
		#--------------------
		secondblockpose()
		time.sleep(10)
		grip_close()
		time.sleep(0.1)
		defaultpos()
		time.sleep(7)
		secondground_d()
		time.sleep(3)
		secondground()         #  Pick and Place 2nd block
		time.sleep(6)
		grip_open()
		time.sleep(2)
		secondground_d()
		time.sleep(6)
		defaultpos()
		time.sleep(3)
		#---------------------
		firstblockpose()
		time.sleep(10)
		grip_close()
		time.sleep(1)
		defaultpos()
		time.sleep(7)
		firstground_d()
		time.sleep(4)
		firstground()         #  Pick and Place 1st block
		time.sleep(6)
		grip_open()
		time.sleep(2)
		firstground_d()
		time.sleep(6)
	

		#--------------------------
		
		thirdground_d()
		time.sleep(3)
		thirdground()
		time.sleep(9)
		grip_close()
		time.sleep(2)
		thirdground_d()
		time.sleep(5)
		defaultpos()
		time.sleep(5)
		firstblockpose()
		time.sleep(10)
		grip_open()
		time.sleep(2)

		defaultpos()
		time.sleep(7)
		firstground_d()
		time.sleep(4)
		firstground()
		time.sleep(9)
		grip_close()
		time.sleep(2)
		firstground_d()
		time.sleep(7)
		defaultpos()
		time.sleep(7)
		secondblockdrop()
		time.sleep(9)
		grip_open()
		time.sleep(2)
		
		defaultpos()
		time.sleep(7)
		fourthground_d()
		time.sleep(4)
		#grip_open()
		fourthground()
		time.sleep(9)
		grip_close()
		time.sleep(2)
		fourthground_d()
		time.sleep(7)
		defaultpos()
		time.sleep(5)
		fourthblockdrop()
		time.sleep(4)
		thirdblockdrop()
		time.sleep(9)
		grip_open()
		time.sleep(2)

		defaultpos()
		time.sleep(7)
		secondground_d()
		time.sleep(4)
		secondground()
		time.sleep(9)
		grip_close()
		time.sleep(2)
		secondground_d()
		time.sleep(7)
		defaultpos()
		time.sleep(5.5)
		fourthblockdrop()
		time.sleep(9)
		grip_open()
		time.sleep(2)
		defaultpos()
		time.sleep(4)
		break
	
		fourthblockdrop()

		

		
	
		
		#thirdblockdrop()
		#grip_open()
	
		
		
 
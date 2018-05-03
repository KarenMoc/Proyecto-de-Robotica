#!/usr/bin/env python

#ROS libraries
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Vector3

import socket
import time
import math
import decimal

#Node to process the incoming data from the control to send valuable packets to the TcpServer

currLeft = 0
currRight = 0
pub = 0
buttonX = False
joySticksDirection = 1

def callback(data):
	global currLeft
	global currRight
	global joySticksDirection
	global buttonX
	diffLeft = abs(currLeft-data.axes[1]);
	diffRight = abs(currRight-data.axes[4]);
	
	if(data.buttons[0]):
		if(not buttonX):
			buttonX = True
			joySticksDirection += 1;
			joySticksDirection &= 1;
	else:
		buttonX = False
	
	if(joySticksDirection):
		vector_message = Vector3(data.axes[1],-data.axes[4],0)
	else:
		vector_message = Vector3(-data.axes[4],data.axes[1],0)
	
	if ((diffLeft >= 0.1 or diffRight >= 0.1) or (data.axes[1] == 0.0 and diffLeft) or (data.axes[4] == 0.0 and diffRight)
	or (abs(data.axes[1]) == 1.0 and diffLeft) or (abs(data.axes[4]) == 1.0 and diffRight)):
		pub.publish(vector_message)
		currLeft = data.axes[1]
		currRight = data.axes[4]
		
def talker():
	global pub
	pub = rospy.Publisher('filter_joy', Vector3, queue_size=1)
    
def listener():

	rospy.Subscriber('joy', Joy, callback)
	rospy.init_node('Handy_joy', anonymous=True)

	#rate = rospy.Rate(10) #10Hz

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	talker()
	listener()

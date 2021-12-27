
'''import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge
class Follower:


    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('rrbot/camera1/image_raw',
                                            Image, self.image_callback)
    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        cv2.imshow("wirndow", image)
        cv2.waitKey(3)

while True:
    rospy.init_node('follower')
    follower = Follower()

    
    
rospy.spin()'''
#!/usr/bin/env python
import rospy
import sys
import cv2 as cv
import numpy as np
import imutils
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from varname import nameof



def process_image(msg):
    bridge = CvBridge()

    b_cx = 2000
    b_cy = 2000
    y_cx = 2000
    y_cy = 2000
    r_cx = 2000
    r_cy = 2000
    g_cx = 2000
    g_cy = 2000
    frame = bridge.imgmsg_to_cv2(msg, "bgr8")

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    
    lower_y = np.array([15,10,10]) #yac
    upper_y = np.array([40,255,255]) #xzb

    lower_g = np.array([40,20,40]) #yac
    upper_g = np.array([70,255,255]) #xzb

    lower_r = np.array([0,30,110]) #yac
    upper_r = np.array([13,255,255]) #xzb

    lower_b = np.array([90,60,0]) #yac
    upper_b = np.array([121,255,255]) #xzb
    
    mask_y = cv.inRange(hsv,lower_y,upper_y)
    mask_g = cv.inRange(hsv,lower_g,upper_g)
    mask_r = cv.inRange(hsv,lower_r,upper_r)
    mask_b = cv.inRange(hsv,lower_b,upper_b)

    cnst_y = cv.findContours(mask_y, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnst_y = imutils.grab_contours(cnst_y)

    cnst_g = cv.findContours(mask_g, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnst_g = imutils.grab_contours(cnst_g)

    cnst_r = cv.findContours(mask_r, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnst_r = imutils.grab_contours(cnst_r)

    cnst_b = cv.findContours(mask_b, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnst_b = imutils.grab_contours(cnst_b)

    for c in cnst_y:
        area = cv.contourArea(c)
        if area>500:
            cv.drawContours(frame, [c],-1, (0,255,0), 2)
           
            M = cv.moments(c)
            
            y_cx = int(M['m10']/M['m00'])
            y_cy = int(M['m01']/M['m00'])
            
            cv.circle(frame,(y_cx,y_cy),7,(255,255,255),-1)
            cv.putText(frame, "Yellow " +"x:{}".format(y_cx)+" y:{}".format(y_cy), (y_cx,y_cy), cv.FONT_HERSHEY_PLAIN, 2.5, (0,255,0))

    for c in cnst_g:
        area = cv.contourArea(c)
        if area>500:
            cv.drawContours(frame, [c],-1, (0,255,0), 2)
           
            M = cv.moments(c)
            
            g_cx = int(M['m10']/M['m00'])
            g_cy = int(M['m01']/M['m00'])
            
            cv.circle(frame,(g_cx,g_cy),7,(255,255,255),-1)
            cv.putText(frame,"Green " +"x:{}".format(g_cx)+" y:{}".format(g_cy), (g_cx,g_cy), cv.FONT_HERSHEY_PLAIN, 2.5, (0,255,0))

    for c in cnst_r:
        area = cv.contourArea(c)
        if area>500:
            cv.drawContours(frame, [c],-1, (0,255,0), 2)
           
            M = cv.moments(c)
            
            r_cx = int(M['m10']/M['m00'])
            r_cy = int(M['m01']/M['m00'])
            
            cv.circle(frame,(r_cx,r_cy),7,(255,255,255),-1)
            cv.putText(frame,"Red " +"x:{}".format(r_cx)+" y:{}".format(r_cy), (r_cx,r_cy), cv.FONT_HERSHEY_PLAIN, 2.5, (0,255,0))

    for c in cnst_b:
        area = cv.contourArea(c)
        if area>500:
            cv.drawContours(frame, [c],-1, (0,255,0), 2)
           
            M = cv.moments(c)
            
            b_cx = int(M['m10']/M['m00'])
            b_cy = int(M['m01']/M['m00'])
            
            cv.circle(frame,(b_cx,b_cy),7,(255,255,255),-1)
            cv.putText(frame,"Blue " +"x:{}".format(b_cx)+" y:{}".format(b_cy), (b_cx,b_cy), cv.FONT_HERSHEY_PLAIN, 2.5, (0,255,0))
            #print(cx,cy)

    '''b =(y_cy,g_cy,r_cy,b_cy)
    a = sorted(b)
    c = nameof(b)'''
    if b_cy > g_cy and g_cy > r_cy and r_cy > y_cy and y_cy >400:
        cv.putText(frame,"SUCCESS", (230,300), cv.FONT_HERSHEY_PLAIN, 5, (0,255,0),5)
    else:
        cv.putText(frame,"NOT ARRANGED", (200,300), cv.FONT_HERSHEY_PLAIN, 5, (0,0,255),5)
    #print("Yellow: ",y_cx,y_cy,"Green: ",g_cx,g_cy,"Red: ",r_cx,r_cy,"Blue: ",b_cx,b_cy)
    cv.namedWindow("image",cv.WINDOW_FREERATIO)
    cv.imshow("image",frame)
    
    if cv.waitKey(1)==13:
        cv.destroyAllWindows
    #cv.waitKey(50)
if __name__ == '__main__':
    while not rospy.is_shutdown():
        rospy.init_node('image_sub')
        rospy.loginfo('image_sub node started')
        rospy.Subscriber("/rrbot/camera1/image_raw", Image, process_image)

        rospy.spin()

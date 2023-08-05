#!/usr/bin/env python3
# license removed for brevity
import rospy
import random 
from geometry_msgs.msg import Vector3

def talker():
    pub = rospy.Publisher('velocity_data', Vector3, queue_size=10)
    rospy.init_node('velocity_generator', anonymous=True)
    rate = rospy.Rate(5) # 5hz
    while not rospy.is_shutdown():
        vel_linear = Vector3(x=random.uniform(0, 10), y=random.uniform(0, 10), z=random.uniform(0, 10))
        vel_angular = Vector3(x=random.uniform(0, 10), y=random.uniform(0, 10), z=random.uniform(0, 10))
        pub.publish(vel_angular)
        pub.publish(vel_linear)
        rospy.loginfo(vel_angular)
        rospy.loginfo(vel_linear)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
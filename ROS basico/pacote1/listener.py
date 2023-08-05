#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64

def callback(data):
    vel_linear = (data.x**2 + data.y**2 +data.z**2)**0.5
    vel_angular = (data.x**2 + data.y**2 + data.z**2)**0.5

    linear_pub = rospy.Publisher('linear_velocity', Float64, queue_size=10)
    angular_pub = rospy.Publisher('angular_velocity', Float64, queue_size=10)
    linear_pub.publish(vel_linear)
    angular_pub.publish(vel_angular)
    rospy.loginfo(vel_angular)
    rospy.loginfo(vel_linear)

def calculador_vel():
    rospy.init_node('calculador_vel', anonymous=True)
    rospy.Subscriber("velocity_data", Vector3, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    calculador_vel()
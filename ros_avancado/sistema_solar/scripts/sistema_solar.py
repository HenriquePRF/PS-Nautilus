#!/usr/bin/env python3

import rospy
import tf2_ros
import math
from geometry_msgs.msg import TransformStamped

def main():
    rospy.init_node('sistema_solar_sim') 

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    tf_broadcaster = tf2_ros.TransformBroadcaster()

    # Pega parametros do arquivo .yaml
    NOME_ASTRO = rospy.get_param('NOME_ASTRO')
    NOME_PLANETA = rospy.get_param('NOME_PLANETA')
    NOME_SATELITE = rospy.get_param('NOME_SATELITE')
    RAIO_PLANETA = rospy.get_param('RAIO_PLANETA')
    RAIO_SATELITE = rospy.get_param('RAIO_SATELITE')
    VELOCIDADE_PLANETA = rospy.get_param('VELOCIDADE_PLANETA')
    VELOCIDADE_SATELITE = rospy.get_param('VELOCIDADE_SATELITE')

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown(): 
        try:
            current_time = rospy.Time.now().to_sec()  # Tempo atual em segundos
            # Simula a revolucao do planeta em torno do astro
            revolucao_planeta = TransformStamped()
            revolucao_planeta.header.stamp = rospy.Time.now()
            revolucao_planeta.header.frame_id = NOME_ASTRO
            revolucao_planeta.child_frame_id = NOME_PLANETA
            # Mantém o ângulo dentro de uma volta completa 
            angle_planeta = current_time * VELOCIDADE_PLANETA % (2 * math.pi)
            revolucao_planeta.transform.translation.x = RAIO_PLANETA * math.cos(angle_planeta)
            revolucao_planeta.transform.translation.y = RAIO_PLANETA * math.sin(angle_planeta)
            revolucao_planeta.transform.rotation.w = 1.0

            # Simula a revolucao do satelite em torno do planeta
            revolucao_satelite = TransformStamped()
            revolucao_satelite.header.stamp = rospy.Time.now()
            revolucao_satelite.header.frame_id = NOME_PLANETA
            revolucao_satelite.child_frame_id = NOME_SATELITE
            # Mantém o ângulo dentro de uma volta completa 
            angle_satelite = current_time * VELOCIDADE_SATELITE % (2 * math.pi)
            revolucao_satelite.transform.translation.x = RAIO_SATELITE * math.cos(angle_satelite)
            revolucao_satelite.transform.translation.y = RAIO_SATELITE * math.sin(angle_satelite)
            revolucao_satelite.transform.rotation.w = 1.0

            # Envia os dados do planeta e satelite
            tf_broadcaster.sendTransform(revolucao_planeta)
            tf_broadcaster.sendTransform(revolucao_satelite)

            rate.sleep() # Garante 10hz

        except (rospy.ROSInterruptException, tf2_ros.TransformException):
            pass

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

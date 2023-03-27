#!/usr/bin/env python

import rospy
from dofbot_driver.srv import *
from dofbot_driver.msg import *

def main():
    # 노드 초기화
    rospy.init_node('dofbot_example', anonymous=True)

    # 서비스 프록시 생성
    joint_service = rospy.ServiceProxy('/dofbot_driver/joint_cmd', JointCmd)
    gripper_service = rospy.ServiceProxy('/dofbot_driver/gripper_cmd', GripperCmd)

    # 메시지 생성
    joint_cmd = JointCmdRequest()
    joint_cmd.joint_name = ["joint1", "joint2", "joint3", "joint4", "joint5", "joint6"]
    joint_cmd.velocity = [20, 20, 20, 20, 20, 20]
    joint_cmd.position = [0, 0, 0, 0, 0, 0]

    gripper_cmd = GripperCmdRequest()
    gripper_cmd.position = 8000
    gripper_cmd.velocity = 300

    # 동작
    print('DOFBOT을 초기 위치로 이동시킵니다.')
    joint_service(joint_cmd)
    rospy.sleep(3)

    print('그리퍼를 닫습니다.')
    gripper_service(gripper_cmd)
    rospy.sleep(3)

    print('DOFBOT을 다시 초기 위치로 이동시킵니다.')
    joint_cmd.position = [0, 30, 60, 0, 0, 0]
    joint_service(joint_cmd)
    rospy.sleep(3)

    print('그리퍼를 엽니다.')
    gripper_cmd.position = 14000
    gripper_service(gripper_cmd)
    rospy.sleep(3)

    print('DOFBOT을 초기 위치로 이동시킵니다.')
    joint_cmd.position = [0, 0, 0, 0, 0, 0]
    joint_service(joint_cmd)
    rospy.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

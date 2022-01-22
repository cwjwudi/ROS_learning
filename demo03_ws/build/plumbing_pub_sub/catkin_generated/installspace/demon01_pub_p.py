#!/usr/bin/env python2
# coding=utf-8

import rospy
from std_msgs.msg import String # 发布消息类型

"""
    使用Python 实现消息发布：
        1.导入包
        2.初始化ros节点
        3.创建发布者对象
        4.编写发布逻辑并发布数据
"""


if __name__ == "__main__":
    #    2.初始化ros节点
    rospy.init_node("talker_p") #传入节点名称
    #    3.创建发布者对象
    pub = rospy.Publisher("che", String,queue_size=10)
    #    4.编写发布逻辑并发布数据
    # 创建数据
    msg = String()
    count = 0  #计数器 
    rate = rospy.Rate(1)
    rospy.sleep(1)  # 给充足的时间注册
    # 使用循环发布数据
    while not rospy.is_shutdown():
        msg.data = "hello" + str(count)
        pub.publish(msg)
        rate.sleep()
        rospy.loginfo("写出的数据:%s",msg.data)
        count += 1
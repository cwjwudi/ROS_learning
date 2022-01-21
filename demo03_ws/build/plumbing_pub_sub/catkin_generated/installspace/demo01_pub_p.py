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


if __name__ == "__mian__":
    #    2.初始化ros节点
    rospy.init_node("sanDai") #传入节点名称
    #    3.创建发布者对象
    pub = rospy.Publisher("che", String,queue_size=10)
    #    4.编写发布逻辑并发布数据
    # 创建数据
    msg = String()
    # 使用循环发布数据
    while not rospy.is_shutdown():
        msg.data = "hello"
        pub.publish(msg)
        rospy.loginfo("写出的数据:%s",msg.data)
    
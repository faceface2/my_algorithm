#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : pub.py
@Time    : 2019/7/2 14:20
@Author  : hrx
@Email   : hurx1116@gmail.com
"""

"""
topic模式跟direct差不多，只是把type改一下就行。

direct是把固定的routing_key跟queue绑定，topic是把模糊的routing_key跟queue绑定
"""
import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=credentials)  # 默认端口5672，可不写
)
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')  # 1、改成type='direct'
# 2、默认发送的消息级别为info，可以带参数，warning error等
severity = "info"

message = "Hello World!"
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,  # 3、把上面的消息发到这个queue中
                      body=message)
print("send :", message)
connection.close()

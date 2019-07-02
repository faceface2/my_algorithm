#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : pub.py
@Time    : 2019/7/2 14:03
@Author  : hrx
@Email   : hurx1116@gmail.com
"""
import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=credentials)  # 默认端口5672，可不写
)
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')  # 1、改成type='topic'
# 2、改默认格式为*.info
routing_key = "anonymous.info"

message = "Hello World!"
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print("send :", message)
connection.close()

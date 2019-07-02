#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : sub.py
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
                         exchange_type='topic')  # 3、改topic的类型
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# 4、改为binding_keys 就变量名称改了
binding_keys = ['error', '*.info', 'warning']
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)
print("Wait for logs...")


def callback(ch, method, properties, body):
    print("received:", method.routing_key, body)


channel.basic_consume(queue_name,
                      callback,
                      auto_ack=True)
channel.start_consuming()

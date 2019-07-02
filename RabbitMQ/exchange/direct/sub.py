#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : sub.py
@Time    : 2019/7/2 14:20
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
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')  # 4、改exchange的类型
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# 5、启动订阅端的时候，severities存放订阅端订阅了哪些级别
#    然后用routing_key把这些级别绑定到queue上，这些queue就放这些级别的消息
severities = ['info', 'error']

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
print("Wait for logs...")


# 6、使用method.routing_key可以得到消息的级别
def callback(ch, method, properties, body):
    print("received:", method.routing_key, body)


channel.basic_consume(
    queue_name,
    callback,
    auto_ack=True)
channel.start_consuming()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : subscriber.py
@Time    : 2019/7/1 8:34
@Author  : hrx
@Email   : hurx1116@gmail.com
"""

import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=credentials)  # 默认端口5672，可不写
)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare('', exclusive=True)
# 获取随机的queue名字
queue_name = result.method.queue
print("random queuename:", queue_name)

channel.queue_bind(exchange='logs',  # queue绑定到转发器上
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
    queue_name,
    callback,
    auto_ack=True)

channel.start_consuming()

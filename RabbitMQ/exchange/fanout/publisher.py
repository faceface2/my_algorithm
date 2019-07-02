#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : publisher.py
@Time    : 2019/7/1 8:33
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
# 注意：这里是广播，不需要声明queue
channel.exchange_declare(exchange='logs',  # 声明广播管道
                         exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',  # 注意此处空，必须有
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

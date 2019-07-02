#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : server.py
@Time    : 2019/7/1 9:33
@Author  : hrx
@Email   : hurx1116@gmail.com
"""

import pika
import time


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
        exchange='',  # 把执行结果发回给客户端
        routing_key=props.reply_to,  # 客户端要求返回想用的queue
        # 返回客户端发过来的correction_id 为了让客户端验证消息一致性
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 任务完成，告诉客户端


if __name__ == '__main__':
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, virtual_host='/', credentials=credentials)
        # 默认端口5672，可不写
    )
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')  # 声明一个rpc_queue ,

    channel.basic_qos(prefetch_count=1)
    # 在rpc_queue里收消息,收到消息就调用on_request
    channel.basic_consume('rpc_queue', on_request)
    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

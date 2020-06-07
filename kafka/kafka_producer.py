#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from confluent_kafka import Producer


p = Producer({'bootstrap.servers': '192.168.198.133:29092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]: {}'.format(msg.topic(), msg.partition(), msg.value().decode('utf-8')))


for data in ["data%d" % i for i in range(20)]:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    # p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)
    # 向指定分区(partition)生产数据
    p.produce('mytopic', data.encode('utf-8'), partition=0, callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()

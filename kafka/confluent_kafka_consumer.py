#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
from confluent_kafka import Consumer
from confluent_kafka.cimpl import TopicPartition

"""
earliest
当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，从头开始消费

latest
当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，消费新产生的该分区下的数据

none
topic各分区都存在已提交的offset时，从offset后开始消费；只要有一个分区不存在已提交的offset，则抛出异常
"""
c = Consumer({
    'bootstrap.servers': '192.168.198.133:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

# 配置向指定(partition)分区，指定分区内的偏移位置起 消费数据
# TopicPartition(topic[, partition][, offset])
tp = TopicPartition('mytopic', 0, 0)
c.assign([tp])
c.seek(tp)

# c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message {} [{}]: {}'.format(msg.topic(), msg.partition(), msg.value().decode('utf-8')))

c.close()
from rocketmq.client import Producer, Message

producer = Producer('PID-XXX')
producer.set_name_server_address('127.0.0.1:9876')
producer.start()

msg = Message('YOUR-TOPIC')
msg.set_keys('XXX')
msg.set_tags('XXX')
msg.set_body('XXXX')
ret = producer.send_sync(msg)
print(ret.status, ret.msg_id, ret.offset)
producer.shutdown()
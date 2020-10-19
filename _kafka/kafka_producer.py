import json

from kafka import KafkaProducer

# 生产端
producer = KafkaProducer(bootstrap_servers=['192.168.3.222:29092'],
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))
future = producer.send('my_topic', key=b'my_data', value={"name": "willi", "email": "willi@163.com"}, partition=0)

# 发送字符串类型的key和value
# 指定 key_serializer 和 value_serializer 为 str.encode,但消费者收到的还是字节字符串。
# 若想要消费者收到的为字符串类型，就需要解码操作，key_deserializer= bytes.decode
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'], key_serializer=str.encode, value_serializer=str.encode)
# future = producer.send('my_topic', key='key_3', value='value_3', partition=0)

result = future.get(timeout=10)  # future.get()函数等待单条消息发送完成或超时，经测试，必须有这个函数，不然发送不出去，或用time.sleep代替
print(result)

import json

from kafka import KafkaConsumer
from kafka import TopicPartition

# 消费端
# 常用参数配置：
#   consumer_timeout_ms：超时毫秒数，若不指定，默认一直循环等待接收；若指定，则超时返回，不再等待
#   value_deserializer：解码json数据。与生产端的value_serializer编码json数据相对应
consumer = KafkaConsumer('my_topic', group_id='group2', bootstrap_servers=['192.168.3.222:29092'],
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))
# 手动分配partition
# consumer = KafkaConsumer(bootstrap_servers=['192.168.3.222:29092'])
# consumer.assign([TopicPartition(topic='my_topic', partition=0)])
# 订阅多个topic
consumer.subscribe(topics=['my_topic', 'topic01'])
# 正则订阅一类topic
# consumer.subscribe(pattern='^topic.*')
for msg in consumer:
    print(msg)

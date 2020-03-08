### 引用自pyspider中的message_queue
https://github.com/binux/pyspider

### redis_queue.py 基于redis实现Queue
利用的list数据类型的RPUSH、LPOP操作实现的FIFO的队列  
可以通过更改RPUSH、RPOP操作实现LIFO队列  
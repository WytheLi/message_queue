import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

queue_name = 'queue'
channel.queue_declare(queue=queue_name, durable=True, auto_delete=True)

for i in range(100):
    message = "data%d" % i

    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sent %r" % message)

connection.close()

if __name__ == '__main__':
    pass

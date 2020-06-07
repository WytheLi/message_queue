import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

queue_name = "queue"
channel.queue_declare(queue=queue_name, durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(" [x] Done")

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

if __name__ == '__main__':
    pass

import time
import pika


def message_received(ch,method,properties,body):
    print(f'Consumver 2 recevied message{body}')

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
queue = channel.queue_declare(queue='',exclusive=True)

#channel.basic_qos(prefetch_count=1)
channel.queue_bind(exchange='PubSub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue,on_message_callback=message_received)
channel.start_consuming()
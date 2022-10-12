import time
import pika


def message_received(ch,method,properties,body):
    print(f'Routing Consumer 2 recevied message{body}')

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
queue = channel.queue_declare(queue='',exclusive=True)

channel.queue_bind(exchange='Routing', queue=queue.method.queue,routing_key='india')

channel.basic_consume(queue=queue.method.queue,on_message_callback=message_received)
channel.start_consuming()
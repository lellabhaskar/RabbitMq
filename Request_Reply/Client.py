import time
import pika
import uuid

def message_received(ch,method,properties,body):
    print(f'Client recevied message{body}')


connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='requestQueue')

channel.queue_declare(queue='replyQueue')

channel.basic_consume(queue='replyQueue',on_message_callback=message_received)

#id = str(uuid.uuid4())

channel.basic_publish(exchange='',routing_key='requestQueue',body='message from clinet',
                      properties=pika.BasicProperties(reply_to='replyQueue'))

channel.start_consuming()
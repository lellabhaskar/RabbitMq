import time
import pika


def message_received(ch,method,properties,body):
    print(f'Server recevied message{body}')
    ch.basic_publish('',routing_key=properties.reply_to,body='Here is your response')

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='requestQueue')

channel.basic_consume(queue='requestQueue',on_message_callback=message_received)

channel.start_consuming()

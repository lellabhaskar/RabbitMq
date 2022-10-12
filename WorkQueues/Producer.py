import time
import pika


connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='letterbox')
#message = 'Helalo World'
messageid = 1
while True:
    message =f'sending message {messageid}'
    channel.basic_publish(exchange='',routing_key='letterbox',body=message)
    print(message)
    time.sleep(2)
    messageid=messageid + 1


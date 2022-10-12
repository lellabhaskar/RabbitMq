import time
import pika     # pip install pika


connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='letterbox')
message = 'Helalo World'
while True:
    channel.basic_publish(exchange='',routing_key='letterbox',body=message)
    print('message sent successfully')
    time.sleep(2)


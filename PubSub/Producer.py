import time
import pika
from pika.exchange_type import ExchangeType

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
#channel.queue_declare(queue='letterbox')

#messageid = 1

while True:
    channel.exchange_declare(exchange='PubSub',exchange_type=ExchangeType.fanout)
    message =f'sending message for PubSub'
    channel.basic_publish(exchange='PubSub',routing_key='',body=message)
    print(message)
    time.sleep(2)
    #messageid=messageid + 1


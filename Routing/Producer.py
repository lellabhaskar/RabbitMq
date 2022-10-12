import time
import pika
from pika.exchange_type import ExchangeType

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()

channel.exchange_declare(exchange='Routing',exchange_type=ExchangeType.direct)

while True:
    #channel.exchange_declare(exchange='PubSub', exchange_type=ExchangeType.fanout)
    message =f'sending message for Routing'
    channel.basic_publish(exchange='Routing',routing_key='india',body=message)
    print(message)
    time.sleep(2)


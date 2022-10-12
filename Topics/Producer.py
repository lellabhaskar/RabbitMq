import time
import pika
from pika.exchange_type import ExchangeType

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()

channel.exchange_declare(exchange='Topic',exchange_type=ExchangeType.topic)

while True:
    message =f'sending message for Topic'
    channel.basic_publish(exchange='Topic',routing_key='asia.india.tcs',body=message)
    print(message)
    time.sleep(2)


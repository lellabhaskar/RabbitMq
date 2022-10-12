import time
import pika


def message_received(ch,method,properties,body):
    time.sleep(5)
    print(f' received {body}')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('message processed and acknowledged')

connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='lellerbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox',on_message_callback=message_received)
channel.start_consuming()
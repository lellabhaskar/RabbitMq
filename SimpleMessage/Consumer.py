import pika


def message_received(ch,method,properties,body):
    print('message received successfully')


connection_parms = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()
channel.queue_declare(queue='lellerbox')
channel.basic_consume(queue='letterbox',on_message_callback=message_received,auto_ack=True)
channel.start_consuming()
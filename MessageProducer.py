import pika

Docker_Connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = Docker_Connection.channel()

routing_key=input('Enter Routing Key: ')
Message= input('Enter Message: ')

channel.queue_declare(queue=(routing_key))
channel.basic_publish(exchange='',routing_key=(routing_key),body='(Message)')

Docker_Connection.close()
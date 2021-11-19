import pika
Docker_Connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = Docker_Connection.channel()

def main():
    Queue=input('Queue: ')

    channel.queue_declare(Queue)
    def callback(ch, method, properties, body):

        print("[*] A massage received %r" % body)

        with open("Message.txt", "a") as ths:      # To save the Headers and Message  at the the text file
            ths.write(str(body)+str(properties)+"\n")

    channel.basic_consume(queue=(Queue), on_message_callback=callback, auto_ack=True)

    print('[#] Waiting for messages.')
    channel.start_consuming()

main()

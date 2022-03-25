import queue
import pika 

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="192.168.31.240"))
channel = connection.channel()

channel.queue_decalare(queue="hello")
channel.basic_publish(exchange="", routing_key='hello', body='Hello World!')
print(" [x] Snet 'Hello world'")
connection.close()
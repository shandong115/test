import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#channel.basic_publish(exchange='',routing_key='face_in', body='hello, dayou')
strData = 'hello,dayou->'+str(time.time())
channel.basic_publish(exchange='face.in_exchange',routing_key='face.in_queue', body=strData)

channel.close

print("[x] Send msg ok:"+strData)

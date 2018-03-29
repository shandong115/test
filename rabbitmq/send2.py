import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#channel.basic_publish(exchange='',routing_key='face_in', body='hello, dayou')
strData = 'hello,dayou->'+str(time.time())
message = ' '.join(sys.argv[1:]) or strData
#channel.basic_publish(exchange='face.in_exchange',routing_key='face.in_queue', body=message)
channel.basic_publish(exchange='face.in_exchange',routing_key='', body=message)

channel.close

print("[x] Send msg ok:"+message)

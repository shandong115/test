# -*- coding: utf-8 -*-

import socket
import threading
import sys
import re
import base64
import json
import pika


def socket_service():
    try:
        # 创建 TCP Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字选项的值
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.22.159', 6666))
        s.listen(10)
    # 错误处理
    except socket.error as msg:
        print msg
        sys.exit(1)

    print 'Waiting connection...'

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target = deal_data, args = (conn, addr))
        # 开启线程
        t.start()


def sendMq(message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))   
	channel = connection.channel()
	channel.basic_publish(exchange='face.in_exchange',routing_key='', body=message) 
	channel.close
	print("[x] Send msg ok:")

def switch_data(data):
	jsonData = json.loads(data)
	tranType = jsonData['tran_type']
	print("tranType :%s"%(tranType))
	if tranType == "tran_add":
		sendMq(data)
	elif tranType == "tran_recognition":
		sendMq(data)
	else:
		print("unsupport tranType:%s"%(tranType))
"""	elif tranType == "tran_query" :
	elif tranType == "tran_delete" :
    elif tranType == "tran_recognition" :
	else:
		print("unsupport tranType :%s"%(tranType))
"""	


def deal_data(conn, addr):
    print 'Accept new connection from {0}'.format(addr)

    conn.send('Hi dayou, Welcome to the server!')

    while True:     
        print 'start receiving...'
        img_64 = ''
        dataa = ''
        
        while True:
            data = conn.recv(1024)

            if data != '':
                img_64 += data
            else:
				switch_data(img_64)
				img_64 = ''
				break

        print 'end receive...'
        conn.close()
        sys.exit()

if __name__ == '__main__':
    socket_service()

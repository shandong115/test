# -*- coding: utf-8 -*-

import socket
import sys
import base64
import time
import json

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.22.159', 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)

    print s.recv(1024)

    f = open(r'./3.jpg','rb')
    img_64 = base64.b64encode(f.read())
    f.close()

    ticks = time.time()
    dict_add = {'tran_type':'tran_add', 'image':img_64, 'name':'zhaodan', 'timestamp':str(ticks)}
    dict_recog = {'tran_type':'tran_recognition', 'image':img_64}
    data = json.dumps(dict_recog)

    while True:
        #s.send(img_64)
        s.send(data)
        #s.send('timestamp' + str(ticks))
		#s.send('name:dayou')
        s.close()
        break

if __name__ == '__main__':
    socket_client()
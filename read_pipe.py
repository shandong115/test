import os
import time
from mytime import *

file_path = "/tmp/face_file.pipe"

def read_pipe():
	ss=''
	rf = None
	while True:
		if rf == None:
			print("before open file:"+str(nowTime()))
			rf = os.open(file_path, os.O_RDONLY)
			print("opened file",rf)
			print("after open file:"+str(nowTime()))
		s = os.read(rf, 1024)
		ss += s
		if len(s)==0:
			print("closed pipe:"+str(nowTime()))
			break
	os.close(rf)
	return ss

if __name__ == '__main__':
	print read_pipe()

import sys
import random
import operator
from functools import reduce
file=sys.argv[1]
count=sys.argv[2]
ips = []
for i in range(int(count)):
	ip=''
	for j in range(4):
		ip=ip+str(random.randint(0,255))
		ip=ip+'.'
	ip=ip[:-1]+''
	l=[]
	l.append(ip)
	ips.append(l*random.randint(0,255))
#print(ips)
ips=reduce(operator.add, ips)
#print(ips)
random.shuffle(ips)
with open(file,'w') as f:
	for ip in ips:
		f.write(ip+'\n')

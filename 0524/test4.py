import sys
file = sys.argv[1]
n = int(sys.argv[2])

with open(file,'r') as f:
	ips= [ip[:-1] for ip in f.readlines()]
	ips_set = set(ips)
	ips_dict = {}
	for ip in ips_set:
		ips_dict[ip] = ips.count(ip)
	ips_sorted=sorted(ips_dict.items(), lambda x,y: cmp(x[1],y[1]))
	print(ips_sorted)
	ips_sorted_reverse = ips_sorted[::-1]
	
	for i in range(n):
		ip,count = ips_sorted_reverse[i]
		print("the %d ip is:%s,number is %s"%(i+1, ip, count))

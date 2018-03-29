import os
s1='-'
s2='.'
filename=''
fileNum=0
changeNum=0
for ss in os.listdir("."):
	print ss
	n1=ss.index(s1)
	n2=ss.index(s2)
	fileNum=fileNum+1
	if(n1>0 and n2>0):
		filename=ss[0:n1]
		filename+=ss[n2:]
		print filename
		os.rename(ss, filename)
		changeNum=changeNum+1
print("fileNum:"+str(fileNum))
print("changeNum:"+str(changeNum))
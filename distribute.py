import os

result = open('part-00000','r')
i = 1
for line in result.readlines():
	line = line.strip('\n')
	line = line.strip(')')
	group_number = int(line.split(',')[-1])
	os.rename("/Users/shanqingtan/Desktop/result/file_%d.txt"%(i), "/Users/shanqingtan/Desktop/result/%d/file_%d.txt"%(group_number, i))
	i = i+1
	

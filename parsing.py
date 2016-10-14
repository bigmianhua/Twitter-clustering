import re

for i in range(166,351):
	nptweetfile = open('%d.txt'%(i),'r')
	savefile = open('file/file_%d.txt'%(i),'w')
	for line in nptweetfile:
		line = line.strip('\n')
		pattern_http=re.compile(r'https[^\s]+\s|https[^\s]+\n')
		if pattern_http.findall(str(line))!=[]:
		#delete http and replace data
			line=pattern_http.sub(r'',line)
		savefile.write(str(line))

	nptweetfile.close()




############

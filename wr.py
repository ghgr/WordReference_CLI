import urllib2,sys

args = sys.argv

if len(args)==1:
	print "Usage: wr enes house [num rel. Def 5]"
	exit(1)

if len(args)==4:
	res=int(args[3])
else:
	res=5

url = 'http://www.wordreference.com/'+args[1]+'/'+args[2]


headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request(url, None, headers)
data = urllib2.urlopen(req).read()

data=data.split("\n")

i=0
for line in data:
	if line.find("class='ToWrd'")<>-1:
		print line.split("'ToWrd'")[1].split("<em")[0].split("<a title")[0]
		i+=1
	if i==res:
		break
	

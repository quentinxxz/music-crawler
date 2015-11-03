import urllib
import urllib2
import sys
from StringIO import *
import gzip  
from GolableValues import *



url ='http://music.163.com/weapi/v1/resource/comments/R_AL_3_3308707/?csrf_token='
url="http://music.163.com/api/playlist/detail?id=113314392&ids=%5B%22113314392%22%5D&limit=10000&offset=0"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
cookie ='{placeholde}'

values = {
	'params':'cebkf4J/w/12R3e0+UZ0FCxvT66HrN3dqJicrkSfZPDItRVLwic9zRs6Y3G5KWP0',
	'encSecKey':'05a5e72e6c0a658f94cdbb1028b59bde2ae190aa987b45e8548e08006b841e4ed4502380462e942cfaa9be6563a8f0bc9b3f61b8791067d3e45bd2d36bb3d3fa3590471785398d8c5cad886b50483a129e38605aeb7355850bd53fa8a4e3dd916c23ab8267b27a75173c280422f6bb5c5f311bd9926ddfb85add98c530853e59'
	}
headers = { 
	'Host' : 'music.163.com',
	'Connection': 'keep-alive',
	'Origin':'http://music.163.com',
	'RA-Sid':'7D78DE40-20150702-170828-f2248c-87c071',
	'RA-Ver':'3.0.7',
 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
 	'Content-Type': 'application/x-www-form-urlencoded',

	'Cookie' : cookie,
	'Referer' : 'http://music.163.com/',
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
}

data = urllib.urlencode(values)
#req = urllib2.Request(url, data, headers)
req = urllib2.Request(url,  headers=headers)

response = urllib2.urlopen(req)
#print response.info()

if response.info().get('Content-Encoding') == 'gzip':
	print 'gzip enabled'
	buf = StringIO(response.read())
	f = gzip.GzipFile(fileobj=buf)
	data = f.read()
	html = data.decode('utf-8','replace').encode(sys.getfilesystemencoding())
	#print html
else:
	# sys.getfilesystemencoding() 
	the_page = response.read()

	html = the_page.decode('utf-8','replace').encode(sys.getfilesystemencoding())

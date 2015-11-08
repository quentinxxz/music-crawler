import urllib
import urllib2
import sys
from StringIO import *
import gzip  




url ='http://music.163.com/weapi/v1/resource/comments/R_AL_3_3308707/?csrf_token='
url="http://music.163.com/api/playlist/detail?id=113314392&ids=%5B%22113314392%22%5D&limit=10000&offset=0"
url="http://music.163.com/playlist?id=123905597"
url="http://music.163.com/api/playlist/detail?id=123905597"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
cookie ='_ntes_nuid=095e72026b39d417f409d1e38941f834; usertrack=c+5+hlXPNEmdK0bWH5CEAg==; _ntes_nnid=10450ccd3dc193a10f786ea74cbad33f,1439642698238; NETEASE_WDA_UID=15126131#|#1405510863328; Province=0571; City=0571; NTES_SESS=uCMzf7hI_e1Cyhd5AOy5pWC1QbOel4itcCcKi4dqL3r8UdQsjWDS2IDt4j2LE5GfRJ1qRnsA7cK43GeyuxZIARZpSu8UUWfXX9oogxokuPrnOqNzxN0t4hxlRuibHf8KwONPDfVIVX8AinX10Nzzlh6lM6Pd4z89Khco0KtNEvXSuE073zye.Zr3qj93DVv3t; S_INFO=1444230946|0|3&80##|quentinxxz#287777265; P_INFO=quentinxxz@163.com|1444230946|0|mobilemail|00&99|zhj&1444145356&carddav#zhj&330100#10#0#0|138938&0|mobilemail|quentinxxz@163.com; visited=true; playerid=72357665; playlist=113030239|113511978; JSESSIONID-WYYY=79394df28b5d74b1347858db28d5aa579ba1b1e68e268944eb276000a3e26866da137a4653eec827e90b3d144413fb78bafc60e6cd5d080bf285766ee50b2e20d913b2274fed19aa4d787b9db09e383e4f167638361dbd0aaefa9200e030673d014f21fb384dcb602eff669bb6f253d24009d3b49c8bda363e094fb18fd79da5054dc21b%3A1444320328151; _iuqxldmzr_=25; __utma=94650624.259324023.1441465620.1444314943.1444318529.8; __utmb=94650624.3.10.1444318529; __utmc=94650624; __utmz=94650624.1441465620.1.1.utmcsr=itechzero.com|utmccn=(referral)|utmcmd=referral|utmcct=/google-mirror-sites-collect.html'

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
	print html
else:
	# sys.getfilesystemencoding() 
	the_page = response.read()

	html = the_page.decode('utf-8','replace').encode(sys.getfilesystemencoding())

file_object = open('thefile.html', 'w')
file_object.write(html)
file_object.close( )



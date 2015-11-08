#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import sys
from StringIO import *
import gzip  

class PlayListDownloader(object):
    """This class is a http downloader to dowload 
    	music playlist as json text"""


    '''
    @param timeout
    @param cookie :please use the cookie when you are in login state 
    '''
    def __init__(self,timeout,cookie):

       self.timeout=timeout
       self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

       self.headers={ 
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



    '''   
    @param url : a playList url , example "http://music.163.com/api/playlist/detail?id=123905597"
    '''
    def downloadPlayList(self,url):
    	req = urllib2.Request(url,  headers=self.headers)
    	response = urllib2.urlopen(req,timeout=self.timeout)
    	if response.info().get('Content-Encoding') == 'gzip':
			buf = StringIO(response.read())
			f = gzip.GzipFile(fileobj=buf)
			data = f.read()
			playListJson = data.decode('utf-8','replace').encode(sys.getfilesystemencoding())
			f.close()
    	else: 
			sys.getfilesystemencoding() 
			the_page = response.read()
			playListJson = the_page.decode('utf-8','replace').encode(sys.getfilesystemencoding())
    	response.close()
    	return playListJson
	

if __name__ == '__main__':

	cookie = '_ntes_nuid=095e72026b39d417f409d1e38941f834; usertrack=c+5+hlXPNEmdK0bWH5CEAg==; _ntes_nnid=10450ccd3dc193a10f786ea74cbad33f,1439642698238; NETEASE_WDA_UID=15126131#|#1405510863328; Province=0571; City=0571; NTES_SESS=uCMzf7hI_e1Cyhd5AOy5pWC1QbOel4itcCcKi4dqL3r8UdQsjWDS2IDt4j2LE5GfRJ1qRnsA7cK43GeyuxZIARZpSu8UUWfXX9oogxokuPrnOqNzxN0t4hxlRuibHf8KwONPDfVIVX8AinX10Nzzlh6lM6Pd4z89Khco0KtNEvXSuE073zye.Zr3qj93DVv3t; S_INFO=1444230946|0|3&80##|quentinxxz#287777265; P_INFO=quentinxxz@163.com|1444230946|0|mobilemail|00&99|zhj&1444145356&carddav#zhj&330100#10#0#0|138938&0|mobilemail|quentinxxz@163.com; visited=true; playerid=72357665; playlist=113030239|113511978; JSESSIONID-WYYY=79394df28b5d74b1347858db28d5aa579ba1b1e68e268944eb276000a3e26866da137a4653eec827e90b3d144413fb78bafc60e6cd5d080bf285766ee50b2e20d913b2274fed19aa4d787b9db09e383e4f167638361dbd0aaefa9200e030673d014f21fb384dcb602eff669bb6f253d24009d3b49c8bda363e094fb18fd79da5054dc21b%3A1444320328151; _iuqxldmzr_=25; __utma=94650624.259324023.1441465620.1444314943.1444318529.8; __utmb=94650624.3.10.1444318529; __utmc=94650624; __utmz=94650624.1441465620.1.1.utmcsr=itechzero.com|utmccn=(referral)|utmcmd=referral|utmcct=/google-mirror-sites-collect.html'
	playListDownloader = PlayListDownloader(5,cookie)
	print playListDownloader.downloadPlayList("http://music.163.com/api/playlist/detail?id=123905597")



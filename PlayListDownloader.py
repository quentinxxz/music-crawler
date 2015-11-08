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
			'RA-Sid':'7D78DE40-20150702-170828-f2248c-87c071',##TODO ??  what's that
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

	cookie = 'your own cookie'
	playListDownloader = PlayListDownloader(5,cookie)
	print playListDownloader.downloadPlayList("http://music.163.com/api/playlist/detail?id=123905597")



#!/usr/bin/env python
#coding=utf-8

'''
crawl a playlist 

please provide follow infos : 
	1、palylist url
	2、your cookie in login state

'''

from PlayListDownloader import *
from PlaylistParser import *

cookie = '_ntes_nuid=095e72026b39d417f409d1e38941f834; usertrack=c+5+hlXPNEmdK0bWH5CEAg==; _ntes_nnid=10450ccd3dc193a10f786ea74cbad33f,1439642698238; NETEASE_WDA_UID=15126131#|#1405510863328; Province=0571; City=0571; NTES_SESS=uCMzf7hI_e1Cyhd5AOy5pWC1QbOel4itcCcKi4dqL3r8UdQsjWDS2IDt4j2LE5GfRJ1qRnsA7cK43GeyuxZIARZpSu8UUWfXX9oogxokuPrnOqNzxN0t4hxlRuibHf8KwONPDfVIVX8AinX10Nzzlh6lM6Pd4z89Khco0KtNEvXSuE073zye.Zr3qj93DVv3t; S_INFO=1444230946|0|3&80##|quentinxxz#287777265; P_INFO=quentinxxz@163.com|1444230946|0|mobilemail|00&99|zhj&1444145356&carddav#zhj&330100#10#0#0|138938&0|mobilemail|quentinxxz@163.com; visited=true; playerid=72357665; playlist=113030239|113511978; JSESSIONID-WYYY=79394df28b5d74b1347858db28d5aa579ba1b1e68e268944eb276000a3e26866da137a4653eec827e90b3d144413fb78bafc60e6cd5d080bf285766ee50b2e20d913b2274fed19aa4d787b9db09e383e4f167638361dbd0aaefa9200e030673d014f21fb384dcb602eff669bb6f253d24009d3b49c8bda363e094fb18fd79da5054dc21b%3A1444320328151; _iuqxldmzr_=25; __utma=94650624.259324023.1441465620.1444314943.1444318529.8; __utmb=94650624.3.10.1444318529; __utmc=94650624; __utmz=94650624.1441465620.1.1.utmcsr=itechzero.com|utmccn=(referral)|utmcmd=referral|utmcct=/google-mirror-sites-collect.html'
url= "http://music.163.com/api/playlist/detail?id=123905597"

#download the play list as json text
playListDownloader = PlayListDownloader(timeout=5,cookie=cookie)
playListJsonText=playListDownloader.downloadPlayList(url)




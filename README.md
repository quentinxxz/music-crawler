# music-crawler
对国内某互联网公司的音乐爬虫

## code Example in Main.py
```
'''
this file show you how to crawl a playlist 
and save the mp3 files , music info files into disk 
you should provide follow infos : 
	1、palylist url
	2、your cookie in login state
	3、directory paths to save PlayListInfo josn files、musicInfo josn files and mp3 files, you can change those diretories paths in Constants.py
'''

from PlayListDownloader import *
from PlayListParser import *

#replace the placeHolder with your own cookie
cookie = 'palaceHolder'
## playlist url  example, change id param if you want to crawl other playlists
url= "http://music.163.com/api/playlist/detail?id=123905597"

#download the play list as json text
playListDownloader = PlayListDownloader(timeout=5,cookie=cookie)
playListJsonText=playListDownloader.downloadPlayList(url)

#init the MP3Crawler with 10 work threads
crawler = MP3Crawler("MP3Crawler",10)
crawler.start()
    	
PlayListParser.init()
jsonData = PlayListParser.parser(playListJsonText)
#save the playListInfo
if PlayListParser.savePlayListInfo(jsonData):
	#save music Infos and  mp3 files
	PlayListParser.downloadMusics(jsonData,crawler)
	#wait to commplete
	crawler.waitUtilComplete()
else:
  	crawler.stop()
```

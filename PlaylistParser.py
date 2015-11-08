#!/usr/bin/env python
#coding=utf-8
import json
import os
from MP3Crawler import *
from Constants import *

class PlayListParser(object):
    """This class is used to parser json result """

    @classmethod
    def init(cls):
    	if not os.path.isdir(playListInfoDir):
    		os.mkdir(playListInfoDir)
    	if not os.path.isdir(musicInfoDir):
    		os.mkdir(musicInfoDir)
    	if not os.path.isdir(mp3Dir):
    		os.mkdir(mp3Dir)


    @classmethod
    def parser(cls,jsonText):
    	jsonData=json.loads(jsonText, encoding="utf-8")
    	return jsonData

    
    @classmethod 
    def savePlayListInfo(cls,josnData):
    	'''save a playlist info as file 
    		##TODO save into database
    	'''
    	playListInfo= josnData['result'].copy()
    	del playListInfo['tracks']
    	id = playListInfo['id']  ##TODO  raise some  exception 
    	if id :
    		playListInfoFie = open(playListInfoDir+str(id)+'.txt', 'w') 
    		playListInfoFie.write(str(playListInfo))
    		playListInfoFie.close( )
    		return True
    	else:
    		print 'save playListInfo fail'
    		return False


    @classmethod 
    def downloadMusics(cls,jsonData,mp3Crawler):
    	''''download mp3 music and save music info '''
    	tracks = jsonData['result']['tracks']
    	for track in tracks: 
    		PlayListParser.__saveMusic(track,mp3Crawler)
    		


    @classmethod 
    def __saveMusic(cls,track,mp3Crawler):
    	'''save a mp3 music info as file 
    		##TODO save into database
    	   and save mp3 file
    	'''
    	id = track['id']  ##TODO  raise some  exception 
    	if  id :
    		musicInfoFie = open(musicInfoDir+str(id)+'.txt', 'w') 
    		musicInfoFie.write(str(track))
    		musicInfoFie.close( )
    	else:
    		print 'save music info fail'
    		return False 

    	task={'savePath':mp3Dir + str(id)+'.mp3','url':track['mp3Url'],'type':'mp3'}
    	mp3Crawler.addTask(task)
    	return True



if __name__ == '__main__':

	fileObject = open('result.json')
	try:
		jsonText = fileObject.read( )
	finally:
		fileObject.close( )

	crawler = MP3Crawler("MP3Crawler",10)
	crawler.start()
    	
	PlayListParser.init()
	jsonData = PlayListParser.parser(jsonText)
	if PlayListParser.savePlayListInfo(jsonData):
		PlayListParser.downloadMusics(jsonData,crawler)

	crawler.waitUtilComplete()



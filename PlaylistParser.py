#!/usr/bin/env python
#coding=utf-8
import json
import os

class PlaylistParser(object):
    """This class is used to parser json result """

    @classmethod
    def parser(cls,jsonText):
    	jsonData=json.loads(jsonText)
    	return jsonData

    
    @classmethod 
    def savePlayListInfo(cls,josnData):
    	'''save a playlist info as file 
    		##TODO save into database
    	'''
    	playListInfo= josnData['result'].copy()
    	del playListInfo['tracks']
    	id = playListInfo['id']  ##TODO  raise some  exception 
    	dirPath = "playListInfo/"
    	if id :
    		if not os.path.isdir(dirPath):
    			os.mkdir(dirPath)
    		playListInfoFie = open(dirPath+str(id)+'.txt', 'w') 
    		playListInfoFie.write(str(playListInfo))
    		playListInfoFie.close( )
    		return True
    	else:
    		print 'save playListInfo fail'
    		return False




    @classmethod 
    def downloadMusics(cls,jsonData):
    	''''download mp3 music and save music info '''
    	tracks = jsonData['result']['tracks']
    	for track in tracks: 
    		print track
   

if __name__ == '__main__':
	fileObject = open('result.json')
	try:
		jsonText = fileObject.read( )
	finally:
		fileObject.close( )
	jsonData = PlaylistParser.parser(jsonText)
	PlaylistParser.savePlayListInfo(jsonData)
	#PlaylistParser.downloadMusics(jsonData)

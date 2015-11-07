#!/usr/bin/env python
#coding=utf-8
import threading
import urllib
import re
import time
from ThreadPool import *
from MP3Downloader import *

class MP3Crawler:
    '''
    @param crawlername
    @param workerThreadNum
    @param pollInterval: interval time to poll task from task queue
    @param pollTimeout: timeout seconds to poll a task from task queue
    @param downloadTimeout: timeout seconds to download media from web
    '''
    def __init__(self,crawlername,workerThreadNum,
        pollInterval=0.5,pollTimeout=None,downloadTimeout=5):
        self.threadPool = ThreadPool(workerThreadNum)
        self.crawlername=crawlername
        self.pollTimeout = pollTimeout 
        self.crawlerThread = CrawlerThread(self.threadPool,pollTimeout)
        self.mp3Downloader = MP3Downloader(downloadTimeout)

    def start(self):
        '''start crawl'''
        self.crawlerThread.start()

    def stop(self):
        '''stop crawl, block until all tasks finish'''
        self.threadPool.stop()
        self.crawlerThread.dismiss()
        self.crawlerThread.join()

    def __checkTask(self,task):
        if task.has_key('type')==False or task.has_key('url') ==False:
           return False
        if task['type']!='mp3' and task['type']!='html' and task['type']!='json':
            return False
        if task.has_key('savePath')==False:
            return False
        else:
            return True
    
    def downloadMP3(self,url,filePath):
        self.mp3Downloader.downloadM(url, filePath)

    def addTask(self,task):
        '''add a mp3 download task
        '''
        if self.__checkTask(task) == False:
            print 'Task not Avilable:', task  
            return
        req = WorkRequest(self.downloadMP3,args=[task['url'],task['savePath']],kwds={},callback=self.__printResult)
        self.threadPool.putRequest(req)
        print "work request #%s added." % req.requestID

    def __printResult(self,request,result):
        print "---Result from request %s : %r" % (request.requestID,result)
        #pass


class CrawlerThread(threading.Thread):
    """Crawler Thread"""
    def __init__(self,threadPool,pollInterval):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.threadPool = threadPool
        self.pollInterval = pollInterval
        self._dismissed = threading.Event()
        
    def run(self):
        while True:
            #TODO: left taskes may not be executed
            if self._dismissed.is_set():
                    break
            try:
                if(self.pollInterval>0):
                    time.sleep(self.poolInterval) 
                self.threadPool.poll()
            except NoResultsPending:
                print "no pending results"
                break
    
    def dismiss(self):
        self._dismissed.set()

if __name__=="__main__":
    crawler = MP3Crawler("MP3Crawler",3)
    crawler.start()
    for i in range(5):
        task ={'savePath':"tmp/" + str(i)+'.mp3','type':'mp3',
        'url':"http://m2.music.126.net/yvMiGSJhylUxrU2AGhuTbg==/1158885255685125.mp3"}
        crawler.addTask(task)
    time.sleep(20)
    crawler.stop()
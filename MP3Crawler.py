#!/usr/bin/env python
#coding=utf-8
import threading
import urllib
import re
import time
from ThreadPool import *

class MP3Crawler:
    '''
    @param crawlername
    @param workerThreadNum
    @param pollInterval: interval time to poll task from task queue
    @param pollTimeout: timeout second to poll a task from task queue
    '''
    def __init__(self,crawlername,workerThreadNum,pollInterval=5,pollTimeout=None):
        self.threadPool = ThreadPool(workerThreadNum)
        self.crawlername=crawlername
        self.pollTimeout = pollTimeout 
        self.crawlerThread = CrawlerThread(self.threadPool,pollTimeout)

    def start(self):
        '''start crawl'''
        crawlerThread.start()

    def stop(self):
        '''stop crawl, block until all tasks finish'''
        self.threadPool.stop()
        self.crawlerThread.dismiss()
        self.crawlerThread.join()

    def __checkTask(self,task):
        if task.has_key('type')==False or task.has_key('url') ==False:
           return False
        if task['type']!='mp3' or task['type']!='html' or task['type']!='json':
            return False
        if task.has_key('savePath')==False:
            return False
        else:
            return True
    
    def downloadMP3(url,filePath):
        downloader.downloadM(url, filePath)

    def addTask(self,task):
        '''add a mp3 download task
        '''
        if self.__checkTask(task) == False:
            print 'Task not Avilable:', task  
            return
        req = WorkRequest(downloadMP3,args=[task['url'],task['savePath']],kwds={},callback=self.__printResult)
        main.putRequest(req)
        print "work request #%s added." % req.requestID

    def __printResult(request,result):
        pass
        '''print "---Result from request %s : %r" % (request.requestID,result)
        '''

class CrawlerThread(threading.Thread):
    """Crawler Thread"""
    def __init__(self,threadPool,pollInterval):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.threadPool = threadPool
        self.pollInterval = pollInterval
        self._dismissed = threading.Event()
        self.start()
        
    def run(self):
        while True:
            #TODO: left taskes may not be executed
            if self._dismissed.is_set():
                    break
            try:
                if(self.pollInterval>0):
                    time.sleep(self.poolInterval) 
                threadPool.poll()
            except NoResultsPending:
                print "no pending results"
                break
    
    def dismiss(self):
        self._dismissed.set()

if __name__=="__main__":
    task ={'a':1}
    crawler = MP3Crawler("mp3",3)
    crawler.addTask(task)
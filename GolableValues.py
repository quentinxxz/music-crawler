#!/usr/bin/env python
#coding=utf-8
import threading


g_mutex=threading.Condition()
g_pages=[]  #从中解析所有url链接
g_queueURL=[]  #等待爬取的url链接列表
g_existURL=[]  #已经爬取过的url链接列表
g_failedURL=[] #下载失败的url链接列表
g_totalcount=0 #下载过的页面数


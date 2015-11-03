import urllib  



class MP3Downloader(object):
    """This class is a http mp3 downloader"""


    def __init__(self,timeout):
       self.timeout=timeout


    def jujstPrint(self):
    	print self.timeout 	
   
    def __myCallback(blocknum, blocksize, totalsize): 
        ## donothing yet  
        pass  
        '''percent = 100.0 * blocknum * blocksize / totalsize
        if percent>100.0:
            percent=100
        else:
            print percent'''

    def downloadM(self,url,local,callbackfunc=__myCallback):
        #"""" download methond"""""
        urllib.urlretrieve(url, local, callbackfunc)


def test():
    downloader = MP3Downloader(100)
    downloader.jujstPrint()
    downloader.downloadM("http://m2.music.126.net/yvMiGSJhylUxrU2AGhuTbg==/1158885255685125.mp3", "a.mp3")

if __name__ == '__main__':
    test()


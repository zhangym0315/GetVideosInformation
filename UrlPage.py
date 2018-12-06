import requests
from Video import Video
from bs4 import BeautifulSoup
import json
import re

class UrlPage():
    def __init__(self, pageurl):
        self.pageurl = pageurl
        self.content = self.getPageContent
        return None
    
    @property
    def getPageContent(self):
        r = requests.get(self.pageurl)
        return r.content.decode('utf-8')
    
    @property
    def getVideo(self):
        video = Video(self.getPageContent)
        return video
    
    @property
    def otherUrls(self):
        relatepattern = re.compile("\"u\":\"(.*?)\"")
        url = 'https://www.xvideos.com/'
        soup = BeautifulSoup(self.getPageContent, features="html.parser")
        scripts = soup.findAll('script')
        relate_scr = ''
        for scr in scripts:
            if 'video_relate' in scr.text[4:16]:
                relate_scr = scr.text
        relates = re.findall(relatepattern, relate_scr)
        otherurls = []
        for relate in relates:
            relate = relate.replace('\\', '')
            otherurls.append(url+relate[1:])
        return otherurls
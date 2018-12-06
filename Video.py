import re
from SaveFile import SaveFile
from bs4 import BeautifulSoup

class Video():
    def __init__(self, urlcontent):
        self.urlcontent = urlcontent
        self.titleRe = "setVideoTitle\(\'(.+?)\'\);"
        self.lowMp4Re = "setVideoUrlLow\(\'(.+?)\'\);"
        self.highMp4Re = "setVideoUrlHigh\(\'(.+?)\'\);"
        return None
    
    def cleanTitle(self, title):
        cleanedTitle = ''
        for t in title:
            if t.isdigit() or t.isalpha():
                cleanedTitle += t
        cleanedTitle += '.mp4'
        return title

    @property
    def videoTitle(self):
        soup = BeautifulSoup(self.urlcontent, features="html.parser")
        return soup.title.text
#        patternTitle = re.compile(self.titleRe)
#        matchTitle = patternTitle.search(self.urlcontent)
#        if matchTitle:
#            return self.cleanTitle(matchTitle.group(1))
#        else:
#            return None

    def videoMp4(self, quantity='low'):
        if quantity == 'low':
            patternMp4 = re.compile(self.lowMp4Re)
        else:
            patternMp4 = re.compile(self.highMp4Re)
        matchMp4 = patternMp4.search(self.urlcontent)
        if matchMp4:
            mp4url = matchMp4.group(1)
            return mp4url
        else:
            return None
    
    def videoDownload(self, quantity, path, num):
        videourl = self.videoMp4(quantity)
        if videourl != None:
            savefile = SaveFile(path)
            return savefile.saveFromUrl(videourl, self.videoTitle, num)
        else:
            return None
    
    @property
    def videoTags(self):
        soup = BeautifulSoup(self.urlcontent, features="html.parser")
        links = soup.findAll('a')
        tags = []
        for link in links:
            href = link.get('href')
            if href != None:
                if '/tags' in href:
                    tags.append(href)
        return tags





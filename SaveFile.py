import os
#from PrintLog import PrintLog

class SaveFile():
    def __init__(self, path):
        self.path = path
        return None
    
    def saveFromUrl(self, url, title, num):
        print("Download %s[title] - %s[url]" %(title, url))
        if  not os.path.exists(self.path+str(num)+'.mp4'):
            try:
                wgetlog = os.system("wget "+url+" -O "+self.path+str(num)+'.mp4')
                print(wgetlog)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            print("Already Download for %d" %(num))
            return True

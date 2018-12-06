import os
import pandas as pd
import json

class LogDownload():
    def __init__(self, path):
        self.path = path
        self.files = self.logFiles
        return None
    
    @property
    def initialDic(self):
        dic = {'id':[0], \
                'url':['n'], \
                'title':['n'], \
                'tags':[json.dumps(['n'])]}
        return dic

    @property
    def logFiles(self):
        files = os.listdir(self.path)
        return files

    @property
    def loadLog(self):
        df = pd.DataFrame(self.initialDic)
        for n, file in enumerate(self.files):
            df1 = pd.read_csv(self.path+file)
            if n == 0:
                df = df1
            else:
                df = df.merge(df1, how='outer')
        return df
    
    @property
    def downloadedList(self):
        df = self.loadLog
        return list(df['url'])
    
    @property
    def newNum(self):
        return(max(self.loadLog['id']))

    def logName(self, dic):
        print(dic['id'])
        startnum = min(list(dic['id']))
        endnum = max(list(dic['id']))
        name = "%d_%d.csv" %(startnum,endnum)
        return name
    
    def writeLog(self, dic):
        name = self.logName(dic)
        df = pd.DataFrame(dic)
        df.to_csv(self.path+name, index=False)
        return self.path+name

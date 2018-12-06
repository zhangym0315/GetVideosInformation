from UrlPage import UrlPage
from Video import Video
from LogDownload import LogDownload
import pandas as pd
import json

def initialDownload(pathlog):
    ld = LogDownload(pathlog)
    downloadedurls = ld.downloadedList
    n = ld.newNum+1
    return downloadedurls, n

def DownloadUrls(path, urls, downloadedurls, n, dic, batch):
    newurls = []
    for unum, url in enumerate(urls):
        if n%batch == 0 and n!=0 and unum!=0:
            break
        print("Start %d url: %s" %(n, url))
        if url not in downloadedurls:
            page = UrlPage(url)
            video = page.getVideo
            video.videoDownload('high', path, n)
            tags = video.videoTags
            downloadedurls.append(url)
            otherurls = page.otherUrls
            for ourl in otherurls:
                if ourl not in downloadedurls:
                    newurls.append(ourl)
            dic["id"].append(n)
            dic["title"].append(video.videoTitle)
            dic["tags"].append(json.dumps(tags))
            dic["url"].append(video.videoMp4('high'))
        else:
            print("Downloaded!")
            continue
        print("End %d url: %s" %(n, url))
        n+=1
    return newurls, downloadedurls, n, dic

pathlog = "/home/yayalio315/VD/logs/"
path = "/home/yayalio315/VD/videos/"
pathnew = "/home/yayalio315/VD/newurls.txt"
ld = LogDownload(pathlog)
dic = ld.initialDic
starturl = [""]
T = True
n = 0
m = 0
batch = 100
while T:
    if n%batch==0 and n!=0:
        ld = LogDownload(pathlog)
        ld.writeLog(dic)
        dic = ld.initialDic
        downloadedurls, n =initialDownload(pathlog)
        print("New n :%d" %(n))
        with open(pathnew, 'w') as f:
            f.write('\n'.join(newurls))
    else:
        print("***** Start %d_%d Batch *****" %(int(n/batch), n))
        if n == 0:
            downloadedurls, n =initialDownload(pathlog)
            newurls = ["https://www.xvideos.com/video14647825/hentai_-_female_ravaged_by_soldiers"]
            print(n)
            if n != 0 and n != 1:
                with open(pathnew, 'r') as f:
                    newurls = f.read().split('\n')
    newurls, downloadedurls, n, dic = DownloadUrls(path, newurls, downloadedurls, n, dic, batch)
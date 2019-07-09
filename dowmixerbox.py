import requests
import youtube_dl
import uuid


class mixerbox:
    r = requests.session()
    my_headers = {
        'Referer': 'https://www.mixerbox.com/user/1234567',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    }
    def dowload(self, item):
        options = {
            'format': 'bestaudio/best',
            'outtmpl': 'G:\\GitHub\\Downloads\\music\\%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        for x in item:
            try:
                if x['type'] != 'music':
                    continue
                url = "http://www.youtube.com/watch?v=" + x["f"]
                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([url])
                pass
            except:
                pass

    def getHTML(self, vectorId):
        cto = self.r.get('https://www.mixerbox.com/service?func=getVector&locale=zh-tw&type=playlist&uuid=' + str(uuid.uuid4()) + '-web&vectorId=' + vectorId, headers = self.my_headers)
        # cto = requests.get(
        #     'http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId=' + vectorId + '&random=8398&_=1453105381259')
        return cto.json()


mixerbox = mixerbox()
vectorId = "106086091"  # 歌單的編碼 https://www.mixerbox.com/list/106086091
result = mixerbox.getHTML(vectorId)
item = result["getVector"]["items"]
mixerbox.dowload(item)
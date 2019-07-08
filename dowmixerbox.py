import requests
import youtube_dl
import json
import re
import uuid


class mixerbox:
    r = requests.session()
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
                url = "http://www.youtube.com/watch?v=" + x["f"]
                with youtube_dl.YoutubeDL(options) as ydl:
                    ydl.download([url])
                pass
            except:
                pass

    def getHTML(self, vectorId):
        rrr = 'https://www.mixerbox.com/list/7742969'

        rrr = 'https://www.mixerbox.com/service?func=getVector&locale=zh-tw&type=playlist&uuid=6afdff98-9fa2-4876-b37a-5746b017b256-web&vectorId=7742969'
        newUuid = str(uuid.uuid4()) + '-web'
        cookie = {
            '__cfduid' : "d7cc2481cbb80a715bd6dd743ee1e77af1560955670",
            'driftt_aid' : "39981c55-9cbd-4194-9586-60c98813e2cd",
            'DFTT_END_USER_PREV_BOOTSTRAPPED' : "true",
            'PHPSESSID' : "3tav1m2m1s3sp1agh88622cr23",
            'uuid' : "6afdff98-9fa2-4876-b37a-5746b017b256-web",
            'driftt_wmd' : "true",
            'driftt_sid' : "a8d0249e-10d1-4334-82d8-c167e40203ca"
        }
        # self.r.cookies.set(cookie)
        html = self.r.get(rrr , cookies=cookie)
        # html2 = self.r.get('https://www.mixerbox.com/service?func=getVector&locale=zh-tw&type=playlist&uuid=6afdff98-9fa2-4876-b37a-5746b017b256-web&vectorId=7742969')
        # print(html.headers)
        print(self.r.cookies.get_dict())
        # print(self.r.text)
        exit()
        cto = requests.get(
            'http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId=' + vectorId + '&random=8398&_=1453105381259')
        return cto.text


mixerbox = mixerbox()
vectorId = "40361693"  # 歌單的編碼 https://www.mixerbox.com/user/40361693
HTML = mixerbox.getHTML(vectorId)
# result = re.search(r'\((.+?)\)\;',HTML).group(1)
# res = json.loads(result)
# item = res["getVector"]["items"]
# mixerbox.dowload(item)
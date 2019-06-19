# -*- coding: UTF-8 -*- 
import requests
import youtube_dl
import json
import re
import listtt

class mixerbox:
	def getvectorId(self, url):
		try:
			return re.search(r'http\:\/\/www\.mixerbox\.com\/list\/([0-9]+)', url).group(1)
			pass
		except:
			print("網址輸入錯誤")
			exit()

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
			

	def getHTML(self,vectorId):
		cto = requests.get('http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId='+vectorId+'&random=8398&_=1453105381259')
		return cto.text

# print(listtt.aliist)
mixerbox = mixerbox()
# InputUrl = input("請輸入收藏清單網址：")
# vectorId = mixerbox.getvectorId(InputUrl)
vectorId = "7742969"
# HTML = mixerbox.getHTML(vectorId)
# result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = listtt.aliist
# res = json.loads(result)
# print(res)
item = res["getVector"]["items"]
mixerbox.dowload(item)
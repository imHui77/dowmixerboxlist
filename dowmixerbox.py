# -*- coding: UTF-8 -*- 
import urllib.request
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
			'verbose': True,
			'format': 'bestaudio/best',
			'outtmpl': 'C:\\Users\\user\\Downloads\\music\\%(title)s.%(ext)s',
			'noplaylist' : True,
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
			}],
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
		cto = urllib.request.urlopen('https://www.mixerbox.com/service?func=getVector&locale=zh-tw&type=playlist&uuid=dbb57c69-f753-4470-8024-2a1ea01135c8-web&vectorId=' + vectorId)
		return cto.read().decode('utf-8')

# print(listtt.aliist)
mixerbox = mixerbox()
# InputUrl = input("請輸入收藏清單網址：")
# InputUrl = 'http://www.mixerbox.com/list/7742969'
# vectorId = mixerbox.getvectorId(InputUrl)
# vectorId = "7742969"
# HTML = mixerbox.getHTML(vectorId)
# result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = listtt.aliist
# res = json.loads(result)
# print(res)
item = res["getVector"]["items"]
mixerbox.dowload(item)
# -*- coding: UTF-8 -*- 
import urllib.request
import youtube_dl
import json
import re

class mixerbox:
	def getvectorId(self,url):
		try:
			return re.search(r'http\:\/\/www\.mixerbox\.com\/list\/([0-9]+)',url).group(1)
			pass
		except:
			print("網址輸入錯誤")
			exit()

	def dowload(self,item):
		options = {
			'verbose': True,
			'format': 'mp4',
			'outtmpl': 'C:\\Users\\user\\Downloads\\music\\%(title)s.%(ext)s',
			'noplaylist' : True,
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
			}],
		}
		for x in item:
			url = "http://www.youtube.com/watch?v="+x["f"]
			try:
				with youtube_dl.YoutubeDL(options) as ydl:
					ydl.download([url])
				pass
			except:
				pass
			

	def getHTML(self,vectorId):
		cto = urllib.request.urlopen('http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId='+vectorId+'&random=8398&_=1453105381259')
		return cto.read().decode('utf-8')

mixerbox = mixerbox()
<<<<<<< HEAD
# InputUrl = input("請輸入收藏清單網址：")
# vectorId = mixerbox.getvectorId(InputUrl)
vectorId = "7742969"
=======
InputUrl = input("請輸入收藏清單網址：")
vectorId = mixerbox.getvectorId(InputUrl)
HTML = mixerbox.getHTML(vectorId)
result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = json.loads(result)
item = res["getVector"]["items"]
mixerbox.dowload(item)
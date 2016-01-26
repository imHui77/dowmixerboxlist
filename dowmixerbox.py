# -*- coding: UTF-8 -*- 
import urllib.request
import youtube_dl
import json
import re
# from bs4 import BeautifulSoup

class mixerbox:
	def getvectorId(self,url):
		try:
			return re.search(r'http\:\/\/www\.mixerbox\.com\/list\/([0-9]+)',url).group(1)
			# return vectorId
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
			with youtube_dl.YoutubeDL(options) as ydl:
				ydl.download([url])
			# try:
			# 	url = "http://www.youtube.com/watch?v="+x["f"]
			# 	with youtube_dl.YoutubeDL(options) as ydl:
			# 		ydl.download([url])
			# 	pass
			# except:
			# 	# print("========檔名有問題=========")
			# 	# print("代碼:"+x["f"])
			# 	# print(x["tt"].encode('utf-8'))
			# 	# print("========檔名有問題=========")
			# 	pass

mixerbox = mixerbox()
InputUrl = input("請輸入收藏清單網址：")
vectorId = mixerbox.getvectorId(InputUrl)
# vectorId = re.search(r'http\:\/\/www\.mixerbox\.com\/list\/([0-9]+)',InputUrl).group(1)
# vectorId = "7742969"
cto = urllib.request.urlopen('http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId='+vectorId+'&random=8398&_=1453105381259')
HTML = cto.read().decode('utf-8')
# HTML = cto.read()
# soup = BeautifulSoup(HTML,"html5lib")
# print(soup)
result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = json.loads(result)
item = res["getVector"]["items"]
mixerbox.dowload(item)
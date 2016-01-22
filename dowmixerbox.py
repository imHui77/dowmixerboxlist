# -*- coding: UTF-8 -*- 
import urllib.request
import youtube_dl
import json
import re
from bs4 import BeautifulSoup

InputUrl = input("請輸入收藏清單網址：")
vectorId = re.search(r'http\:\/\/www\.mixerbox\.com\/list\/([0-9]+)',InputUrl).group(1)
cto = urllib.request.urlopen('http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId='+vectorId+'&random=8398&_=1453105381259')
HTML = cto.read().decode('utf-8')
result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = json.loads(result)
item = res["getVector"]["items"]
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
	try:
		url = "http://www.youtube.com/watch?v="+x["f"]
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([url])
		pass
	except:
		# print("========檔名有問題=========")
		# print("代碼:"+x["f"])
		# print(x["tt"].encode('utf-8'))
		# print("========檔名有問題=========")
		pass
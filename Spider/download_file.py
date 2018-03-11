# -*- coding=utf-8 -*-
import requests

class df():
	def __init__(self,url,path,name):
		self.url = url 
		self.path = path
		self.name = name

	def dp(self):
		l = self.url + self.name
		p = self.path + self.name
		response=requests.get(l,stream=True)
		
		try:
			with open(p,'wb')as f:
				for chunk in response.iter_content(128):
					f.write(chunk)
		except Exception as e:
			print(e)

if __name__ == '__main__':
	a=df('http://yqgx.xatrm.com/upload/images/import/','f:\\csv\\','345.jpg')
	a.dp()
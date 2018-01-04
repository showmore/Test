# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import os
import os.path
import time

cookies={'JSESSIONID':'DF7CBA95366E585826CF4B5DEFEF119A'}
url='http://dxmmqrdadmin.xainfo.gov.cn/api/mqinfo/mqinfo_view.action?ids='

with open('c:\\gyqy_ids.txt','r') as ids_file:
	for ids in ids_file.read().split(','):

		res = requests.get(url+ids,cookies=cookies)
		res.encoding ='utf-8'
		soup = BeautifulSoup(res.text,'html.parser')
		h=str(soup)

		with open('C:\\Python_Project\\gyqy_html\\%s.html'% ids,'w',encoding='utf-8') as f:
			f.write(h)
			print(url+ids)
		time.sleep(1)

# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import requests
import re
import os
import os.path
import pymysql

file=[]
rootdir='C:\\Python_Project\\qy_html\\'
cookies={'JSESSIONID':'FDC3E5E5D506127D5CF6851ED2DBFBCB'}
conn = pymysql.connect(host='192.168.8.69', port=3306, user='root', passwd='rootroot',db='demo',charset='utf8') 
cur = conn.cursor()

for parent,dirnames,filenames in os.walk(rootdir):  
    for filename in filenames:     
        file.append(os.path.join(parent,filename))
print('共有文件数：'+str(len(file)))

for f in file:
	with open(f,'r',encoding='utf-8') as fi:
		html=fi.read()
	soup = BeautifulSoup(html,'html.parser')
	for idx,link in enumerate(soup.find_all('a')):
		print('-'*100)
		fn=f[26:-5]
		print(fn)
		print(idx)
		imgname=link.text
		print(imgname)
		jpgname=link.get('href')[-20:]
		print(jpgname)
		lk=link.get('href')
		print(lk)
		sql='insert into jpg(id,sid,name,jpgname,url) \
		values("%s","%s","%s","%s","%s")' %(fn,idx,imgname,jpgname,lk)
		print(sql)
		cur.execute(sql)
		conn.commit()

		if lk[:35]=='http://dxmmqrd.xainfo.gov.cn/upload':
			try:
				response=requests.get(lk,stream=True,cookies=cookies)
				with open('f:\\jpg\\%s' %(jpgname),'wb')as f:
					for chunk in response.iter_content(128):
						f.write(chunk)
			except:
				continue
cur.close()
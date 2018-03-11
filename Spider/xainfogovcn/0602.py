# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re
import os
import os.path


# 文件列表
rootdir='C:\\Python_Project\\xjr_list'
file=[]
ids=[]
for parent,dirnames,filenames in os.walk(rootdir):  
    for filename in filenames:     
        file.append(os.path.join(parent,filename))
print(file)
#取IDS
for f in file:
	with open('%s' % f,'r',encoding='utf-8') as fi:
		html=fi.read()
	soup = BeautifulSoup(html,'html.parser')
	td = soup.find_all("a", href=re.compile("orgId"),string="查看")
	for i in td:
		print(i[44:76])

	


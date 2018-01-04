# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re
import os
import os.path


# 文件列表
rootdir='C:\\Python_Project\\xjr_list\\'
file=[]
ids=[]
for parent,dirnames,filenames in os.walk(rootdir):  
    for filename in filenames:     
        file.append(os.path.join(parent,filename))
print('共有文件数：'+len(file))

#取IDS
for f in file:
	with open('%s' %f,'r',encoding='utf-8') as fi:
		html=fi.read()
	soup = BeautifulSoup(html,'html.parser')
	td = soup.select('input[name="ids"]')
	p = re.compile(r'''<input name="ids" type="checkbox" value="(.*)"/>''')

	for i in td:
		ids.append(p.findall(str(i))[0])

print(len(ids))

with open ('c:\\xjr_ids.txt','a') as ads_f:
	for n in ids:
		ads_f.write(n+',')


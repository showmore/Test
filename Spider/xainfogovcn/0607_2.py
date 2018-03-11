# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re

fn='E9CC8DB347425022E040007F0100109C'
with open('C:\\Python_Project\\spider\\gyqy_html\%s.html' %fn,'r',encoding='utf-8',errors='ignore') as fi:
	html=fi.read()
	soup = BeautifulSoup(html, 'html.parser')


	for idx, tb in enumerate(soup.find_all('table')):
		if idx < 10:
			tb = tb.select('table')
			for tb_idx,t in enumerate(tb):
				print('-'*20+' 分割线 '+'-'*20)
				for tr_idx, tr in enumerate(t.find_all('tr')):
					tds = tr.select('td')
					m = re.sub(r'<.*?>', '', str(tds))
					l=m.replace(" ","").replace("[","").replace("]","").\
					replace("\n","").replace("\t","").replace("\xa0","").split(",")

					# print(tb_idx,tr_idx)
					# print(l)

					if tb_idx == 0 and tr_idx > 1:
						# print(fn,tr_idx-1,l[0],l[1],l[2])
						sql='insert into talbe(a,b,c,d,e) values("%s","%s","%s","%s","%s")' \
						% (fn,tr_idx-1,l[0],l[1],l[2])
						print(sql)
					elif tb_idx == 1 and tr_idx > 0:
						# print(fn,tr_idx,l[0],l[1],l[2])
						sql='insert into talbe(a,b,c,d,e,f) values("%s","%s","%s","%s","%s")' \
						% (fn,tr_idx-1,l[0],l[1],l[2])
						print(sql)
					elif tb_idx == 2 and tr_idx > 0:
						# print(fn,tr_idx,l)
						sql='insert into talbe(a,b,c,d,e,f) values("%s","%s","%s","%s","%s","%s")' \
						% (fn,tr_idx,l[0],l[1],l[2],l[3])
						print(sql)
					elif tb_idx == 3 and tr_idx > 1:
						# print(fn,tr_idx-1,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7])
						sql='insert into talbe(a,b,c,d,e,f,g,h,i,j) \
						values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' \
						% (fn,tr_idx-1,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7])
						print(sql)

# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re

fn='CDE2F02CBB16B06AE040007F01002A1C'
with open('C:\\Python_Project\\spider\\gyqy_html\%s.html' %fn,'r',encoding='utf-8',errors='ignore') as fi:
	html=fi.read()
	soup = BeautifulSoup(html, 'html.parser')

	new_dict={}

	for idx, tr in enumerate(soup.find_all('tr')):
	    tds = tr.select('td')
	    m = re.sub(r'<.*?>', '', str(tds))
	    l=m.replace(" ","").replace("[","").replace("]","").\
	    replace("\n","").replace("\t","").replace("\xa0","").split(",")

	    if idx in [0,1,2,3,4,5,6,9,13,14,15,20,21,22,23,33,\
			37,40.41,43,45,57,68]:
	    	print(str(idx)+". "+"-"*10+str(len(l))+"位元素"+"-"*10)
	    	print(l)
	    	new_dict[l[0]]=l[1]
	    	new_dict[l[2]]=l[3]
	    	
	    	# print(l[0]+": "+l[1]+"\n"+l[2]+": "+l[3])
	    elif idx in [7,8,10,11,12,16,24,35,37,39,46,47,48,49]:
	    	print(str(idx)+". "+"-"*10+str(len(l))+"位元素"+"-"*10)
	    	print(l)
	    	new_dict[l[0]]=l[1]
	    	# print(l[0]+": "+l[1])
	    elif idx in [18]:
	    	print(str(idx)+". "+"-"*10+str(len(l))+"位元素"+"-"*10)
	    	print(l)
	    	new_dict["高企"+l[0]]=l[1]
	    	new_dict["高企"+l[2]]=l[3]
	
	print(len(new_dict))
	print(new_dict.keys())



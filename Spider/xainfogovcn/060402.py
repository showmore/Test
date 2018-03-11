# -*- coding: UTF-8 -*- 

from bs4 import BeautifulSoup
import re

fn='E9CC8DB347425022E040007F0100109C'
with open('C:\\Python_Project\\spider\\gyqy_html\%s.html' %fn,'r',encoding='utf-8',errors='ignore') as fi:
	html=fi.read()
	soup = BeautifulSoup(html, 'html.parser')

	new_dict={}

	for idx, tr in enumerate(soup.find_all('tr')):
	    tds = tr.select('td')
	    m = re.sub(r'<.*?>', '', str(tds))
	    l=m.replace(" ","").replace("[","").replace("]","").\
	    replace("\n","").replace("\t","").replace("\xa0","").split(",")

	    if len(l)== 4:
	    	if idx in [18]:
	    		new_dict["高企"+l[0]]=l[1]
	    		new_dict["高企"+l[2]]=l[3]

	    	print(str(idx)+". "+"-"*10+str(len(l))+"位元素"+"-"*10)
	    	print(l)
	    	new_dict[l[0]]=l[1]
	    	new_dict[l[2]]=l[3]
	    	
	    	# print(l[0]+": "+l[1]+"\n"+l[2]+": "+l[3])
	    elif len(l) ==2:
	    	print(str(idx)+". "+"-"*10+str(len(l))+"位元素"+"-"*10)
	    	print(l)
	    	new_dict[l[0]]=l[1]
	    	# print(l[0]+": "+l[1])
	    
	
	print(len(new_dict))
	print(new_dict.keys())



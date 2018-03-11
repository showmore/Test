# coding:utf-8
# date:2018-01-08
# author:George

import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import requests
from bs4 import BeautifulSoup
import pymysql
import re
import random
import lxml
import urllib

# 获取即席时间
def get_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 获取随机代理ip
def get_random_ip():
	ips = []
	ip = {}
	with open("f://ip.txt","r") as f:
		for i in f.readlines():
			ips.append(i)
	ip_str = random.choice(ips)
	ip[re.split('://',ip_str)[0]] = ip_str.replace('\n','')
	return ip

# 获取随机代理ip
def get_random_httpip():
    ips = []
    ip = {}
    with open("f://ip.txt","r") as f:
        for i in f.readlines():
            if i.startswith('HTTP://'):
                ips.append(i)
    ip_str = random.choice(ips)
    ip[re.split('://', ip_str)[0]] = ip_str
    return ip

# 获取随机user-agent
def get_random_headers():
    agents = []
    headers = {}
    with open("f://agent.txt", "r") as f:
        for i in f.readlines():
            agents.append(i)
    headers['User-Agent'] = random.choice(agents).replace('\n', '')
    return headers

# 根据url返回soup对象
def soup(url):
	reponse = requests.get(url,proxies=get_random_ip(),headers=get_random_headers(),timeout=10)
	content = reponse.content
	return BeautifulSoup(content, "lxml"),reponse.headers,reponse.url

# 获取category页面url列表
def get_categoryurl(start_url):
	bsObj = soup(start_url)
	tr=bsObj[0].find_all('tr')
	categoryurl=[]
	for td in tr:
		try:
			td = td.find_all('td')
			committee = td[0].get_text().strip()
			link_url = 'https://www.iso.org'+td[0].find('a').get('href').strip()
			title = td[1].get_text().strip()
			categoryurl.append([committee,link_url,title])
		except:
			pass
	return categoryurl

def get_subcategoryurl(start_url):
	bsObj = soup(start_url)
	tr=bsObj[0].find_all('tr')
	subbcategory=[]
	for td in tr:
		# try:
		Subcommittee = td.find('td',{'data-title':'Subcommittee'}).get_text().strip()
		subbcategoryurl = 'https://www.iso.org'+td.find('td',{'data-title':'Subcommittee'}).find('a').get('href')
		title = td.find('td',{'data-title':'Subcommittee Title'}).get_text()
		published = td.find('td',{'data-title':'Published standards'}).find('a').get_text()
		under_development = td.find('td',{'data-title':'Standards under development'}).find('a').get_text()

		subbcategory.append([Subcommittee,subbcategoryurl,title,published,under_development])
		# except:
		# 	pass
	return subbcategory

def get_standlist(start_url):
	bsObj = soup(start_url)
	tr = bsObj[0].find_all('tr',{'ng-show':'pChecked || pChecked == null'})
	# tr = bsObj[0].find_all('tr',{'ng-show':'uChecked || uChecked == null'})
	standlist=[]
	for td in tr:
		title = td.find('div',{'class':'entry-name entry-title'}).get_text().strip()
		standurl = 'https://www.iso.org'+td.find('div',{'class':'entry-name entry-title'}).find('a').get('href')
		summary = td.find('div',{'class':'entry-summary'}).get_text().strip()
		stage = td.find('td',{'data-title':'Stage'}).get_text().strip()
		ics = ''
		ics_lst = [iics.get_text().strip() for iics in td.find('td',{'data-title':'ICS'}).find('ul',{'class':'list-unstyled'}).find_all('a')]
		for i in ics_lst:
			ics = ics+i+','
		standlist.append([title,standurl,summary,stage,ics])
	return standlist

if __name__ == '__main__':
	conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()
	sql1 = "select categoryurl from  iso_category where categoryurl not in (select parent_url from iso_subcategory) and categoryurl not in \
	(select parent_url from iso_standlist_temp)"
	cur.execute(sql1)
	m = [a[0] for a in cur.fetchall()]

	# sql2 = "select subcommittee_url from  iso_subcategory"
	# cur.execute(sql2)
	# n = [b[0] for b in cur.fetchall()]
	# stand_lst = m+n

	# sql3 = "select distinct parent_url from iso_standlist_temp"
	# cur.execute(sql3)
	# n3 = [c[0] for c in cur.fetchall()]

	for u in m[0:1]:
		# try:
		print(u)
		url = u
		print(get_subcategoryurl())
	
		# for i in get_standlist(url):
		# for i in get_subcategoryurl(url):
		# 	sql3 = '''insert into iso_standlist_temp(title,standurl,summary,stage,ics,parent_url,insert_date) \
		# 	values("%s","%s","%s","%s","%s","%s","%s")''' % (i[0],i[1],i[2],i[3],i[4],url,get_time())

		# 	print(sql3)
		# 	cur.execute(sql3)

		# conn.commit()
		# except:
		# 	pass
	conn.close()

	
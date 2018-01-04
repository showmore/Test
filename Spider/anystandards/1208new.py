# coding:utf-8
# date:2017-12-8
# author:George

import requests
from bs4 import BeautifulSoup
import pymysql
import re
import random
import lxml
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 获取即时时间
def get_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 获取随机代理ip
def get_random_ip():
	ips = []
	ip = {}
	with open("/home/george/ip.txt","r") as f:
		for i in f.readlines():
			ips.append(i)
	ip_str = random.choice(ips)
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip

# 获取furl列表
def get_furl(cur):
	sql = "select url from hybz_category where flag ='2' and url not in (select url from hybz_detail) "
	cur.execute(sql)
	return cur.fetchall()

# 根据url返回soup对象
def soup(url,ip):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	content = requests.get(url,proxies=ip,headers=headers).content
	return BeautifulSoup(content, "lxml")

#  selenium 返回bsObj
def selenium_soup(url):

	# 设置浏览器请求头
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"]= "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"

	driver = webdriver.PhantomJS(executable_path="/home/george/phantomjs",desired_capabilities = dcap)
	driver.implicitly_wait(10)
	driver.get(url)
	bsObj = BeautifulSoup(driver.page_source, "lxml")
	driver.close()
	return bsObj

#获取分类信息
def get_cate(soup):
	category = ''
	try:
		for cate in soup.find('div',{'class':'position'}).find_all('a'):
			category += cate.get_text().replace('\n','/')+'/'
	except:
		pass
	return category

#获取文档信息
def get_finfo(soup):
	finfo = {}
	for l1 in soup.find('div',{'class':'soft_l'}).find_all('li'):
		l1 = l1.get_text()
		if l1.startswith('文件大小'):
			finfo['wjdx'] = l1[5:]
		elif l1.startswith('标签'):
			finfo['bq'] = l1[3:]
		elif l1.startswith('标准语言'):
			finfo['bzyy'] = l1[5:]
		elif l1.startswith('授权形式'):
			finfo['sqxs'] = l1[5:]
		elif l1.startswith('更新时间'):
			finfo['gxsj'] = l1[5:]
	return finfo

#获取标准介绍信息
def get_intro(soup):
	intro = ''
	try:
		intro = soup.find('div',{'class':'soft_intro'}).find('div').get_text()
	except:
		pass
	return intro

#获取下载页面url
def get_dlp(soup):
	downurl = []
	try:
		dlp = soup.find('div',{'class':'soft_downurl'}).find_all('a')
		for i in dlp:
			downurl.append(i.get('href'))
	except:
		pass
	return downurl

#获取相关资料url
def get_rel(soup):
	rel = []
	try:
		rels = soup.find('div',{'class':'soft_relate'}).find_all('a')
		for i in rels:
			rel_url = i.get('href')
			rel_name = i.get_text()
			rel.append([rel_url,rel_name])
	except:
		pass
	return rel

#获取标题
def get_title(soup):
	# title = ''
	# try:
	title = soup.find('div',{'class':'soft_name'}).find_next().get_text().replace('\"','')
	# except:
	# 	pass
	return title

if __name__ == '__main__':

	# 设置浏览器请求头
	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"

	service_args=[]
	service_args.append('--load-images=no')
	service_args.append('--disk-cache=yes')
	service_args.append('--ignore-ssl-errors=true')
	driver = webdriver.PhantomJS(executable_path="/home/george/phantomjs",desired_capabilities=dcap,service_args=service_args)
	driver.implicitly_wait(5)

	conn = pymysql.connect(host='192.168.135.128', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()

	i_n = 0
	for i in get_furl(cur):
		url = i[0]
		print(url)
		i_n += 1

		driver.get(url)
		d_soup = BeautifulSoup(driver.page_source, "lxml")



		# 获取标题
		title = get_title(d_soup)

		# 下载页面link
		downloadlink = ''
		for dlp in get_dlp(d_soup):
			downloadlink += dlp + ','

		# 获取标准介绍信息
		intro = get_intro(d_soup)

		# 获取分类信息
		cate = get_cate(d_soup)

		# 文件信息
		finfo = get_finfo(d_soup)

		sql2 = "insert into hybz_detail(url,title,category,wjdx,bq,bzyy,sqxs,gxsj,intro,dllink,insert_date) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (url, title, cate, finfo['wjdx'], finfo['bq'], finfo['bzyy'], finfo['sqxs'], finfo['gxsj'], intro,downloadlink,get_time())

		print(sql2)

		for rel in get_rel(d_soup):
			sql1 = "insert into hybz_detail_relation(url,name,link,insert_date) values(\"%s\",\"%s\",\"%s\",\"%s\")" % (url,rel[1],rel[0],get_time())
			print(sql1)
			cur.execute(sql1)

		cur.execute(sql2)

		conn.commit()

	# 每关闭十次页面清一次内存
	driver.quit() if i_n % 10 == 0 else driver.close()

	cur.close()
	conn.close()




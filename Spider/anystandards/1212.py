# coding:utf-8
# date:2017-12-12
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
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib
import os

# 获取即时时间
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

# 获取dllink列表
def get_dllink(cur):
	sql = "select dllink from  hybz_detail where dllink not in (select url from hybz_dl_log)"
	cur.execute(sql)
	return cur.fetchall() 


# 根据url返回soup对象
def soup(url,ip):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	reponse = requests.get(url,proxies=ip,headers=headers)
	content = reponse.content
	return BeautifulSoup(content, "lxml"),reponse.headers,reponse.url

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


if __name__ == '__main__':

	conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()
	dllink = get_dllink(cur)
	for url in dllink:
		try:
			ip = get_random_ip()
			print(url[0])
			bsObj = soup(url[0],ip)[0]
			bsObj.find('div',{'class':'formbox'}).find('a')
			a = bsObj.find('div',{'class':'formbox'}).find('a')
			if a.get('href').startswith('/plus/download.php'):
				durl = 'http://www.anystandards.com'+a.get('href')
				print(durl)

				pat = re.compile(r'id=\w+')
				fid = pat.search(durl).group().split('=')[1]
				fn = "g:\\hybz\\"+fid+".rar"
				headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
				h_text = soup(durl,get_random_ip())
				rlink = h_text[2]
				h_server_text = h_text[1]['Content-Type']
				h_server_xpower = h_text[1]['X-Powered-By']

				if h_server_xpower == "BaiduCloud":
					sql ="insert into hybz_dl_log(url,dllink,hash,rlink,inserttime) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (url[0],durl,fid,rlink,get_time())
				elif h_server_text == "text/html" and h_server_xpower != "BaiduCloud":
					sql ="insert into hybz_dl_log(url,dllink,hash,rlink,inserttime) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (url[0],durl,fid,'Invalid Link',get_time())
				else:
					urllib.request.urlretrieve(durl,fn)
					sql ="insert into hybz_dl_log(url,dllink,hash,inserttime) values(\'%s\',\'%s\',\'%s\',\'%s\')" % (url[0],durl,fid,get_time())
				print(sql)
				cur.execute(sql)
				conn.commit()
		except:
			continue

	cur.close()
	conn.close()






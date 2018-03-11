# coding:utf-8
# date:2017-12-15
# author:George

import time
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
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip

# 获取随机user-agent
def get_random_headers():
	agents = []
	headers = {}
	with open("f://agent.txt","r") as f:
		for i in f.readlines():
			agents.append(i)
	headers['User-Agent'] = random.choice(agents).replace('\n','')
	return headers

# 获取随机代理ip
def get_random_httpip():
	ips = []
	ip = {}
	with open("f://ip.txt","r") as f:
		for i in f.readlines():
			if i.startswith('HTTP://'):
				ips.append(i)

	ip_str = random.choice(ips)
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip

# 根据url返回soup对象
def soup(url,ip,headers):
	content = requests.get(url,proxies=ip,headers=headers).content
	return BeautifulSoup(content, "lxml")

#  selenium 返回bsObj
def selenium_soup(url):

	service_args=[]
	service_args.append('--load-images=no')
	service_args.append('--disk-cache=yes')
	service_args.append('--ignore-ssl-errors=true')
	service_args.append('--ssl-protocol=any')
	service_args.append('--ignore-ssl-errors=true')

	# 新建一个“期望技能”
	dcp = DesiredCapabilities.PHANTOMJS.copy()

	# 设置浏览器请求头
	dcp["phantomjs.page.settings.userAgent"] = get_random_headers()

	# 把代理ip加入到技能中
	proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': get_random_httpip()['HTTP'][7:-1]})
	proxy.add_to_capabilities(dcp)

	driver = webdriver.PhantomJS(executable_path="phantomjs",desired_capabilities=dcp,service_args=service_args)
	driver.get(url)
	bsObj = BeautifulSoup(driver.page_source, "lxml")
	driver.close()
	return dcp


if __name__ == '__main__':
	url = 'http://www.spc.org.cn/gb168/standardonline'
	url1 = 'http://www.iptrm.com'

	# ip = get_random_ip()
	# headers = get_random_headers()

	# bsObj = soup(url1,ip,headers)

	bsObj = selenium_soup(url1)

	print(bsObj)

# coding:utf-8
# date:2017-12-15
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
from selenium.webdriver.common.keys import Keys

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

#  使用phantomjs返回bsObj，测试中......
def selenium_soup_phantomjs(url):

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
	return bsObj

#  使用firefox返回bsObj
def selenium_soup_firefox(url):
	ip = get_random_httpip()['HTTP'][7:-1]
	proxy = Proxy({'proxyType': ProxyType.MANUAL,'httpProxy': ip})
	driver=webdriver.Firefox(executable_path="geckodriver",proxy=proxy)
	driver.implicitly_wait(10)
	driver.get(url)
	return driver,ip

def get_category(soup):
	content = soup.find_all('div',{'class':'online_content'})
	for sub_content in content:
		print('-'*50)
		for a in sub_content.find_all('div',{'class':'standard'}):
			print(a.get_text())


if __name__ == '__main__':
	url = 'http://www.spc.org.cn/gb168/standardonline'
	url1 = 'http://www.iptrm.com'
	url2 = 'http://www.spc.org.cn/gb168/online/GB%252015093-1994/'
	url3 = 'http://www.spc.org.cn/gb168/standardonline/detail/'
	url4 = 'http://www.spc.org.cn/gb168/standardonline/gettype?standclass=CN'

	# 使用普通request的情况
	# print(soup(url4,get_random_ip(),get_random_headers()))
	

	# 使用火狐浏览器
	temp = selenium_soup_firefox(url)
	ip = temp[1]
	driver = temp[0]
	print(ip)

	# className = driver.find_element_by_id('submitForm').find_element_by_name('className')
	# className.send_keys('综合')
	# className = driver.find_element_by_id('submitForm').find_element_by_name('classCode')
	# classCode.send_keys('A')
	# className = driver.find_element_by_id('submitForm').find_element_by_name('classLevel')
	# classLevel.send_keys('1')
	# className = driver.find_element_by_id('submitForm').find_element_by_name('classType')
	# classType.send_keys('国内标准')

	
	# tag_a = driver.find_element_by_id('CN_list').find_element_by_tag_name('a').get_attribute("href")

	tag_js = driver.find_element_by_id('CN_list').find_element_by_link_text('A 综合').get_attribute("href")
	print(type(tag_js))
	print(unquote(tag_js,encoding = "utf-8")
	driver.execute_script(tag_js)













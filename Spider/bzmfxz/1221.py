# coding:utf-8
# date:2017-12-20
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
	reponse = requests.get(url,proxies=get_random_headers(),headers=get_random_headers(),timeout=10)
	content = reponse.content
	return BeautifulSoup(content, "lxml"),reponse.headers,reponse.url

# 获取detail页面url列表
def get_lsturl(start_url):
	print(start_url)
	reponse = soup(start_url)
	gwsp_lst = reponse[0].find('div',{'class':'mod_infolistd'}).find('ul').find_all('a')
	for i in gwsp_lst:
		print(i.get('href'))
		print(i.get_text())
		sql = '''insert into foodmate_list(url,pageurl,name,insertdate)'''




if __name__ == '__main__':
	url = 'http://down.foodmate.net/standard/sort/2/'
	get_lsturl(url)
	# for pn in range(166):
	# 	nextpage = "http://down.foodmate.net/standard/sort/2/index-%s.html" % (pn)
	# 	print(nextpage)
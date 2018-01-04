# coding:utf-8
# date:2017-12-5
# author:George

import requests
from bs4 import BeautifulSoup
import pymysql
import re
import sys
import io
import random
import lxml
import time
from selenium import webdriver
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 获取随机代理ip
def get_random_ip():
	ips = []
	ip = {}
	with open("d:\\proxies20.txt","r") as f:
		for i in f.readlines():
			ips.append(i)
	ip_str = random.choice(ips)
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip

	# 获取furl列表
def get_furl(cur):
    sql = "select url from hybz_category where flag ='2'  and url not in (select url from hybz_detail) limit 1"
    cur.execute(sql)
    return cur.fetchall()


# 根据url返回soup对象
def soup(url,ip):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	content = requests.get(url,proxies=ip,headers=headers).content
	soup = BeautifulSoup(content, "lxml")
	return soup

if __name__ == '__main__':

	conn = pymysql.connect(host='192.168.17.128', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()

	for i in get_furl(cur):
		url = 'http://www.anystandards.com/qiche/22642.html'
		print(url)
		bsObj = soup(url,get_random_ip())
		print(bsObj)

	cur.close()
	conn.close()




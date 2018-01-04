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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


# 随机获取代理IP
def get_random_ip():
	url = 'http://www.xicidaili.com/nn/'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
	web_data = requests.get(url, headers=headers)
	soup = BeautifulSoup(web_data.text, "html.parser")
	ips = soup.find_all('tr')
	ip_list = []
	for i in range(1, len(ips)):
		ip_info = ips[i]
		tds = ip_info.find_all('td')
		ip_list.append(tds[5].text+'://'+tds[1].text + ':' + tds[2].text)
	ip = {}
	ip_str = random.choice(ip_list)
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip






# 根据url返回soup对象
def soup(url,ip):
	content = requests.get(url,proxies=ip).content
	soup = BeautifulSoup(content, "lxml")
	return soup

# 获取category信息
def get_category(soup):
	category = soup.find_all('li',{'class':'bg2'})
	cate_l = []
	for i in category:
		cate_l.append(['http://www.anystandards.com'+i.a.get('href'),i.get_text()])
	return cate_l

# 获取category_url
def get_category_url(cur):
	sql ="select url from hybz_category where parent='0'"
	cur.execute(sql)
	return cur.fetchall()

#获取nextpage url
def get_nextpg(soup,base_url):
	# 获取下一页url
	np = ''
	for pagnav in soup.find('div',{'class':'list_page'}).find_all('a'):
		if pagnav.get_text() == '下一页':
			np = base_url+pagnav.get('href')
	return np


# 获取标准详情页面url列表
def get_list_url(soup):
	bz_lst = []
	bz_lst_bsObj = soup.find_all('div',{'class':'listbox'})
	for b in bz_lst_bsObj:
		if b.a is not None:
			bz_lst.append(['http://www.anystandards.com'+b.find('a').get('href'),b.find('a').get_text()])
	return bz_lst


if __name__ == '__main__':
	conn = pymysql.connect(host='192.168.17.128', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()

	def get_furl(url,cur):
		d_soup = soup(url,get_random_ip())
		for j in get_list_url(d_soup):
			sql1 = 'insert into hybz_category(url,parent,flag) values(\'%s\',\'%s\',\'%s\')' % (j[0],url,'2')
			print(sql1)
			cur.execute(sql1)
			conn.commit()
		try:
			url = get_nextpg(d_soup,d_url[0])
			for k in get_furl(url,cur):
				sql2 = 'insert into hybz_category(url,parent,flag) values(\'%s\',\'%s\',\'%s\')' % (k[0],k[1],'2')
				print(sql2)
				cur.execute(sql2)
				conn.commit()
		except:
			pass

	# 获取标准详情页面url列表
	# for d_url in get_category_url(cur):

	# 	get_furl(d_url[0],cur)

	# 测试 get_nextpg
	# url ='http://www.anystandards.com/industry/cjt/list-6.html'
	# base_url ='http://www.anystandards.com/industry/cjt/'
	# print(get_nextpg(soup(url,get_random_ip()),base_url))
			
	# 测试 get_random_ip()


	print(get_random_ip())

	cur.close()
	conn.close()



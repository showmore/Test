# IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
# 仅仅爬取首页IP地址就足够一般使用

from bs4 import BeautifulSoup
import requests
import random

def get_ips(num):
	ip_list = []
	for pn in range(num):
		url = 'http://www.xicidaili.com/nn/'+str(num)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
		web_data = requests.get(url, headers=headers)
		soup = BeautifulSoup(web_data.text, "html.parser")
		ips = soup.find_all('tr')

		for i in range(1, len(ips)):
			ip_info = ips[i]
			tds = ip_info.find_all('td')
			url = tds[5].text+'://'+tds[1].text + ':' + tds[2].text
			wl = '{\'%s\':\'%s\'}' % (tds[5].text,url)
			ip_list.append(wl)
			print(wl)
	return ip_list

def get_random_ip():
	ips = []
	with open("d:\\proxies20.txt","r") as f:
		for i in f.readlines():
			ips.append(i)
	return random.choice(ips)

if __name__ == '__main__':

	
    print(get_random_ip())


# -*- coding: UTF-8 -*- 

import random
import requests
from lxml import etree


def get_proxies():
	url = 'http://proxy.ipcn.org/country/'
	xpath = '/html/body/div[last()]/table[last()]/tr/td/text()'

	r = requests.get(url)
	tree = etree.HTML(r.text)

	results = tree.xpath(xpath)
	proxies_list = [line.strip() for line in results]
	proxies = [i for i in proxies_list if i !='']
	proxies = random.choice(proxies)
	return proxies

if __name__ == '__main__':
	
	print(get_proxies())


import requests
from bs4 import BeautifulSoup
import re
import sys
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


# 获取代理IP
def get_random_ip():
	ips = []
	ip = {}
	with open("d:\\proxies20.txt","r") as f:
		for i in f.readlines():
			ips.append(i)
	ip_str = random.choice(ips)
	ip[re.split('://',ip_str)[0]] = ip_str
	return ip

def soup(url,ip,cookies):
    content = requests.get(url,proxies=ip,cookies=cookies).content
    soup = BeautifulSoup(content, "html.parser")
    return soup


if __name__ == '__main__':
	
	cookies = {"Hm_lvt_215fd5dde5106dd9a692498f0563696b":"1512453285,1512453738"
	,"Hm_lpvt_215fd5dde5106dd9a692498f0563696b":"1512453777"
	,"UM_distinctid":"160253dab9cca-079958c227dc24-173a7640-1fa400-160253dab9d359"
	,"SSOTOKEN":"beacon!76873FDF884A480C91BBBA592F8E6FFC77329EB04EF10C7F5142B676111F70EE6082929ACE384B471996FE516D078CF8CFA1BD371472EFAB5BBA12DF9AA2AB72"
	,"Hm_lvt_c30cfe64c111172dcd13abe3d7532080":"1512453755"
	,"Hm_lpvt_c30cfe64c111172dcd13abe3d7532080":"1512455084"
	,"JSESSIONID":"A05453837B2FE323FEC255868E36F25B"}

	ip = get_random_ip()

	url = 'http://www.so.iptrm.com/app/authorization?isNewWindow=yes&patentLib=&patentType=&select-key%3Apd=20140702&select-key%3Apns=CN302864869S&pid=PIDCNS0201407020000000030286411460528FN017480&_sessionID='



	bsObj = soup(url,ip,cookies)
	tb = bsObj.find('table',{'class':'qwb_box_tab'})

	for i in tb.find_all('tr'):
		print(i.find_all('td')[0].get_text().replace(' ',''))

	


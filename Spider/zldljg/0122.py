# coding:utf-8
# date:2018-01-11
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
import json
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType


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
    reponse = requests.post(url,proxies=get_random_ip(),headers=get_random_headers(),timeout=10)
    content = reponse.content
    return BeautifulSoup(content, "lxml"),reponse.headers

def selenium_soup_firefox(url):
    ip = get_random_httpip()['HTTP'][7:-1]
    proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': ip})
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.dir', 'G:\\')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
    driver = webdriver.Firefox(executable_path="geckodriver", proxy=proxy)
    driver.get(url)
    return driver

if __name__ == '__main__':
    # url = 'http://www.acpaa.cn/view/findAgency.jhtml?agencyId=11&shopname=&contact=&area=&x=70&y=14'

    conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
    cur = conn.cursor()

    def get_list(url):
        driver = selenium_soup_firefox(url)

        bs = BeautifulSoup(driver.page_source, "lxml")
        trs = bs.find('table',{'class':'data_f'}).find_all('tr')
        for tr in trs[1:]:
            # print(tr.find_all('td'))
            lines = []
            for td in tr.find_all('td'):
                if td.get_text() == "查看详细":
                    xq = td.find('a').get('href')
                    lines.append(xq)
                else:
                    lines.append(td.get_text())


            sql = '''insert into acpaa_lst(jgdm,jgzh,jgmc,jglb,fzr,dy,detail_url,insert_date) values("%s","%s","%s","%s","%s","%s","%s","%s")''' % (lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],'http://www.acpaa.cn'+lines[7],get_time())
            print(sql)
            cur.execute(sql)
        conn.commit()

        # # 下一页
        # np = driver.find_element_by_class_name('nextPage').get_attribute("href")
        # np = urllib.parse.unquote(np, encoding="utf-8")
        # driver.execute_script(np)
        # # np.click() if np else null
        # get_list()

        driver.close()

    for i in range(35,36):
        url2  = 'http://www.acpaa.cn/view/findAgency.jhtml?pageNumber=%s' % i
        print(url2)

        get_list(url2)

    cur.close()
    conn.close()


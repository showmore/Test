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
import os


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

def get_detail_link():
    sql = 'select detail_url from acpaa_lst'
    cur.execute(sql)
    tmp = cur.fetchall()
    return tmp

def get_info_link():
    sql = 'select zyz_url from acpaa_proxy where fzrq is null'
    cur.execute(sql)
    tmp = cur.fetchall()
    return tmp

def get_pic_url():
    sql ='''select txpic from acpaa_proxy where txpic != 'http://www.acpaa.cn/resources/agent/images/nopic.gif' '''
    cur.execute(sql)
    tmp = cur.fetchall()
    return tmp



if __name__ == '__main__':
    url = 'http://www.acpaa.cn/view/agencyDetail.jhtml?id=827&pageNumbe=1'

    conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
    cur = conn.cursor()

    def get_detail(url):
        driver = selenium_soup_firefox(url)
        bs = BeautifulSoup(driver.page_source, "lxml")
        lianxis = bs.find('table',{'class':'ksuang'}).find_all('td',{'class':'lan12xi'})
        jcxx = {}
        for i in lianxis:
            # print(i.get_text())
            if i.get_text().startswith('名　称：'):
                jcxx['mc'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('负责人：'):
                jcxx['fzr'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('成立日：'):
                jcxx['clr'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('电　话：'):
                jcxx['dh'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('传　真：'):
                jcxx['cz'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('网　址：'):
                jcxx['wz'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('邮　箱：'):
                jcxx['yx'] = re.split('：',i.get_text())[1]
            elif i.get_text().startswith('地　址：'):
                jcxx['dz'] = re.split('：',i.get_text())[1]

        sql1 = '''insert into acpaa_detail(url,mc,fzr,clr,dh,cz,wz,yx,dz,insert_date) \
        values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' \
        % (url,jcxx['mc'],jcxx['fzr'],jcxx['clr'],jcxx['dh'],jcxx['cz'],jcxx['wz'],jcxx['yx'],jcxx['dz'],get_time())
        print('*'*100)
        print(sql1)
        cur.execute(sql1)

        tb = bs.find_all('table',{'bgcolor':'#e8e8e8'})
        for tr in tb:
            print('*'*66)
            #获取相片链接
            txpic = 'http://www.acpaa.cn'+tr.find('td',{'rowspan':'6'}).find('img').get('src')

            # 获取执业证号
            zyzh = tr.find('a',{'class':'laingidi'}).get_text()
            zyzh = re.split('：',zyzh)[1]
            zyz_url = 'http://www.acpaa.cn'+tr.find('a',{'class':'laingidi'}).get('href')

            # 获取代理人基础信息
            xb = tr.find_all('td',{'height':'20'})
            for ixb in xb:
                ixb = ixb.get_text()
                if ixb.startswith('性　　别：'):
                    sex = re.split('：',ixb)[1]
                elif ixb.startswith('所学专业：'):
                    sxzy = re.split('：',ixb)[1]
                elif ixb.startswith('资格证号：'):
                    zgzh = re.split('：',ixb)[1]

            # 获取姓名
            xm = tr.find('span',{'class':'lan12xi'}).get_text()

            sql2 = '''insert into acpaa_proxy(url,zgzh,xm,sex,sxzy,zyzh,txpic,zyz_url,insert_date) \
            values("%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (url,zgzh,xm,sex,sxzy,zyzh,txpic,zyz_url,get_time())

            print(sql2)
            cur.execute(sql2)
        conn.commit()
        driver.close()

    

    def get_fzrq(url):
        driver = selenium_soup_firefox(url)
        bs = BeautifulSoup(driver.page_source, "lxml")
        fzrq = bs.find_all('td',{'class':'xjcu18zi'})
        fzrq = fzrq[1].get_text()
        driver.close()
        return fzrq

    # detail_url = get_detail_link()
    # for i in detail_url:
    #     print(i[0])
    #     get_detail(i[0])

    # for i in get_info_link():
    #     print(i[0])
    #     get_fzrq(i[0])
    #     sql = '''update acpaa_proxy set fzrq = "%s" where zyz_url = "%s" ''' % (get_fzrq(i[0]),i[0])
    #     print(sql)
    #     cur.execute(sql)
    #     conn.commit()
    s1 = set()
    for i in os.listdir('G:\\proxy_pic'):
        s1.add(i[9:])


    for i in get_pic_url():
        dllink = i[0]
        picname = re.split('/',i[0])[-1]
        if picname not in s1:
            fn = 'G:\\proxy_pic'+'\\'+picname
            print(dllink)
            try:
                urllib.request.urlretrieve(dllink, fn)
                print(fn)
            except:
                pass
        


    cur.close()
    conn.close()


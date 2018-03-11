# coding:utf-8
# date:2017-12-20
# author:George

import time
import requests
from bs4 import BeautifulSoup
import pymysql
import re
import random
import lxml
import urllib
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import socket


# 获取即席时间
def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


# 获取随机代理ip
def get_random_ip():
    ips = []
    ip = {}
    with open("/home/george/ip.txt", "r") as f:
        for i in f.readlines():
            ips.append(i)
    ip_str = random.choice(ips)
    ip[re.split('://', ip_str)[0]] = ip_str.replace('\n', '')
    return ip


# 获取随机代理ip
def get_random_httpip():
    ips = []
    ip = {}
    with open("/home/george/ip.txt", "r") as f:
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
    with open("/home/george/agent.txt", "r") as f:
        for i in f.readlines():
            agents.append(i)
    headers['User-Agent'] = random.choice(agents).replace('\n', '')
    return headers


# 根据url返回soup对象
def soup(url):
    reponse = requests.get(url, proxies=get_random_headers(), headers=get_random_headers(), timeout=10)
    content = reponse.content
    return BeautifulSoup(content, "lxml"), reponse.headers, reponse.url


# 获取detail页面url列表
def get_lsturl(start_url, conn):
    print(start_url)
    reponse = soup(start_url)
    gjb_lst = reponse[0].find_all('div', {'class': 'childclasslist_title'})

    for i in gjb_lst:
        detail_url = 'http://www.bzmfxz.com' + i.find('a').get('href')
        detail_name = i.find('a').get_text()
        sql = ''' insert into gjb_list(url,name,page_url,insertdate) values(\"%s\",\"%s\",\"%s\",\"%s\") ''' % (
        detail_url, detail_name, start_url, get_time())
        print(sql)
        conn.cursor().execute(sql)

    conn.commit()

    # 递归获取下一页，并递归
    try:
        nextpage = 'http://www.bzmfxz.com' + reponse[0].find('span', {'id': 'pe100_page_infolist'}).find('a',string='下一页').get('href')
    except:
        print("The end page!")
    else:
        get_lsturl(nextpage, conn)


# 从数据库中获取detail页面url列表
def get_db_lsturl(conn):
    cur = conn.cursor()
    sql = "select url from gjb_list where dlp_url is null"
    cur.execute(sql)
    cur.close()
    return [a[0] for a in cur.fetchall()]


def get_dlp_url(url):
    reponse = soup(url)
    m = ''
    try:
        dlp = reponse[0].find('a', {'class': 'STYLE1'}).get('onclick')
        m = re.match(".*\((.*)\).*", dlp)
        m = "http://www.bzmfxz.com" + m.group(1).replace("'", "")
    except:
        pass
    finally:
        return m


def get_db_dlpurl(conn):
    cur = conn.cursor()
    sql = '''select dlp_url from gjb_list where dl_url is null'''
    cur.execute(sql)
    cur.close()
    return [a[0] for a in cur.fetchall()]


def selenium_soup_firefox(url):
    ip = get_random_httpip()['HTTP'][7:-1]
    proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': ip})
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference('browser.download.dir', '/home/george/GJB/')
    # profile.set_preference('browser.download.folderList', 2)
    # profile.set_preference('browser.download.manager.showWhenStarting', False)
    # profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
    driver = webdriver.Firefox(executable_path="geckodriver", proxy=proxy)
    driver.get(url)
    return driver, ip


if __name__ == '__main__':
    start_url = 'http://www.bzmfxz.com/biaozhun/Soft/GJBGJJYBZ/List_1.html'

    conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')

    for idx, i in enumerate(get_db_dlpurl(conn)):
        print(i)
        try:
            temp = selenium_soup_firefox(i)
            ip = temp[1]
            driver = temp[0]
            print(ip)

            locator = (By.ID, 'ShowDownloadUrl')
            WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located(locator))

            try:
                dllink = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/form/div[2]/table/tbody/tr/td/a').get_attribute("href")
                fn = "/home/george/GJB/" + re.split('/', dllink)[-1]

                # 设置超时时间为30s
                socket.setdefaulttimeout(30)
                # 解决下载不完全问题且避免陷入死循环
                try:
                    urllib.request.urlretrieve(dllink, fn)
                    sql = '''update gjb_list set dl_url = \"%s\" where dlp_url = \"%s\"''' % (dllink, i)
                except socket.timeout:
                    count = 1
                    while count <= 3:
                        try:
                            urllib.request.urlretrieve(dllink, fn)
                            sql = '''update gjb_list set dl_url = \"%s\" where dlp_url = \"%s\"''' % (dllink, i)
                        except socket.timeout:
                            err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                            print(err_info)
                            count += 1
                    if count > 3:
                        print("downloading fialed!")
                        sql = '''update gjb_list set dl_url = \"%s\" where dlp_url = \"%s\"''' % ("pass", i)

                print(sql)
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
            except:
                sql = '''update gjb_list set dl_url = \"%s\" where dlp_url = \"%s\"''' % ("pass", i)
            finally:
                driver.close()
        except:
            pass


    conn.close()
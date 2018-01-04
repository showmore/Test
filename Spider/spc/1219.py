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
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 获取即时时间
def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


# 获取随机代理ip
def get_random_ip():
    ips = []
    ip = {}
    with open("f://ip.txt", "r") as f:
        for i in f.readlines():
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


# 根据url返回soup对象
def soup(url, ip, headers):
    content = requests.get(url, proxies=ip, headers=headers).content
    return BeautifulSoup(content, "lxml")


#  使用phantomjs返回bsObj，测试中......
def selenium_soup_phantomjs(url):
    service_args = []
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

    driver = webdriver.PhantomJS(executable_path="phantomjs", desired_capabilities=dcp, service_args=service_args)
    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, "lxml")
    driver.close()
    return bsObj


#  使用firefox返回bsObj
def selenium_soup_firefox(url):
    ip = get_random_httpip()['HTTP'][7:-1]
    proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': ip})
    driver = webdriver.Firefox(executable_path="geckodriver", proxy=proxy)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver,ip


def get_category(soup):
    content = soup.find_all('div', {'class': 'online_content'})
    for sub_content in content:
        print('-' * 50)
        for a in sub_content.find_all('div', {'class': 'standard'}):
            print(a.get_text())


if __name__ == '__main__':
    url = 'http://www.spc.org.cn/gb168/standardonline'
    url1 = 'http://www.iptrm.com'
    url2 = 'http://www.spc.org.cn/gb168/online/GB%252015093-1994/'
    url3 = 'http://www.spc.org.cn/gb168/standardonline/detail/'
    url4 = 'http://www.spc.org.cn/gb168/standardonline/gettype?standclass=CN'
    url5 = 'http://www.spc.org.cn/gb168/basicsearch?search=a100'

    # 使用普通request的情况
    # print(soup(url4,get_random_ip(),get_random_headers()))


    # 使用火狐浏览器
    temp = selenium_soup_firefox(url5)
    ip = temp[1]
    driver = temp[0]
    print(ip)

    conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
    cur = conn.cursor()

    def spider_bz():
        locator = (By.ID, 'footer')
        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located(locator))
        page_url = driver.current_url
        print(page_url)
        #列表页
        detail_list = driver.find_elements_by_link_text('详细信息')
        begin_page = driver.current_window_handle
        for i in detail_list:
            i.click() #打开该页所有标准链接

        handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
        for handle in handles:# 切换窗口
            if handle != begin_page:
                print ('switch to ',handle,'......')
                driver.switch_to_window(handle)
                print ('-'*20,driver.current_window_handle,'-'*20) # 输出当前窗口句柄
                print(driver.current_url)

                def get_detail():
                    locator = (By.ID, 'footer')
                    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
                    bz_detail = {}
                    bz_detail['dzbjg'] = driver.find_element_by_xpath('/html/body/div[4]/div[3]/table/tbody/tr[2]/td[3]').text
                    bz_detail['bzjj'] = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div').text
                    bz_detail['bzh'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[1]').text
                    bz_detail['bzmc'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[2]').text
                    bz_detail['ywmc'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[3]').text
                    bz_detail['bzzt'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[4]').text
                    bz_detail['fbrq'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[5]').text
                    bz_detail['ssrq'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[6]').text
                    bz_detail['cbyz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/ul/li[7]').text
                    bz_detail['ics'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[2]/ul/li[1]').text
                    bz_detail['zbflh'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[2]/ul/li[2]').text
                    bz_detail['tdbz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[1]').text
                    bz_detail['btdbz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[2]').text
                    bz_detail['yybz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[3]').text
                    bz_detail['cybz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[4]').text
                    bz_detail['cbmc'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[5]').text
                    bz_detail['cbcd'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[3]/ul/li[6]').text
                    bz_detail['ys'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[1]').text
                    bz_detail['zs'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[2]').text
                    bz_detail['kb'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[3]').text
                    bz_detail['bc'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[4]').text
                    bz_detail['caiys'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[5]').text
                    bz_detail['chays'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[6]').text
                    bz_detail['ywdzb'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[7]').text
                    bz_detail['ywcstp'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[8]').text
                    bz_detail['zzbcbrq'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/ul/li[9]').text
                    bz_detail['ywxgd'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[5]/ul/li[1]').text
                    bz_detail['xgdbz'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[5]/ul/li[2]').text
                    bz_detail['bzlx'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[1]').text
                    bz_detail['bzsx'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[2]').text
                    bz_detail['qcr'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[4]').text
                    bz_detail['qcdw'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[5]').text
                    bz_detail['gkdw']= driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[6]').text
                    bz_detail['tcbm'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[7]').text
                    bz_detail['fbbm'] = driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/ul/li[8]').text

                    return bz_detail
                try:
                    bz_detail = get_detail()

                    sql = '''insert into spc_detail(url,page_url,dzbjg,bzjj,bzh,bzmc,ywmc,bzzt,fbrq,ssrq,cbyz,ics,zbflh,tdbz,btdbz,yybz,cybz,cbmc,cbcd,ys,zs,kb,bc,caiys,chays,ywdzb,ywcstp,zzbcbrq,ywxgd,xgdbz,bzlx,bzsx,qcr,qcdw,gkdw,tcbm,fbbm,insertdate) VALUES(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")''' % (driver.current_url,page_url,bz_detail['dzbjg'], bz_detail['bzjj'], bz_detail['bzh'], bz_detail['bzmc'],bz_detail['ywmc'], bz_detail['bzzt'], bz_detail['fbrq'], bz_detail['ssrq'], bz_detail['cbyz'],bz_detail['ics'], bz_detail['zbflh'], bz_detail['tdbz'], bz_detail['btdbz'], bz_detail['yybz'],bz_detail['cybz'], bz_detail['cbmc'], bz_detail['cbcd'], bz_detail['ys'], bz_detail['zs'],bz_detail['kb'], bz_detail['bc'], bz_detail['caiys'], bz_detail['chays'], bz_detail['ywdzb'],bz_detail['ywcstp'], bz_detail['zzbcbrq'], bz_detail['ywxgd'], bz_detail['xgdbz'], bz_detail['bzlx'],bz_detail['bzsx'], bz_detail['qcr'], bz_detail['qcdw'], bz_detail['gkdw'], bz_detail['tcbm'],bz_detail['fbbm'], get_time())

                    print(sql)
                    cur.execute(sql)
                    conn.commit()
                except:
                    sql = '''insert into spc_detail(url,page_url,insertdate) VALUES (\"%s\",\"%s\",\"%s\")''' % (driver.current_url,page_url,get_time())
                    print(sql)
                    cur.execute(sql)
                    conn.commit()
                finally:
                    driver.close() #关闭当前窗口

        driver.switch_to_window(handles[0]) #切换原始窗口

        # 下一页
        np = driver.find_element_by_link_text('下一页').get_attribute("href")
        np = urllib.parse.unquote(np, encoding="utf-8")
        driver.execute_script(np)
        spider_bz()



    spider_bz()
    cur.close()
    conn.close()


    
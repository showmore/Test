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
    return BeautifulSoup(content, "lxml"),reponse.headers,reponse.url

if __name__ == '__main__':
    conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
    cur = conn.cursor()

    for n in [312, 282]:
        url = "http://www.std.gov.cn/hb/search/hbPage?sortOrder=asc&pageSize=100&pageNumber=%s" % (n)
        # try:
        jns = soup(url)[0].find_all('p')
        for i in jns:
            rows = i.get_text()
            s = json.loads(rows)
            pn = s['pageNumber']
            print(pn)
            # print(s['rows'])
            # print(len(s['rows']))
            for ii in s['rows']:
                # print(ii)
                # print(len(ii))
                print('*'*20)
                # print(ii['ACT_DATE'],ii['CCS'],ii['CHARGE_DEPT'],ii['C_NAME'],ii['G_ICS_NAME'])
                # print(ii['G_ICS_NAME1_1'],ii['G_STATE'],ii['G_STD_DOMAIN'],ii['G_STD_NATURE'],ii['G_TRADE_DEPT_FULL'])
                # print(ii['HISTORY_VERSION'],ii['ICS'],ii['ICS_NAME1_1'],ii['ICS_NAME1_FULL'],ii['ISSUE_DATE'])
                # print(ii['NOTICE_ID'],ii['NOTICE_NO'],ii['RECORD_NO'],ii['STATE'])
                # print(ii['STATE_ID'],ii['STD_CATEGORY'],ii['STD_CODE'],ii['STD_CODE2'],ii['STD_CODE3'])
                # print(ii['STD_CODE4'],ii['STD_CODE5'],ii['STD_DOMAIN'],ii['STD_LEVEL'],ii['STD_NATURE'])
                # print(ii['STD_ZXD'],ii['TABLE_NAME'],ii['TRADE_CLASSIFIED'],ii['TRADE_DEPT'])
                # print(ii['TRADE_DEPT_FULL'],ii['_version_'],ii['id'],ii['score'])
                # print(ii['TA_UNIT'])
                # print(ii['REVISE_STD_CODES'])
                try:
                    ACT_DATE = ii['ACT_DATE']
                except:
                    ACT_DATE = ''
                try:
                    CCS = ii['CCS']
                except:
                    CCS = ''
                try:
                    CHARGE_DEPT= ii['CHARGE_DEPT']
                except:
                    CHARGE_DEPT = ''
                try:
                    C_NAME = ii['C_NAME']
                except:
                    C_NAME = ''
                try:
                    G_ICS_NAME= ii['G_ICS_NAME']
                except:
                    G_ICS_NAME = ''
                try:
                    G_ICS_NAME1_1 = ii['G_ICS_NAME1_1']
                except:
                    G_ICS_NAME1_1 = ''
                try:
                    G_STATE = ii['G_STATE']
                except:
                    G_STATE = ''
                try:
                    G_STD_DOMAIN = ii['G_STD_DOMAIN']
                except:
                    G_STD_DOMAIN = ''
                try:
                    G_STD_NATURE = ii['G_STD_NATURE']
                except:
                    G_STD_NATURE = ''
                try:
                    G_TRADE_DEPT_FULL = ii['G_TRADE_DEPT_FULL']
                except:
                    G_TRADE_DEPT_FULL = ''
                try:
                    HISTORY_VERSION = ii['HISTORY_VERSION']
                except:
                    HISTORY_VERSION = ''
                try:
                    ICS = ii['ICS']
                except:
                    ICS = ''
                try:
                    ICS_NAME1_1 = ii['ICS_NAME1_1']
                except:
                    ICS_NAME1_1 = ''
                try:
                    ICS_NAME1_FULL = ii['ICS_NAME1_FULL']
                except:
                    ICS_NAME1_FULL = ''
                try:
                    ISSUE_DATE = ii['ISSUE_DATE']
                except:
                    ISSUE_DATE = ''
                try:
                    NOTICE_ID = ii['NOTICE_ID']
                except:
                    NOTICE_ID = ''
                try:
                    NOTICE_NO = ii['NOTICE_NO']
                except:
                    NOTICE_NO = ''
                try:
                    RECORD_NO = ii['RECORD_NO']
                except:
                    RECORD_NO = ''
                try:
                    STATE = ii['STATE']
                except:
                    STATE = ''
                try:
                    STATE_ID = ii['STATE_ID']
                except:
                    STATE_ID = ''
                try:
                    STD_CATEGORY = ii['STD_CATEGORY']
                except:
                    STD_CATEGORY = ''
                try:
                    STD_CODE = ii['STD_CODE']
                except:
                    STD_CODE = ''
                try:
                    STD_CODE2 = ii['STD_CODE2']
                except:
                    STD_CODE2 = ''
                try:
                    STD_CODE3 = ii['STD_CODE3']
                except:
                    STD_CODE3 = ''
                try:
                    STD_CODE4 = ii['STD_CODE4']
                except:
                    STD_CODE4 = ''
                try:
                    STD_CODE5 = ii['STD_CODE5']
                except:
                    STD_CODE5 = ''
                try:
                    STD_DOMAIN = ii['STD_DOMAIN']
                except:
                    STD_DOMAIN = ''
                try:
                    STD_LEVEL = ii['STD_LEVEL']
                except:
                    STD_LEVEL = ''
                try:
                    STD_NATURE = ii['STD_NATURE']
                except:
                    STD_NATURE = ''
                try:
                    STD_ZXD = ii['STD_ZXD']
                except:
                    STD_ZXD = ''
                try:
                    TABLE_NAME = ii['TABLE_NAME']
                except:
                    TABLE_NAME = ''
                try:
                    TRADE_CLASSIFIED = ii['TRADE_CLASSIFIED']
                except:
                    TRADE_CLASSIFIED = ''
                try:
                    TRADE_DEPT = ii['TRADE_DEPT']
                except:
                    TRADE_DEPT = ''
                try:
                    TRADE_DEPT_FULL = ii['TRADE_DEPT_FULL']
                except:
                    TRADE_DEPT_FULL = ''
                try:
                    version = ii['_version_']
                except:
                    version = ''
                try:
                    idn = ii['id']
                except:
                    idn = ''
                try:
                    score = ii['score']
                except:
                    score = ''
                try:
                    TA_UNIT = ii['TA_UNIT']
                except:
                    TA_UNIT = ''
                try:
                    REVISE_STD_CODES = ii['REVISE_STD_CODES'] 
                except:
                    REVISE_STD_CODES = ''

                sql = '''insert into std_hy_detail_new(ACT_DATE,CCS,CHARGE_DEPT,C_NAME,G_ICS_NAME,G_ICS_NAME1_1,\
                G_STATE,G_STD_DOMAIN,G_STD_NATURE,G_TRADE_DEPT_FULL,HISTORY_VERSION,ICS,ICS_NAME1_1,ICS_NAME1_FULL,\
                ISSUE_DATE,NOTICE_ID,NOTICE_NO,RECORD_NO,STATE,STATE_ID,STD_CATEGORY,STD_CODE,STD_CODE2,STD_CODE3,\
                STD_CODE4,STD_CODE5,STD_DOMAIN,STD_LEVEL,STD_NATURE,STD_ZXD,TABLE_NAME,TRADE_CLASSIFIED,TRADE_DEPT,\
                TRADE_DEPT_FULL,version,idn,score,TA_UNIT,REVISE_STD_CODES,pn,insert_date) \
                values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (ACT_DATE,CCS,CHARGE_DEPT,C_NAME,G_ICS_NAME,G_ICS_NAME1_1,\
                G_STATE,G_STD_DOMAIN,G_STD_NATURE,G_TRADE_DEPT_FULL,HISTORY_VERSION,ICS,ICS_NAME1_1,ICS_NAME1_FULL,\
                ISSUE_DATE,NOTICE_ID,NOTICE_NO,RECORD_NO,STATE,STATE_ID,STD_CATEGORY,STD_CODE,STD_CODE2,STD_CODE3,\
                STD_CODE4,STD_CODE5,STD_DOMAIN,STD_LEVEL,STD_NATURE,STD_ZXD,TABLE_NAME,TRADE_CLASSIFIED,TRADE_DEPT,\
                TRADE_DEPT_FULL,version,idn,score,TA_UNIT,REVISE_STD_CODES,pn,get_time())

                print(sql)
                cur.execute(sql)
            conn.commit()
        # except:
        #     pass
        time.sleep(1)
    conn.close()


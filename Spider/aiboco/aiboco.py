# -*- coding:utf-8 -*-
# date:2017-11-30
# author:George

import requests
from bs4 import BeautifulSoup
import pymysql
import re

# 获取start_url列表
def get_starturl(cur):
    sql = "select url from gwbz_category where c_name !='1' and c_name != '3' and c_parentname !='0' "
    cur.execute(sql)
    return cur.fetchall()


# 获取start_url列表
def get_detailurl(cur):
    sql = "select url from gwbz_category where c_name='3' and url not in (select url from gwbz_aiboco_detail1) limit 1"
    cur.execute(sql)
    return cur.fetchall()



# 根据url返回soup对象
def soup(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    return soup

#获取nextpage url
def get_nextpg(soup):
    nextpg = soup.find('a',attrs={'class':'next'})
    return 'http://www.aiboco.com'+nextpg.get('href')

# 获取标准url
def get_furl(soup):
    lst = []
    for i in soup.find_all('p', attrs={'class': 'w1'}):
        if i.a is not None:
            lst.append('http://www.aiboco.com' + i.a.get('href'))
    return lst


if __name__ == '__main__':
    conn = pymysql.connect(host='192.168.17.128', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
    cur = conn.cursor()

# 抓取detail_url
    def spider_detail_url():
        # 获取start_url列表
        for i in get_starturl(cur):
            print(i[0])
            start_url = i[0]

            # start_url = 'http://www.aiboco.com/Mil/index/code/3220.html'
            for i in get_furl(soup(start_url)):
                print('-'*20+start_url+'-'*20)
                print(i)
                sql = "insert into gwbz_category(c_name,c_parentname,url) values(\'%s\',\'%s\',\'%s\')" % ('3',start_url,i)
                cur.execute(sql)
                try:
                    # 有下一页时start_url重新赋值
                    start_url = get_nextpg(soup(start_url))
                except:
                    # 没有下一页时则报异常
                    pass
                else:
                    # 递归访问下一页页面
                    for j in get_furl(soup(start_url)):
                        print('-' * 20 + start_url + '-' * 20)
                        print(j)
                        sql = "insert into gwbz_category(c_name,c_parentname,url) values(\'%s\',\'%s\',\'%s\')" % (
                        '3', start_url,j)
                        cur.execute(sql)
                conn.commit()

# 抓取detail

    for i in get_detailurl(cur):
        print(i[0])

        try:
            # 获取分类描述信息
            tr1 = soup(i[0]).find_all('table',{'class':'table1'})[0].find_all('tr')
            tr_lst = []
            detail = {}
            for j in tr1:
                if len(j.find('td', class_="w1").get_text()) == 0 :
                    pass
                elif j.find('td', class_="w1").get_text() == "文档状态" :
                    wdzt = j.find('td', class_="w2").get_text().replace('\r\n','').replace(' ','')
                else:
                    detail[j.find('td', class_="w1").get_text()] = j.find('td', class_="w2").get_text().replace('\r\n','')
                    tr_lst.append(j.find('td', class_="w1").get_text() + ':' + j.find('td', class_="w2").get_text().replace('\r\n',''))
            detail['gldw'] = tr_lst[-1]
            # print(detail)
            sql1 = 'insert into gwbz_aiboco_detail1(url,bz,gafw,ms,flgs,wdzt,wdrq,scrq,wdlx,wdzs,qcjg,bzjg,xtjb,gldw) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (i[0],detail['标准'],detail['涵盖范围'],detail['描述'],detail['分类归属'],wdzt,detail['文档日期'],detail['审查日期'],detail['文档类型'],detail['文档注释'],detail['起草机构'],detail['编制机构'],detail['协调级别'],detail['gldw'])
            print(sql1)
            cur.execute(sql1)
            conn.commit()





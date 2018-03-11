#-*- coding: UTF-8 -*-   
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import time
import requests
import random
from bs4 import BeautifulSoup



def get_info(url):
    info_list=[]
    data={"pageNumber":"200"}#应该就是通过传输这个pageNum给服务器实现翻页}

    content = requests.post(url,data=data).content#就是这里
    #t = session.post(url,data,headers)
    print(content)#无法print出内容，说是HTTP Status 405 - Request method 'POST' not supported


if __name__ == '__main__':
    
    url ="http://www.std.gov.cn/hb/search/hbQuery"
    get_info(url)
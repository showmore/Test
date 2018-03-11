# coding:utf-8
# date:2018-01-17
# author:George

import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import re
import os
import shutil
import pymysql

def get_gjb():
	base_path = "D:\\gjb_pdf"
	file_in_dir = [file for file in os.listdir(base_path)]
	l1 = []
	for i in file_in_dir:
		l1.append([re.split(' ',i)[1],i])
	return l1

conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
cur = conn.cursor()
for i in get_gjb():

	# print(i)
	sql = '''insert into file_gjb_statistics(code,cname) values("%s","%s")''' % (i[0],i[1])
	print(sql)
	cur.execute(sql)
conn.commit()
cur.close()
conn.close()
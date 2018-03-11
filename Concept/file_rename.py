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

def get_hybz():
	base_path = "D:\\hybz_pdf"
	file_in_dir = [file for file in os.listdir(base_path)]
	pattern = re.compile("^[a-zA-Z]+\\s+[0-9]+.*-[0-9]+")
	l1 = []
	for i in file_in_dir:
		m = pattern.search(i)

		l1.append(i.split(' ')[0])

	return l1

if __name__ == '__main__':
	conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()
	for i in get_hybz():
		# print(i)
		sql ='''insert into file_hy_statistics(category,number) values("%s","%s")''' % (i,1)
		print(sql)
		cur.execute(sql)
	conn.commit()
	cur.close()
	conn.close()
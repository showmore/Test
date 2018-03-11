# coding:utf-8
# date:2018-01-17
# author:George

import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import re
import os
import pymysql
import shutil


def get_hybz():
	base_path = "D:\\hybz_pdf"
	file_in_dir = [file for file in os.listdir(base_path)]
	pattern = re.compile("^[a-zA-Z]+\\s+[0-9]+.*-[0-9]+")
	# pattern = re.compile("[\u4e00-\u9fa5]+")
	l1 = []
	for i in file_in_dir:
		m = pattern.search(i)
		# print(i)
		# print(m.group())
		# print(i.split(' ')[0])
		l1.append(i.split(' ')[0])
		# try:
		# 	# print(m.group())
		# 	l1.append([i,m.group()])
		# except:
		# 	pass
	return l1


def copy_gjb():
	l1 = [x for x in os.listdir('D:\\gjb_pdf') if os.path.isdir('D:\\gjb_pdf\\'+x)]
	for i in l1:
		# print('D:\\gjb_pdf\\'+i)
		for ii in os.listdir('D:\\gjb_pdf\\'+i):
			if ii[-4:] == '.pdf':
				fn = 'D:\\gjb_pdf\\'+i+'\\'+ii
				print(fn)
				shutil.copy(fn,"D:\\gjb_pdf\\tmp")

if __name__ == '__main__':
	conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()
	lst = get_hybz()
	a = {}
	for i in lst:
		if lst.count(i)>1:
			a[i] = lst.count(i)
	for ii in a:
		# print(i,a[i])
		sql ='''insert into file_hy_statistics(category,number) values("%s","%s")''' % (ii,a[ii])
		print(sql)
		cur.execute(sql)

# base_path = "D:\\gjb_pdf"

# for i in traversalDir_FirstDir(base_path):
# 	print(i)
# 	sf = i
# 	tf = "D:\\gjb_pdf\\tmp"
# 	shutil.copy(sf,tf)

	conn.commit()
	cur.close()
	conn.close()

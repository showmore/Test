import re
import os
import pymysql

file_id = [n.replace('.rar','') for n in os.listdir("G:\\HYBZ")]


def delete():
	conn = pymysql.connect(host='192.168.135.129', port=3306, user='root', passwd='rootroot', db='demo', charset='utf8')
	cur = conn.cursor()

	sql1 = "select hash from hybz_dl_log"
	cur.execute(sql1)
	tl = cur.fetchall()
	for i in tl:
		for j in i:
			print(j)
			if j not in file_hash:
				sql2 = "delete from hybz_dl_log where hash = '%s'" % (j)
				print(sql2)
	cur.close()
	conn.close()


if __name__ == '__main__':

	print(len(file_id))
	print(len(set(file_id)))
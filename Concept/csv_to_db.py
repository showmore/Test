# -*- coding: UTF-8 -*- 

import csv
import pymysql

conn = pymysql.connect(host='192.168.8.69', port=3306, user='root', passwd='rootroot',\
 db='demo',charset='utf8') 
cur = conn.cursor() 
print(cur)

with open('c:\\visit_new.csv') as csvfile:
	sp =csv.reader(csvfile)
	for row in sp:
		print(row)
		a = row[0]
		b = row[1]
		print(a,b)
		sql = 'insert into dv_visit(date,name) values("%s","%s")' %(a,b)
		print(sql)
		cur.execute(sql)
conn.commit()
cur.close()




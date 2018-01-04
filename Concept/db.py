# -*- coding: UTF-8 -*- 
import csv
import pymysql
import re

conn = pymysql.connect(host='192.168.0.174', port=3306, user='vant', passwd='vant', db='zy',charset='utf8') 
cur = conn.cursor() 
cur.execute('SELECT project_info_id,technology_info FROM tbu_zy_project_info where technology_info is not null ') 
r = cur.fetchall()
dr = re.compile(r'<[^>]+>',re.S)

cur.close() 
conn.close() 


with open("c:\\csvfile.csv","w",newline='') as datacsv:
	writer=csv.writer(datacsv)
	writer.writerow(['project_info_id','technology_info'])
	for row in r:
		row0=dr.sub('',row[0])
		if row[1] is None:
			row1 = ''
		else:
			row1=dr.sub('',row[1])

		writer.writerow([row0,row1])

datacsv.close()



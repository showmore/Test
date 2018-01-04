# -*- coding: UTF-8 -*- 

import csv
import pymysql

class Mysqldb():
	def __init__(self,ip,user,pw,db):
		self.ip=ip
		self.user=user
		self.password=pw
		self.db=db

	#获取数据库连接  
	def getCon(self):  
		try:  
			conn=pymysql.connect(host=self.ip,user=self.user,password=self.password,db=self.db,\
				port=3306,charset='utf8')
			return conn
		except Exception as e:
			print(e)
	
	#查询方法，使用con.cursor(pymysql.cursors.DictCursor),返回结果为字典      
	def select(self,sql):
		try:
			conn=self.getCon()
			cur=conn.cursor()
			cur.execute(sql)
			data=cur.fetchall()
			return data
		except Exception as e:
			print(e)
		finally:
			cur.close()
			conn.close()

class Mycsv():
	def __init__(self,filename):
		self.filename=filename

	def writecsv(self,*args):
		try:
			with open(self.filename,"a+",newline='') as fn:
				writer=csv.writer(fn)
				writer.writerow(*args)
		except Exception as e:
			print(e)

if __name__ == '__main__':

	#获取数据
	gx=Mysqldb('192.168.0.174','vant','vant','gx')

	sql='SELECT enterprise_id,enterprise_name,enterprise_address,linkman,org_type FROM tbu_gx_enterprise ORDER BY enterprise_name'

	data=gx.select(sql)

	#写入数据
	c=Mycsv('f:\\csv\\test.csv')
	for l in data:
		c.writecsv(l)
		
# -*- coding: UTF-8 -*-

import pymysql
import json


class Mysqldb_dv:
	#获取数据库连接
	def getCon(self):
		try:
			#conn = MySQLdb.connect("192.168.8.68","root","rootroot","demo",charset="utf8")
			conn = pymsql.connect("192.168.0.236","select","onlyselect","dv",charset="utf8")
			return conn
		except Exception as e:  
			print (e)	

	#查询方法，使用con.cursor(MySQLdb.cursors.DictCursor),返回结果为字典
	def select(self,sql):
		try:
			con=self.getCon()   
			cur=con.cursor(pymsql.cursors.DictCursor)  
			count=cur.execute(sql)  
			fc=cur.fetchall()
			return fc  
		except Exception as e:  
			print (e)	
		finally:  
			cur.close()  
			con.close()  

db=Mysqldb_dv()
def get(in_sql):
	try:
		fc=db.select(in_sql)
		json_data=json.dumps(fc,ensure_ascii=False)
	except:
		print ('get fail...')
	else:
		return json_data

if __name__ == '__main__':
	get('select * from cat')

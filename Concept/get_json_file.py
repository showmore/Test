# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import MySQLdb
import json

def TableToJson():
	try:


# 打开数据库连接
		db = MySQLdb.connect("192.168.8.68","root","rootroot","demo",charset="utf8")

# 使用cursor()方法获取操作游标 
		cursor = db.cursor()

# 使用execute方法执行SQL语句
		cursor.execute("SELECT * FROM dv_jmhtgc ")

# 使用 fetchall() 方法获取查询结果。
		data = cursor.fetchall()

#关闭cursor
		cursor.close()

# 关闭数据库连接
		db.close()

		jsonData = []
         
		for row in data:
			result = {}
			result['year'] = row[0]
			result['hangye'] = row[1]
			result['money'] = row[2]
			result['number'] = str(row[3])
			jsonData.append(result)
			
		json_data_o=json.dumps(jsonData,ensure_ascii=False)

	except:
		print 'MySQL connect fail...'
	else:
		return json_data_o

if __name__ == '__main__':
	jsonData = TableToJson()
	
	f = open(r'C:\my_python\txt\jmhtgc.txt','w+')
	f.write(jsonData)
	f.close()
	print (jsonData)



 

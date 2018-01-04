# -*- coding=utf-8 -*-

import suds
from suds.client import Client

from suds.plugin import MessagePlugin
from suds.sax.attribute import Attribute
from db_to_csv import *
import json

def get_yq(x,y,z):
	a_url = 'http://yqgx.xatrm.com/ws_server/cxf/instru?wsdl'
	a_client = suds.client.Client(a_url)
	a = a_client.service.instrument(x,y,z)
	return a


if __name__ == '__main__':

	gx=Mysqldb('192.168.0.174','vant','vant','gx')

	sql='SELECT enterprise_id,enterprise_name,org_type FROM tbu_gx_enterprise ORDER BY enterprise_name'

	sql1 = 'SELECT achievement,cname,contact,email FROM xajtdx_instrument'

	# 从数据库中获取数据
	data=gx.select(sql1,type==1)
	for i in data:
		# print(i)
		# 转换成json串
		json_data=json.dumps(i,ensure_ascii=False)

		# 调用webservice服务发送数据
		x,y,z="CZ",5,json_data
		b = get_yq(x,y,z)
		# print(x,y,z)
		print(b)


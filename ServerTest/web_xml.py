# -*- coding=utf-8 -*-

import suds
from suds.client import Client

from suds.plugin import MessagePlugin
from suds.sax.attribute import Attribute

# QQ在线状态
def get_qq_status(qq_num):
	a_url = 'http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl'
	a_client = suds.client.Client(a_url)
	a=a_client.service.qqCheckOnline(qq_num)
	return a


# IP地址归属地
def get_ip_city(ip):
	b_url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
	b_client = suds.client.Client(b_url)
	b = b_client.service.getCountryCityByIp(ip)  
	return b

# 手机归属地
def get_phone_area(phoneCode):
	c_url = 'http://www.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
	c_client = Client(c_url)
	c = c_client.service.getMobileCodeInfo(mobileCode = phoneCode)  
	return c

#身份证号码
def get_person_card(person_card):
	d_url = 'http://www.gpsso.com/webservice/idcard/idcard.asmx?wsdl'
	d_client = Client(d_url)
	d = d_client.service.SearchIdCard(person_card)  
	return d

#查询快递
def get_kuaidi(kuaidi_compay,kuaidi_no):
	e_url = 'http://www.gpsso.com/webservice/kuaidi/kuaidi.asmx?wsdl'
	e_client = Client(e_url)
	e = e_client.service.KuaidiQuery(kuaidi_compay,kuaidi_no)
	return e


if __name__ == '__main__':
	print(get_kuaidi('中通快递','444911275961'))
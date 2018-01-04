#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def geocode(address):
	parameters = {'address': address, \
	'key': '9606cb673016b9c1a31a1b707fb14580'}
	base = 'http://restapi.amap.com/v3/geocode/geo'
	response = requests.get(base, parameters)
	answer = response.json()
	if (answer['infocode']=='10000'):
		loc=answer['geocodes'][0]['location']
		# print(answer)
		# print(address + "的经纬度：",loc)
	return loc

if __name__=='__main__':
	#address = input("请输入地址:")
	address = '上海'
	a=geocode(address)
	print(a)
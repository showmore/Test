#coding:utf-8
import sys
import os

import redis

r = redis.Redis(host="192.168.135.129",port=6379,db=0)


r.set('test','write test')

# coding:utf-8
# date:2018-01-17
# author:George

import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import re
import os
import pymysql
import shutil



s = '名　称：苏州携智汇佳专利代理事务所(普通合伙)'

rs = re.split('：',s)
print(rs[1])
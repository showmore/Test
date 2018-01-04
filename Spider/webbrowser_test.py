# -*- coding: UTF-8 -*- 

# coding: UTF-8
import webbrowser as web
import time
import os
import random

count = random.randint (3,5)
j = 0
while j <count:
	i = 0
	while i <= 3:
		web.open_new_tab('www.xatrm.com')
		i=i+1
		time.sleep(0.8)
else:
	os.system('taskkill /F /IM chrome.exe')
	print (j, 'times closing Browser !')
	j = j+1
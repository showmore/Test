# -*- coding=utf-8 -*-

import time

now_time=lambda time_n: time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_n))

def runtime(func):
	def inter():
		start_time=time.time()
		print(now_time(start_time),'start.....')
		func()
		end_time=time.time()
		print(now_time(end_time),'stop')
		print('Run times：%s seconds' % (end_time-start_time))
		return func
	return inter

if __name__ == '__main__':
	@runtime
	def a():
		print('func begin')
		time.sleep(1)
		print('1 second pass')
		time.sleep(1)
		print('func end')
	a()

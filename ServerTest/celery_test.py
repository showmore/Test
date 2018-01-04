#coding:utf-8

from celery import Celery
import time

broker = 'amqp://guest@192.168.135.129//'
# broker = 'redis://192.168.135.129:6379'
backend = 'amqp://guest@192.168.135.129//'
# backend = 'redis://192.168.135.129:6379/0'
app = Celery('tasks',broker=broker,backend=backend)

@app.task
def add(x, y):
	time.sleep(5)
	return x + y





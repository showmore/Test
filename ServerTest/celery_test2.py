#coding:utf-8

from celery_test import add

result = add.delay(234432,523452)
# print(result.ready())
print(result.get())
print('celery ok')


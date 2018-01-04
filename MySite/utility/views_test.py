# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse


def test_url(request,a):
    if a:
        html = 'test%s.html' %(a)
    else:
        html ='test.html'
    print(html)
    return render(request,html,locals())

def dv_url(request,a):
    if a:
        html = 'DataVisual/modules/%s.html' %(a)
    else:
        html = 'DataVisual/index.html'
    return render(request,html,locals())

def jiaoda_url(request):
    return render(request,'jiaoda/index.html',locals())



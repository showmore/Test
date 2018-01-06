# -*- coding: UTF-8 -*-
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from utility import models


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print(username,password)
            models.UserInfo.objects.create(user=username, pwd=password)
            request.session.set_test_cookie()
            return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf})



def login(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users = models.UserInfo.objects.filter(user__exact=username,pwd__exact=password)
            if users:
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

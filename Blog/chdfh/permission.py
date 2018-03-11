# -*- coding: UTF-8 -*-
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from chdfh import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=100,label='姓名',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=100,label='电子邮件',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='密码')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='姓名',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='密码')

def regist(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            email = uf.cleaned_data['email']
            password = uf.cleaned_data['password']
            # print(username,password)
            # models.UserInfo.objects.create(user=username, pwd=password)
            user = User.objects.create_user(username, email, password)
            user.save()

            return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(request,'regist.html',{'uf':uf})


def weblogin(request):
    if request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            # users = models.UserInfo.objects.filter(user__exact=username,pwd__exact=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                # response = HttpResponseRedirect('/index')
                # response.set_cookie('username',username,3600)
                # request.session['username'] = username
                login(request, user)
                # return response
                return render(request,'index.html',locals())
            else:
                return HttpResponseRedirect('/login')
    else:
        lf = LoginForm()
    return render(request,'login.html',{'lf':lf})


def weblogout(request):
    response = HttpResponseRedirect('/login/')
    try:
        # response.delete_cookie('username')
        # del request.session['username']
        logout(request)
    except:
        pass
    return response


# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from utility import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username,password)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)

    #从数据库读取数据
    user_list = models.UserInfo.objects.all()
    # print(str(user_list.query))

    rpath = request.path
    rhost = request.get_host()


    return render(request,"index.html",locals())

def instr(request):
    # return HttpResponse("Hello world!")

    #从数据库读取数据
    instr_list = models.xajtdx_instrument.objects.values('cname','requirement','subject','instrCategory','org','status','serviceUrl')

    subject_list = models.xajtdx_instrument.objects.values_list('subject',flat=True)\
        .exclude(subject__contains="None").distinct()

    #条件查询
    if request.method == "GET":
        eqName = request.GET.get("eqName", None)
        eqOrg = request.GET.get("eqOrg", None)
        eqSubject = request.GET.get("eqSubject", None)

        if eqName is None and eqOrg is None and eqSubject is None:
            eqName = ""
            eqOrg = ""
            eqSubject = ""
        else:
            instr_list = instr_list.filter(cname__icontains = eqName).\
                filter(org__icontains = eqOrg).filter(subject__icontains = eqSubject)


    #分页
    page = request.GET.get('page')
    paginator = Paginator(instr_list,10,3)

    print(instr_list.query)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)


    return render(request,"instrument.html",locals())

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def test_easyui(request):
    return  render(request,'test_easyui.html',locals())



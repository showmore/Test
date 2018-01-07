"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from utility import views
from utility import views_test
from utility import permission

urlpatterns = [
    url(r'^$',views.index),
    url(r'^admin/',admin.site.urls),
    url(r'^add/$',views.add,name='add'),
    url(r'^add/(\d+)/(\d+)/$',views.add2,name='add2'),
    url(r'^instr/',views.instr),
    url(r'^test_easyui/',views.test_easyui),
    url(r'^test(\d*)/$',views_test.test_url),
    url(r'^dv/(\w*)?',views_test.dv_url),
    url(r'^jiaoda/',views_test.jiaoda_url),
    url(r'^regist/$',permission.regist),
    url(r'^login/$',permission.login),
    url(r'^logout/$',permission.logout),

]


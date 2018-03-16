from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeInfo(models.Model):
    jobnumber = models.CharField(max_length=32,unique=True,verbose_name="工号")
    name = models.CharField(max_length=32,verbose_name="姓名")
    department = models.CharField(max_length=32,blank=True,verbose_name="部门")
    post = models.CharField(max_length=32,blank=True,verbose_name="岗位")
    content = models.TextField(blank=True,verbose_name="简历")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    QQ = models.CharField(max_length=128, blank=True)
    blog = models.CharField(max_length=128, blank=True)
    location = models.CharField(max_length=128, blank=True)
    occupation = models.CharField(max_length=64, blank=True)

    reward = models.IntegerField(default=0, blank=True)
    topic_count = models.IntegerField(default=0, blank=True)
    post_count = models.IntegerField(default=0, blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return "标题：{},字数：{},概要：{}".format(self.title,len(self.content),self.content[:20])

class AlcoholDetection(models.Model):
    status_type_choices = (  # 数据库只存1、2、3，后面的信息存在内存里。
        (1, '正常'),
        (2, '饮酒'),
        (3, '醉酒'),
    )

    unit_type_choices = ( #0:mg/100ml; 1:mg/ml
        (1, 'mg/100ml'),
        (2, 'mg/ml'),
    )

    jobnumber = models.ForeignKey(to='EmployeeInfo',to_field='jobnumber',verbose_name="雇员")
    concentration = models.CharField(max_length=32,blank=True,verbose_name="酒精浓度")
    status = models.IntegerField(choices=status_type_choices,default=1,verbose_name="状态")
    unit = models.IntegerField(choices=unit_type_choices,default=1,blank=True,verbose_name="单位")
    date = models.DateField(blank=True,verbose_name="日期")
    time = models.TimeField(verbose_name="时间")
    picurl = models.CharField(max_length=255,blank=True,verbose_name="相片地址")


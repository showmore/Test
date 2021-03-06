# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-13 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chdfh', '0005_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlcoholDetection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration', models.CharField(max_length=32, verbose_name='酒精浓度')),
                ('status', models.CharField(max_length=32, verbose_name='状态')),
                ('unit', models.CharField(max_length=32, verbose_name='单位')),
                ('date', models.DateField(verbose_name='日期')),
                ('time', models.TimeField(verbose_name='时间')),
                ('picurl', models.CharField(max_length=255, verbose_name='相片地址')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobnumber', models.CharField(max_length=32, verbose_name='工号')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('content', models.TextField(verbose_name='简历')),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.AddField(
            model_name='alcoholdetection',
            name='jobnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empid', to='chdfh.EmployeeInfo', verbose_name='工号'),
        ),
    ]

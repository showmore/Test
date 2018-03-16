# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-13 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chdfh', '0006_auto_20180313_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoholdetection',
            name='concentration',
            field=models.CharField(blank=True, max_length=32, verbose_name='酒精浓度'),
        ),
        migrations.AlterField(
            model_name='alcoholdetection',
            name='date',
            field=models.DateField(blank=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='alcoholdetection',
            name='picurl',
            field=models.CharField(blank=True, max_length=255, verbose_name='相片地址'),
        ),
        migrations.AlterField(
            model_name='alcoholdetection',
            name='status',
            field=models.CharField(choices=[(1, '正常'), (2, '饮酒'), (3, '醉酒')], default=1, max_length=32, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='alcoholdetection',
            name='unit',
            field=models.CharField(blank=True, choices=[(1, 'mg/100ml'), (2, 'mg/ml')], default=1, max_length=32, verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='content',
            field=models.TextField(blank=True, verbose_name='简历'),
        ),
    ]

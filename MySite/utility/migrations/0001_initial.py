# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='xajtdx_instrument',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('eqid', models.CharField(max_length=50)),
                ('instruType', models.CharField(max_length=50)),
                ('cname', models.CharField(max_length=200)),
                ('ename', models.CharField(max_length=200)),
                ('innerId', models.CharField(max_length=50)),
                ('instrBelongsType', models.CharField(max_length=50)),
                ('InstrBelongsName', models.CharField(max_length=50)),
                ('instrCategory', models.CharField(max_length=50)),
                ('instrCategoryName', models.CharField(max_length=50)),
                ('instrSource', models.CharField(max_length=50)),
                ('instrSupervise', models.CharField(max_length=50)),
                ('worth', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('beginDate', models.DateTimeField()),
                ('type', models.CharField(max_length=50)),
                ('instrVersion', models.CharField(max_length=50)),
                ('technical', models.CharField(max_length=50)),
                ('function', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('serviceContent', models.CharField(max_length=50)),
                ('achievement', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('requirement', models.CharField(max_length=50)),
                ('fee', models.CharField(max_length=50)),
                ('serviceUrl', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('postalcode', models.CharField(max_length=50)),
                ('shareMode', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('isshow', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField()),
                ('createUser', models.CharField(max_length=50)),
                ('updateDate', models.DateTimeField()),
                ('updateUser', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='xajtdx_instrument_test',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('instruType', models.CharField(max_length=50)),
                ('achievement', models.CharField(max_length=50)),
                ('cname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('establish', models.DateTimeField()),
                ('fee', models.CharField(max_length=50)),
                ('innerId', models.CharField(max_length=50)),
                ('insCode', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('postalCode', models.CharField(max_length=50)),
                ('requirement', models.CharField(max_length=50)),
                ('serviceContent', models.CharField(max_length=50)),
                ('serviceUrl', models.CharField(max_length=50)),
                ('shareMode', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('eqType', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('beginDate', models.DateTimeField()),
                ('ename', models.CharField(max_length=50)),
                ('function', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('technical', models.CharField(max_length=50)),
                ('worth', models.CharField(max_length=50)),
                ('instrBelongsType', models.CharField(max_length=50)),
                ('instrBelongsName', models.CharField(max_length=50)),
                ('instrCategory', models.CharField(max_length=50)),
                ('instrSource', models.CharField(max_length=50)),
                ('instrSupervise', models.CharField(max_length=50)),
                ('instrVersion', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('codeCpd', models.CharField(max_length=50)),
                ('numberCpd', models.CharField(max_length=50)),
                ('declarationNumber', models.CharField(max_length=50)),
                ('contractNumber', models.CharField(max_length=50)),
                ('importPort', models.CharField(max_length=50)),
                ('responsibleCustoms', models.CharField(max_length=50)),
                ('importDate', models.DateTimeField()),
                ('share', models.CharField(max_length=50)),
                ('feesApproved', models.CharField(max_length=50)),
                ('hsCode', models.CharField(max_length=50)),
                ('record', models.CharField(max_length=50)),
                ('amounts', models.CharField(max_length=50)),
                ('serviceTime', models.DateTimeField()),
                ('serviceWay', models.CharField(max_length=50)),
                ('serviceAmount', models.CharField(max_length=50)),
                ('subjectName', models.CharField(max_length=50)),
                ('subjectIncome', models.CharField(max_length=50)),
                ('subjectArea', models.CharField(max_length=50)),
                ('subjectContent', models.CharField(max_length=50)),
                ('applicant', models.CharField(max_length=50)),
                ('applicantPhone', models.CharField(max_length=50)),
                ('applicantEmail', models.CharField(max_length=50)),
                ('applicantUnit', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
    ]

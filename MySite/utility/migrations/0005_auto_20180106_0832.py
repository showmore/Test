# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_merge_20180106_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='amounts',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='applicantEmail',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='applicantPhone',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='applicantUnit',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='city',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='codeCpd',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='contractNumber',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='county',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='declarationNumber',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='eqType',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='establish',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='feesApproved',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='hsCode',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='importDate',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='importPort',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='insCode',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='instrBelongsName',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='level',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='numberCpd',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='postalCode',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='province',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='record',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='responsibleCustoms',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='serviceAmount',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='serviceTime',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='serviceWay',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='share',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='subjectArea',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='subjectContent',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='subjectIncome',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='subjectName',
        ),
        migrations.RemoveField(
            model_name='xajtdx_instrument',
            name='url',
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='InstrBelongsName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='createDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='createUser',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='eqid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='instrCategoryName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='isshow',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='org',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='postalcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='updateDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='xajtdx_instrument',
            name='updateUser',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='achievement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='beginDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='cname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='ename',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='function',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='innerId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instrBelongsType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instrCategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instrSource',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instrSupervise',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instrVersion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='instruType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='nation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='requirement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='serviceContent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='serviceUrl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='shareMode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='technical',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='xajtdx_instrument',
            name='worth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

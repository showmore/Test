# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chdfh', '0002_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]

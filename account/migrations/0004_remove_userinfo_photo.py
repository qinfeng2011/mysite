# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20171204_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='photo',
        ),
    ]
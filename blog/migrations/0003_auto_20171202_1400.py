# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 06:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171202_1357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogArticls',
            new_name='BlogArticles',
        ),
    ]

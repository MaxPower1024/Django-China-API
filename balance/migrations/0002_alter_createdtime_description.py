# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='描述'),
        ),
    ]

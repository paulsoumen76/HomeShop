# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-17 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeshop', '0002_auto_20200616_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ordertable',
            name='user_name',
            field=models.CharField(max_length=5),
        ),
    ]
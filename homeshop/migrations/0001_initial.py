# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-16 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=20)),
                ('mobile_cost', models.FloatField()),
                ('mobile_desc', models.TextField()),
                ('mobile_img', models.ImageField(null=True, upload_to='mobile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('location2', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('zip_code', models.IntegerField(null=True)),
                ('item_json', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

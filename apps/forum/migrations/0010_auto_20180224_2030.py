# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-24 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20180222_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='illustration',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%'),
        ),
    ]

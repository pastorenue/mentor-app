# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-21 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20180221_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='shares',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
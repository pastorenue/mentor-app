# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170901_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
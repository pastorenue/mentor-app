# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-10 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0007_auto_20171009_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
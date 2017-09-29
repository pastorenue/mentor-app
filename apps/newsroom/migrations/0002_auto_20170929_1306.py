# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='sub_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 18:08
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]

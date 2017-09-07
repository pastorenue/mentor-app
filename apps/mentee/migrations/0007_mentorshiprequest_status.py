# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0006_auto_20170829_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorshiprequest',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('A', 'Accepted'), ('D', 'Denied')], default='O', max_length=1),
        ),
    ]

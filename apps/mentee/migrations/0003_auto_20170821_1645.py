# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0002_auto_20170821_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='email',
        ),
        migrations.AlterField(
            model_name='mentee',
            name='mode_details',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Please give details for the mode chosen above'),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='mode_of_communication',
            field=models.CharField(blank=True, choices=[('whatsapp', 'Whatsapp'), ('email', 'Email'), ('call', 'Phone call'), ('f2f', 'Face-to-Face'), ('skype', 'Skype')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='name_of_business',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
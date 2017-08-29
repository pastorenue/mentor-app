# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentee', '0005_auto_20170821_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentorshiprequest',
            options={'ordering': ('-date_created',), 'verbose_name': 'Mentorship Request', 'verbose_name_plural': 'Mentorship Requests'},
        ),
        migrations.RemoveField(
            model_name='mentorshiprequest',
            name='from_user',
        ),
        migrations.AddField(
            model_name='mentee',
            name='background_image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='mentorshiprequest',
            name='mentee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentorshiprequest',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_received', to=settings.AUTH_USER_MODEL),
        ),
    ]

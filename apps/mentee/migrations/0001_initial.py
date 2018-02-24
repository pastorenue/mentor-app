# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-24 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.'), ('Alhaji', 'Alhaji'), ('Chief', 'Chief'), ('Prince', 'Prince'), ('Princess', 'Princess')], max_length=10)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d')),
                ('background_image', models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d')),
                ('age_range', models.CharField(blank=True, choices=[('25-30', '25-30 years'), ('31-35', '31-35 years'), ('36-40', '36-40 years'), ('41-50', '41-50 years'), ('51-60', '51-60 years'), ('60+', '60+ years')], max_length=5, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('level_of_education', models.CharField(blank=True, choices=[('SSCE', 'SSCE'), ('OND', 'OND'), ('HND', 'HND'), ('BSc and MSc', 'BSc and MSc'), ('PhD', 'PhD')], max_length=27, null=True)),
                ('name_of_business', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('year_of_commencement', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018)),
                ('time_with_mentor', models.CharField(blank=True, choices=[('forth-nightly', 'Forth-nightly'), ('monthly', 'Monthy')], max_length=20, null=True, verbose_name='How much time would you need from your mentor?')),
                ('mode_of_communication', models.CharField(blank=True, choices=[('whatsapp', 'Whatsapp'), ('email', 'Email'), ('call', 'Phone call'), ('f2f', 'Face-to-Face'), ('skype', 'Skype')], max_length=50, null=True)),
                ('mode_details', models.CharField(blank=True, max_length=50, null=True, verbose_name='Please give details for the mode chosen above')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expert.Address')),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expert.Industry')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MentorshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('O', 'Open'), ('A', 'Accepted'), ('D', 'Denied')], default='O', max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expert.Industry')),
                ('mentee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
                'verbose_name': 'Mentorship Request',
                'verbose_name_plural': 'Mentorship Requests',
            },
        ),
    ]

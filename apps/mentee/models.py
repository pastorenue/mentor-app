from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.conf import settings


class Mentee(models.Model):
	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
		YEAR_CHOICES.append((r,r))

	TIME_CHOICES = (
		('forth-nightly', 'Forth-nightly'),
		('monthly', 'Monthy')
	)

	QUALIFICATION_CHOICES = (
		('SSCE', 'SSCE'),
		('OND', 'OND'),
		('HND', 'HND'),
		('BSc and MSc', 'BSc and MSc'),
		('PhD', 'PhD')
	)

	title = models.CharField(max_length=10, choices=settings.TITLE_CHOICES)
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12)
	level_of_education = models.CharField(max_length=7, choices=QUALIFICATION_CHOICES)
	name_of_business = models.CharField(max_length=50)
	industry = models.ForeignKey("expert.Industry")
	address = models.ForeignKey("expert.Address")
	slug = models.SlugField(unique=True)
	year_of_commencement = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year) 
	time_with_mentor = models.CharField("How much time would need from your mentor?", max_length=20, choices=TIME_CHOICES)
	model_of_communication = models.OneToOneField('mentee.CommunicationMode')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		pass


class MentorshipRequest(models.Model):
	from_user= models.ForeignKey(User, related_name='from_user')
	industry = models.ForeignKey('expert.Industry')
	to_user = models.ForeignKey(User, related_name='to_user')
	date_created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "%s-->%s" % (self.mentee, self.mentor)


class CommunicationMode(models.Model):
	platform = models.CharField(max_length=50)
	contact_detail = models.CharField(max_length=20)

	def __str__(self):
		return "%s: %s" % (self.platform, self.contact_detail)

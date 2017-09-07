from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.conf import settings
import uuid
from django.template.defaultfilters import slugify
from expert.models import Industry, Address
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class Mentee(models.Model):
	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
		YEAR_CHOICES.append((r,r))

	TIME_CHOICES = (
		('forth-nightly', 'Forth-nightly'),
		('monthly', 'Monthy')
	)
	MODE_CHOICES = (
		('whatsapp', 'Whatsapp'),
		('email', 'Email'),
		('call', 'Phone call'),
		('f2f', 'Face-to-Face'),
		('skype', 'Skype')
	)
	QUALIFICATION_CHOICES = (
		('SSCE', 'SSCE'),
		('OND', 'OND'),
		('HND', 'HND'),
		('BSc and MSc', 'BSc and MSc'),
		('PhD', 'PhD')
	)

	title = models.CharField(max_length=10, choices=settings.TITLE_CHOICES, blank=True)
	name = models.CharField(max_length=50, null=True, blank=True)
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	background_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES, null=True, blank=True)
	phone_number = models.CharField(max_length=12, blank=True)
	level_of_education = models.CharField(max_length=27, choices=QUALIFICATION_CHOICES, null=True, blank=True)
	name_of_business = models.CharField(max_length=50, null=True, blank=True)
	industry = models.ForeignKey(Industry, null=True, blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)
	slug = models.SlugField(unique=True)
	year_of_commencement = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year) 
	time_with_mentor = models.CharField("How much time would you need from your mentor?", max_length=20, choices=TIME_CHOICES, null=True, blank=True)
	mode_of_communication = models.CharField(max_length=50, choices=MODE_CHOICES, null=True, blank=True)
	mode_details = models.CharField("Please give details for the mode chosen above", max_length=50, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s %s" % (self.title, self.name)

	def get_absolute_url(self):
		return reverse('mentee:mentee-profile', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		orig = slugify(self.name)
		self.slug = "%s-%s"[:50] % (orig, uuid.uuid4())
		super(Mentee, self).save(*args, **kwargs)


class MentorshipRequest(models.Model):
	STATUS = (
		('O', 'Open'),
		('A', 'Accepted'),
		('D', 'Denied')
	)
	mentee= models.ForeignKey(User, related_name='request_sent', null=True)
	industry = models.ForeignKey(Industry)
	to_user = models.ForeignKey(User, related_name='request_received')
	status = models.CharField(max_length=1, choices=STATUS, default='O')
	date_created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "%s-->%s" % (self.mentee, self.to_user)

	class Meta:
		verbose_name = _(u'Mentorship Request')
		verbose_name_plural = _(u'Mentorship Requests')
		ordering = ('-date_created',)

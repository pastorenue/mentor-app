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
	name_of_business = models.CharField(max_length=150, null=True, blank=True)
	industry = models.ForeignKey(Industry, null=True, blank=True)
	address = models.ForeignKey(Address, null=True, blank=True)
	slug = models.SlugField(max_length=255, unique=True)
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
	
	def get_absolute_edit(self):
		return reverse('mentee:edit')

	@property 
	def percentage_complete(self):
		percent = get_profile_complete(self)
		return percent

	def save(self, *args, **kwargs):
		orig = slugify(self.name)
		self.slug = "%s-%s"[:50] % (orig, uuid.uuid4())
		self.name = "%s, %s" % (self.user.first_name, self.user.last_name)
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


def get_profile_complete(self):
	percent = { 
			'title': 5, 
			'name': 2, 
			'photo': 10,
			'background_image': 5,
			'industry': 32, 
			'phone_number': 2,
			'address': 15,
			'time_with_mentor':2,
			'mode_of_communication':2,
			'mode_details': 5,
			'name_of_business': 10,
			'year_of_commencement': 5,
			'level_of_education': 5
		}

	total = 0
	if self.title:
		total += percent.get('title', 0)
	if self.name:
		total += percent.get('name', 0)
	if self.photo:
		total += percent.get('photo', 0)
	if self.background_image:
		total += percent.get('background_image', 0)
	if self.industry:
		total += percent.get('industry', 0)
	if self.phone_number:
		total += percent.get('phone_number', 0)
	if self.address:
		total += percent.get('address', 0)
	if self.time_with_mentor:
		total += percent.get('time_with_mentor', 0)
	if self.mode_of_communication:
		total += percent.get('mode_of_communication', 0)
	if self.name_of_business:
		total += percent.get('name_of_business', 0)
	if self.year_of_commencement:
		total += percent.get('year_of_commencement', 0)
	if self.level_of_education:
		total += percent.get('level_of_education', 0)
	
	#and so on
	return int(total)
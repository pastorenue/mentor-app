from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import uuid
# Create your models here.

class MeetingExpert(models.Model):
	WORK_TYPE = (
		(1, 'Business diagnostics'),
		(2, 'Operations optimization'),
		(3, 'Training/HR needs'),
		(4, 'Business plan'),
		(5, 'Feasibility studies'),
		(6, 'Business templates'),
		(7, ' Marketing and brand communication'),
		(8, 'Social media marketing and PR'),
		(9, 'Pubic speaking training'),
		(10, 'Interview preparation training'),
		(11, 'Logo design'),
	)
	NEW_USER, RETURNING_USER = ('N', 'R')
	USER_TYPE_CHOICES = (
		(NEW_USER, 'New User'),
		(RETURNING_USER, 'Returning User')
	)
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50, blank=True)
	name_of_business = models.CharField(max_length=100)
	address_of_business = models.OneToOneField('expert.Address')
	sector_or_industry = models.ForeignKey('expert.Industry')
	work_type = models.CharField(max_length=2, choices=WORK_TYPE)
	user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
	about_project = models.CharField("What is your project about?", max_length=100)
	skills_required = models.CharField("What skills are required?", max_length=100)
	project_description = models.TextField("Describe your project")
	file = models.FileField("Upload files that could be useful", upload_to='uploads/%Y/%m/%d')
	proposed_budget = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
	delivery_date = models.DateTimeField("Expected delivery date")
	further_follow_up = models.CharField("Who do we contact for further follow up?", max_length=12)
	create_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _(u'Meeting With Expert')
		verbose_name_plural = _(u'Meetings With Expert')
		ordering = ('name',)

	def __str__(self):
		return "%s: %s" % (self.name, self.name_of_business)


class Address(models.Model):
	user = models.OneToOneField(User)
	street = models.CharField(max_length=50, blank=True)
	city = models.CharField("City/Town/Village", max_length=20, blank=True)
	state = models.ForeignKey("states.State", blank=True)
	country = models.ForeignKey("states.Country", default="156")

	def __str__(self):
		return "%s, %s" % (self.street, self.city)


class Industry(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Industry')
		verbose_name_plural = _(u'Industries')
		

class Expert(models.Model):
	AVAILABILITY_CHOICES = (
		('daily', 'Daily'),
		('forth-nightly', 'Forth-nightly'),
		('monthly', 'Monthly'),
	)

	PROJECT_TYPE_CHOICES = (
		('project-based', 'Project-based Jobs'),
		('long-term', 'Long-term Jobs'),
		('one-off', 'One-off Jobs')
	)
	title = models.CharField(max_length=10, choices=settings.TITLE_CHOICES)
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	background_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES)
	industry = models.ForeignKey(Industry)
	availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=13)
	type_to_handle = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
	short_biography = models.TextField(blank=True)
	cv_file = models.FileField("Attach PDF copy of CV ", upload_to='uploads/%Y/%m/%d')
	slug = models.SlugField(unique=True, blank=True)
	linkedin_url = models.URLField("Link to LinkedIn Bio/profile", blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s %s" % (self.title, self.name)

	def get_absolute_url(self):
		return reverse('expert:expert-profile', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		orig = slugify(self.name)
		self.slug = "%s-%s"[:50] % (orig, uuid.uuid4())
		self.email = self.user.username
		super(Expert, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _(u'Expert')
		verbose_name_plural = _(u'Experts')
		ordering = ('name',)
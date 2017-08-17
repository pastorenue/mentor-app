from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.

class MeetingExpert(models.Model):
	NEW_USER, RETURNING_USER = ('N', 'R')
	USER_TYPE_CHOICES = (
		(NEW_USER, 'New User'),
		(RETURNING_USER, 'Returning User')
	)
	user = models.ForeignKey(User)
	name = models.CharField(max_length=30)
	name_of_business = models.CharField(max_length=100)
	address_of_business = models.OneToOneField('expert.Address')
	sector_or_industry = models.ForeignKey('expert.Industry')
	work_type = models.ForeignKey('expert.WorkType')
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
	street = models.CharField(max_length=50)
	city = models.CharField("City/Town/Village", max_length=20)
	state = models.ForeignKey("states.State")
	Country = models.ForeignKey("states.Country")

	def __str__(self):
		return "%s, %s" % (self.street, self.city)


class Industry(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Industry')
		verbose_name_plural = _(u'Industries')
		

class WorkType(models.Model):
	business_diagnostics = models.BooleanField(default=False)
	operation_optimization = models.BooleanField(default=False)
	traning_needs = models.BooleanField("Training/HR needs", default=False)
	business_plan = models.BooleanField("Business Plan", default=False)
	feasibility_study = models.BooleanField()
	business_templates = models.BooleanField()
	marketing_communication = models.BooleanField("Marketing and Brand Communication")
	social_media_marketing = models.BooleanField("Social media marketing and PR")
	public_speaking_training = models.BooleanField("Pubic speaking training")
	interview_operations = models.BooleanField("Interview preparation training")
	logo_design = models.BooleanField("Logo Design")
	newsletter_subscription = models.BooleanField("Subscribe to newsletter")


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
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES)
	Industry = models.ForeignKey(Industry)
	availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
	email = models.EmailField()
	phone_number = models.CharField(max_length=13)
	type_to_handle = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
	short_biography = models.TextField(blank=True)
	cv_file = models.FileField("Attach PDF copy of CV ", upload_to='uploads/%Y/%m/%d')
	slug = models.SlugField(unique=True)
	linkedin_url = models.URLField("Link to LinkedIn Bio/profile", blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s %s" % (self.title, self.name)

	def get_absolute_url(self):
		pass
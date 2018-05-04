from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
import uuid

# Create your models here.
class MentorManager(models.Manager):
	def get_queryset(self):
		return super(MentorManager, self).get_queryset().filter(account_status='A')

	def trending_mentors(self):
		pass

class Mentor(models.Model):
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
	STATUS_CHOICES = (
		('A', 'Active'),
		('D', 'Deleted')
	)

	title = models.CharField(max_length=10, choices=settings.TITLE_CHOICES, blank=True)
	name = models.CharField(max_length=50, blank=True)
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	background_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES, blank=True)
	industry = models.ForeignKey('expert.Industry', null=True, blank=True)
	specify_industry = models.CharField('If Others, Specify', max_length=100, null=True, blank=True)
	availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, blank=True)
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=13, null=True, blank=True)
	short_biography = models.TextField(blank=True)
	years_of_experience = models.PositiveIntegerField(null=True, blank=True)
	cv_file = models.FileField("Attach PDF copy of CV ", upload_to='uploads/%Y/%m/%d', blank=True)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	linkedin_url = models.URLField("Link to LinkedIn Bio/profile", null=True, blank=True)
	account_status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
	can_migrate = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	objects = MentorManager()

	def __str__(self):
		return "%s %s" % (self.title, self.name)

	def get_absolute_url(self):
		return reverse('mentor:mentor-profile', kwargs={'slug': self.slug})

	def get_absolute_edit(self):
		return reverse('mentor:edit')

	@property
	def get_industry(self):
		if self.industry:
			if self.industry.name == "Others":
				return self.specify_industry
			else:
				return self.industry
		else:
			return self.industry

	@property 
	def percentage_complete(self):
		percent = get_profile_complete(self)
		return percent

	def save(self, *args, **kwargs):
		orig = slugify(self.name)
		self.slug = "%s-%s"[:50] % (orig, uuid.uuid4())
		self.email = self.user.username
		self.name = "%s, %s" % (self.user.first_name, self.user.last_name)
		super(Mentor, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _(u'Mentor')
		verbose_name_plural = _(u'Mentors')
		ordering = ('name',)



def get_profile_complete(self):
	percent = { 
			'title': 5, 
			'name': 2, 
			'photo': 10,
			'background_image': 5,
			'industry': 42, 
			'phone_number': 2,
			'cv_file':2,
			'years_of_experience':7,
			'age_range': 5,
			'short_biography': 5,
			'availability': 15,
			'linkedin_url': 5
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
	if self.cv_file:
		total += percent.get('cv_file', 0)
	if self.years_of_experience:
		total += percent.get('years_of_experience', 0)
	if self.age_range:
		total += percent.get('age_range', 0)
	if self.short_biography:
		total += percent.get('short_biography', 0)
	if self.availability:
		total += percent.get('availability', 0)
	if self.linkedin_url:
		total += percent.get('linkedin_url', 0)
	
	#and so on
	return int(total)
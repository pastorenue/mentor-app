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

	title = models.CharField(max_length=10, choices=settings.TITLE_CHOICES)
	name = models.CharField(max_length=50, blank=True)
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
	age_range = models.CharField(max_length=5, choices=settings.AGE_RANGE_CHOICES)
	industry = models.ForeignKey('expert.Industry')
	availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=13)
	type_to_handle = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
	short_biography = models.TextField(blank=True)
	years_of_experience = models.PositiveIntegerField(null=True)
	cv_file = models.FileField("Attach PDF copy of CV ", upload_to='uploads/%Y/%m/%d')
	slug = models.SlugField(unique=True, blank=True)
	linkedin_url = models.URLField("Link to LinkedIn Bio/profile", null=True, blank=True)
	account_status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	objects = MentorManager()

	def __str__(self):
		return "%s %s" % (self.title, self.name)

	def get_absolute_url(self):
		pass

	def get_public_url(self):
		return reverse('mentor:mentor-public-profile', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		orig = slugify(self.name)
		self.slug = "%s-%s"[:50] % (orig, uuid.uuid4())
		self.email = self.user.username
		super(Mentor, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _(u'Mentor')
		verbose_name_plural = _(u'Mentors')
		ordering = ('name',)
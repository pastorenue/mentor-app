from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Author(models.Model):
	user = models.ForeignKey(User, null=True)
	name = models.CharField(_('Displayed name'), max_length=300)
	photo = models.ImageField(upload_to="uploads")

	def __str__(self):
		return "{} ({})".format(self.user, self.name)

	class Meta:
		verbose_name = _(u'Author')
		verbose_name_plural = _(u'Authors')
		ordering = ('name',)

class EntryManager(models.Manager):
	def get_all(self):
		return self.all().order_by('-date_created').select_related()

	def get_active(self):
		return self.filter(publish=True).order_by('-date_modified')

	def get_recent(self):
		recent = datetime.today() - timedelta(days=7)
		return self.filter(date_created__gte=recent).order_by('-date_created')[:6]

	def get_most_viewed(self):
		return self.all().order_by('-views')[:6]


class Entry(models.Model):
	author = models.ForeignKey(Author, null=True)
	title = models.CharField(max_length=200, null=True)
	sub_title = models.CharField(max_length=100, null=True, blank=True)
	content = HTMLField()
	illustration = models.ImageField(upload_to='uploads/blogs/', blank=True)
	tags = models.CharField(max_length=300, blank=True)
	slug = models.SlugField()
	views = models.PositiveIntegerField(default=0)
	publish = models.BooleanField(_('Publish now'), default=True, help_text="Show this field in the news feed")
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	objects = EntryManager()

	def __str__(self):
		return "%s --> %s" % (self.author, self.title)

	@models.permalink
	def get_abosolute_url(self):
		return HttpResponseRedirect(reverse('newsroom:news-detail', args=(self.slug,)))

	class Meta:
		verbose_name = _(u'Entry')
		verbose_name_plural = _(u'Entries')
		ordering = ('-date_created',)

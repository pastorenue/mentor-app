from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Author(models.Model):
	user = models.ForeignKey(User, null=True)
	name = models.CharField(_('Displayed name'), max_length=300)
	photo = models.ImageField(upload_to="uploads/%F/%m/%d")

	def __str__(self):
		return "{} ({})".format(self.user, self.name)

	class Meta:
		verbose_name = _(u'Author')
		verbose_name_plural = _(u'Authors')
		ordering = ('name',)

class EntryManager(models.Manager):
	def get_all(self):
		return self.all().order_by('-date_modified').select_related()

	def get_active(self):
		return self.filter(publish=True).order_by('-date_modified')

class Entry(models.Model):
	author = models.ForeignKey(Author, null=True)
	title = models.CharField(max_length=100, null=True)
	content = HTMLField()
	illustration = models.ImageField(upload_to='uploads/blogs/%F/%m/%d', blank=True)
	tags = models.CharField(max_length=300, blank=True)
	slug = models.SlugField()
	publish = models.BooleanField(_('Publish now'), default=True, help_text="Show this field in the news feed")
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	objects = EntryManager()

	def __str__(self):
		return "%s --> %s" % (self.author, self.title)

	class Meta:
		verbose_name = _(u'Entry')
		verbose_name_plural = _(u'Entries')
		ordering = ('title',)

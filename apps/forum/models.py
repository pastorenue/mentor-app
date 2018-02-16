from django.db import models
from django.contrib.auth.models import User
import uuid
from django.template.defaultfilters import slugify


class Channels(models.Model):
	name = models.CharField(max_length=100, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Channel'
		verbose_name_plural = 'Channels'
		ordering = ('date_created',)


class Post(models.Model):
	user = models.ForeignKey(User, null=True)
	content = models.TextField()
	channels = models.ForeignKey(Channels, null=True)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s --> %s" % (self.user.first_name, self.title)

	def save(self, *args, **kwargs):
		orig = slugify(self.content)
		self.slug = "%s-%s" % (orig, uuid.uuid4())
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	user = models.ForeignKey(User, null=True)
	post = models.ForeignKey(Post, null=True)
	body = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s --> %s" % (self.user.first_name, self.body[:20])

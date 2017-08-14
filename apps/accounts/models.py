from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Quote(models.Model):
	author = models.CharField(max_length=30)
	content = models.TextField()
	image = models.ImageField(upload_to='uploads/%Y/%m/%') 
	source = models.CharField("Quote Reference", max_length=40, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _(u'Quote')
		verbose_name_plural = _(u'Quotes')

	def __str__(self):
		return "%s: %s" % (self.author, self.content[:20])

	
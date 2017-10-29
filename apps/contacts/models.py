from django.db import models


class Contact(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(null=True)
	subject = models.CharField(max_length=100, null=True)
	message = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s --> %s" % (self.email, self.subject)

	class Meta:
		ordering = ('-date_created',)

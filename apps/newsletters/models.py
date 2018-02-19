from django.db import models


LETTER_CHOICES = (
	('forbes', 'Forbes'),
	('business', 'Business')
)
class Subscription(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=50, null=True, blank=True)
	name_of_company = models.CharField(max_length=100, null=True)
	letter_type = models.CharField(max_length=100, choices=LETTER_CHOICES, null=True)

	def __str__(self):
		return self.email

class Newsletter(models.Model):
	letter_type = models.CharField(max_length=100, choices=LETTER_CHOICES, null=True)
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s --> %s".format(self.letter_type, self.content[:20])

	class Meta:
		ordering = ('-date_created',)
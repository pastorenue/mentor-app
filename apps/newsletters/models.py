from django.db import models

class Newsletter(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=50, null=True)
	name_of_company = models.CharField(max_length=100, null=True)
	sector = model.CharField(max_length=100, null=True)
	letter_type = models.CharField(max_length=100, choices=LETTER_CHOICES, null=True)

	def __str__(self):
		return self.email

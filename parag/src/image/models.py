from django.db import models
from django.urls import reverse


class Image(models.Model):
	name= models.CharField(max_length=250)
	file= models.FileField()

	def get_absolute_url(self):
		return reverse('image:index')

	def __str__(self):
		return self.name





from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Genre(models.Model):
	name = models.CharField(max_length=300)
	father_id = models.IntegerField(default=-1)

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=300)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='covers/', null=True, blank=True)
	summary = models.TextField()
	stars = models.IntegerField(default=0)
	uploader = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
	upload_date = models.DateTimeField(default=timezone.now)
	file = models.FileField(upload_to='pdfs/')


	def __str__(self):
		return self.title
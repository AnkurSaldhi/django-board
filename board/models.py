from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name


class Task(models.Model):
	board = models.ForeignKey(Board)
	description = models.CharField(max_length=100)
	completed_percentage = models.IntegerField(default=0)

	def __unicode__(self):
		return self.description
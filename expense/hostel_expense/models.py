from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

class Expense(models.Model):
	user = models.ForeignKey(User, db_index=True, null=True)
	date = models.DateTimeField(max_length=10)
	description = models.TextField()
	amount = models.CharField(max_length=20)

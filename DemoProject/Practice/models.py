from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PracModel(models.Model):
	"""docstring for PracModel"""
	name=models.CharField(max_length=100)
	mobile=models.TextField()
	

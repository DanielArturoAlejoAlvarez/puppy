# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=75)
	age=models.IntegerField()
	phone=models.CharField(max_length=20)
	email=models.EmailField()
	address=models.TextField()


	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)


class YourRequest(models.Model):
	person=models.ForeignKey(Person, null=True, blank=True)
	number_pets=models.IntegerField()
	reasons=models.TextField()
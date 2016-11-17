from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Description(models.Model):
	name = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.OneToOneField(Description,on_delete=models.CASCADE,
        primary_key=True,)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	comment = models.TextField(max_length=1000)
	course_id = models.ForeignKey(Course)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


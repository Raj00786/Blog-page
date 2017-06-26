from django.db import models
from taggit.managers import TaggableManager


class Blogs(models.Model):
	name = models.CharField(max_length=20)
	topic = models.CharField(max_length=100)
	content = models.TextField()
	uploadtime = models.DateTimeField(default="nothing")
	tags = TaggableManager()
	def __str__(self):
		return self.topic+'-'+self.name
	

# class Users(models.Model):
# 	username = models.CharField(max_length=20)
# 	password = models.CharField(max_length=20)

# 	def __str__(self):
# 		return self.username

class Register(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.firstname+' '+self.lastname

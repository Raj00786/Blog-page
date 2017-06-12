from django.db import models

class Blogs(models.Model):
	name = models.CharField(max_length=20)
	topic = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	profile = models.CharField(max_length=100,default='https://cdn4.iconfinder.com/data/icons/rcons-user/32/boss_man-512.png',blank=True, null=True)

	def __str__(self):
		return self.topic+'-'+self.name

class Users(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.username
# models of admin1
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from news.models import News_content
# Create your models here.

class profile(models.Model):
	id = models.AutoField	
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_no = models.IntegerField(default="0")
	image = models.ImageField()
	Address = models.CharField(max_length=100,default="")
	proffession	= models.CharField(max_length=50,default="")
	facebook = models.CharField(max_length=250,default="")
	instagram = models.CharField(max_length=250,default="")
	twitter	= models.CharField(max_length=250,default="")
	Field_location = models.TextField(max_length=25,default="")	
	is_login = models.CharField(max_length=50,default="")
	is_blocked = models.CharField(max_length=50,default="Unblock")
	def __str__(self):
		return self.user_id.first_name

class category(models.Model):
	id = models.AutoField
	category_name = models.TextField(max_length="50", default="")
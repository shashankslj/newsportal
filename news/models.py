# models of news
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class News_content(models.Model):
	id = models.AutoField
	News_title = models.CharField(max_length=50,default="")
	content = models.TextField(max_length=1000,default="")
	image = models.ImageField()
	video = models.CharField(max_length=50,default="")
	news_category = models.TextField(max_length=50,default="")
	status = models.TextField(max_length=100, default="Pending")
	user_id = models.ForeignKey(User, default="", on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.News_title
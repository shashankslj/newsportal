from django.db import models
from django.contrib.auth.models import User
from news.models import News_content
from django.utils import timezone
# class  comments_data(models.Model):
# 	id = models.AutoField
# 	user = models.ManyToManyField(User)
# 	news = models.ManyToManyField(News_content)
# 	comments_data = models.TextField(max_length=1000,default=" ")
# 	like = models.IntegerField(default="0")
# 	created_at = models.DateTimeField(default=timezone.now)
# 	updated_at = models.DateTimeField(default=timezone.now)
# 	def __str__(self):
# 		return self.id

class comments_data(models.Model):	
	id = models.AutoField
	news_id = models.ForeignKey(News_content, on_delete=models.CASCADE)	
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	data = models.TextField(max_length = 1000,default="")
	like = models.IntegerField(default="0")
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.data

class message_user(models.Model):
	id = models.AutoField
	sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciver_id')
	reciver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_id')
	data = models.TextField(max_length = 1000,default="")	
	updated_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.sender_id

class feedback(models.Model):	
	id = models.AutoField
	feed_back = models.TextField(max_length = 1000,default="")
	name = models.CharField(max_length = 30,default="")
	email = models.CharField(max_length = 50,default="")
	created_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
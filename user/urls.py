# Url file of User
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
	path('', views.index),
	path('about', views.about),
	path('news_video/<int:id>', views.news_video),
	path('latest_news/<int:id>', views.latest_news),
	path('login', views.login),
	path('comment/<int:id>', views.comments),
	path('register', views.register),	
	path('edit_comment_data/<int:id>', views.edit_comment_data),
	path('delete_comment/<int:id>', views.delete_comment),
	path('user_profile', views.user_profile),
	path('edit_profile', views.edit_profile),
	path('category_grid/<str:category>', views.category_grid),
	path('message/<int:id>', views.message),
	path('contact', views.contact),
	path('contact_detail', views.contact_detail),
	path('logout', views.logout)

]
 
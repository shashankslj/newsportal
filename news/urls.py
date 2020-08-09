 # Url file of news
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('',views.master1),
	path('user_profile', views.user_profile),
	path('edit_profile', views.edit_profile),
	path('addnews', views.Addnews),
	path('status', views.Status),
	path('login', views.login),
	path('logout', views.logout),
    path('edit_data/<int:id>', views.edit_data),    
    path('edit_data_stored/<int:id>', views.edit_data_stored),
    path('data_delete/<int:id>', views.data_delete),
    path('show_data/<int:id>', views.show_data),
    path('show_comment/<int:id>', views.show_comment), 
    path('total_News', views.total_News),
    path('Approved_News', views.Approved_News),
    path('pending', views.pending),
    path('data_comments', views.data_comments),
    path('comment_data/<int:id>', views.comment_data),
    path('delete_all', views.delete_all),
]

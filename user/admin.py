from django.contrib import admin
from .models import comments_data
from .models import message_user
from .models import feedback

admin.site.register(comments_data)
admin.site.register(message_user)
admin.site.register(feedback)
# Register your models here.
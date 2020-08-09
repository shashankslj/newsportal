from django.contrib import admin
from .models import category
from .models import profile

admin.site.register(profile)
admin.site.register(category)
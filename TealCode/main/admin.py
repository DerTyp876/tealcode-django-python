from django.contrib import admin
from .models import Category, Rating, Topic

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Rating)
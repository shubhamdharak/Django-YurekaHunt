from django.contrib import admin
from .models import Blog, BlogComment, contact

admin.site.register((Blog, BlogComment, contact))

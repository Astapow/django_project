from django.contrib import admin
from .models import BlogPost, Topic, Comment

admin.site.register(BlogPost)
admin.site.register(Topic)
admin.site.register(Comment)

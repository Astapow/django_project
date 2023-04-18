from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True)
    author = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    title = models.TextField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.TextField(max_length=100)
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

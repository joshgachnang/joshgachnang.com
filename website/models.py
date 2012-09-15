from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    display_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    content = models.TextField()
    site = models.ForeignKey(Site)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(UserProfile)
    published = models.DateTimeField()
    comments_disabled = models.BooleanField(default=False)
    in_nav_bar = models.BooleanField(default=False)
    in_blog_posts = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

# Add everything to the admin interface
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Post)
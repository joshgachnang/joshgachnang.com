from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib import admin
import datetime


def current_time():
    return datetime.datetime.now()

# Important! Categories, tags, and posts all share one name space.
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
    url = models.CharField(max_length=64, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_preview = models.TextField(blank=True, null=True)
    site = models.ForeignKey(Site)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(UserProfile)
    published = models.DateTimeField(default=current_time)
    comments_disabled = models.BooleanField(default=False)
    in_blog_posts = models.BooleanField(default=True)
    template_name = models.CharField(max_length=256, default="post.html")

    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = self.title.strip().replace(' ', '_').replace(':', '')
        super(Post, self).save(*args, **kwargs)


class NavBar(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class NavBarItem(models.Model):
    url = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)
    navbar = models.ForeignKey(NavBar)
    priority = models.IntegerField()
    target = models.CharField(max_length=64, blank=True, null=True, default=None)
    def __unicode__(self):
        return self.display_name


# Add everything to the admin interface
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(NavBar)
admin.site.register(NavBarItem)

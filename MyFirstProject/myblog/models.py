from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	timestamp = models.DateTimeField()
	def __str__(self):
		return self.title

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)     #register the BlogPost model to admin

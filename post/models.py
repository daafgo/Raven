from django.db import models
from users.models import User
from django.contrib import admin

class Reply(models.Model):
	body = models.TextField(max_length=155)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User)


class Post(models.Model):
	body = models.TextField(max_length=155)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User)
	reply = models.ManyToManyField(Reply)
    


##ADMIN


class PostAdmin(admin.ModelAdmin):
	list_display = ["creator", "created"]
	list_filter = ["creator"]

class ReplyAdmin(admin.ModelAdmin):
	list_display = ["creator", "created"]
	list_filter = ["creator"]

admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)

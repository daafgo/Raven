from django.db import models

from users.models import CustomUser
from django.contrib import admin
from django.db.models.signals import pre_init
from django.dispatch import receiver



class Reply(models.Model):
    body = models.TextField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser)


class Post(models.Model):
    body = models.TextField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser)
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



def Post_creado(sender,args, **kwargs):
#Cuando el usuario con ID=2 crea un post este se almacena como post del Admin
    dic=kwargs.__getitem__('kwargs')
    if dic.get('creator' ) == CustomUser.objects.get(id=2):
        dic.__setitem__('creator', CustomUser.objects.get(id=1))


pre_init.connect(Post_creado, sender=Post)
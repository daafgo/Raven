from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.contrib import admin


class CustomUser(AbstractUser):
    pseudo = models.CharField(max_length=100)  #Alias de usuario
    #followers = models.ManyToManyField(CustomUser, related_name='seguidor')
    birth_date = models.DateField(null=True)
    def content_file_name(self, filename):
        return '/'.join([self.email, 'img', filename])

    photo = models.ImageField(upload_to=content_file_name, default='/static/img/default/defaultProfile.png', blank=True)


class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ["pseudo"]


admin.site.register(CustomUser, CustomUserAdmin)

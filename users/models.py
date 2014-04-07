"""
Primer fichero models que se implementa en la aplicacion
Determina las caracteristicas que van a tener nuestros usuarios
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
class ExtendUser(models.Model):
    """ La clase se usa para almacenar las
	caracteristicas de los usuarios extendidos """
    user = models.ForeignKey(User, unique=True)
    pseudo = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, related_name='seguidor')
    def content_file_name(self, filename):
        """ HOla cacca """
        return '/'.join([self.email, 'img', filename])
    photo = models.ImageField(upload_to=content_file_name, default='/static/img/default/defaultProfile.png', blank=True)



class ExtendUserAdmin(admin.ModelAdmin):
    """ HOla caca """
    list_display = ["user"]
    list_filter = ["pseudo"]



admin.site.register(ExtendUser, ExtendUserAdmin)

from django import forms
from django.utils.translation import ugettext_lazy as _
from post.models import Post
class PostForm(forms.Form):
    body = forms.CharField(initial="Escribe tu post aqui")


import datetime

from lettuce import *
from django.test.client import Client
from lettuce import step, world
from django.contrib.auth.models import User
from post.models import *


@before.all
def set_browser():
    world.browser = Client()


@step(r'El usuario "(.*)", email "(.*)", password "(.*)" postea "(.*)"')
def a_user_have_post(step, nombre, email, password, post):
    user = User.objects.create_user(nombre, email, password)
    p = Post.objects.create(
        creator=user,
        created=datetime.datetime.now(),
        body=post,
    )
    user.delete()
    p.delete()


@step(r'El usuario "(.*)", email "(.*)", password "(.*)" comenta "(.*)"')
def a_user_have_post(step, nombre, email, password, post):
    user = User.objects.create_user(nombre, email, password)
    p = Reply.objects.create(
        creator=user,
        created=datetime.datetime.now(),
        body=post,
    )
    user.delete()
    p.delete()
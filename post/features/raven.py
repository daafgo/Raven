from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from lettuce import step, world
from lettuce.django import django_url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from post.models import *
from django.contrib.auth import authenticate, login
import datetime

@before.all
def set_browser():
    world.browser = Client()


@step(r'El usuario "(.*)", email "(.*)", password "(.*)" postea "(.*)"')
def a_user_have_post(step,nombre,email,password,post):

	user = User.objects.create_user(nombre,email,password)
	p = Post.objects.create(
    	creator = user,
    	created = datetime.datetime.now(),
    	body = post,
    	)
	user.delete()
	p.delete()

@step(r'El usuario "(.*)", email "(.*)", password "(.*)" comenta "(.*)"')
def a_user_have_post(step,nombre,email,password,post):

	user = User.objects.create_user(nombre,email,password)
	p = Reply.objects.create(
    	creator = user,
    	created = datetime.datetime.now(),
    	body = post,
    	)
	user.delete()
	p.delete()
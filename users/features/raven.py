import re
from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from lettuce import step, world
from lettuce.django import django_url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from users.models import ExtendUser

@before.all
def set_browser():
    world.browser = Client()


@step(r'Puedo acceder al registo "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text

@step(r'I see the title "(.*)"')
def see_title(step, text):
    header = world.dom.cssselect('title')[0]
    assert header.text == text


@step(r'Y puedo ver el input "(.*)"')
def see_input(step, text):
    header = world.dom.cssselect('input')[1]
    assert header.name == text

@step(r'puedo ver el input "(.*)" en la pocision "(.*)"')
def i_fill_in(step, text, value):
    header = world.dom.cssselect('input')[int(value)]
    assert header.name == text

@step(r'Me registro con el usuario "(.*)", email "(.*)", password "(.*)"')
def me_registro_en(step,nombre,email,password):
    user = User.objects.create_user(nombre,email,password)
    name = user.username
    assert name == nombre

@step(r'Me logueo con el usuario "(.*)", password "(.*)"')
def me_logueo_en(step,nombre,password):
    user = authenticate(username=nombre, password=password)
    autenticado = "false"
    if user is not None:
        autenticado = "true"
    else:
        autenticado = "false"
    user.delete()
    assert autenticado == "true"

@step(r'Accedo a "(.*)" coen el usuario "(.*)", email "(.*)", password "(.*)"')
def me_registro_en(step,url,nombre,email,password):
    User.objects.create_user(nombre,email,password)
    user = authenticate(username=nombre, password=password)
    response = world.browser.get(url)
    user.delete()
    world.dom = html.fromstring(response.content)


@step(r'El usuario "(.*)", email "(.*)" password "(.*)" sigue al usuario "(.*)", email "(.*)" password "(.*)"')
def seguir_a_un_usuario(step,nombre1,email1,password1,nombre2,email2,password2):
    user1 = User.objects.create_user(nombre1,email1,password1)
    user2 = User.objects.create_user(nombre2,email2,password2)

    pseudo="@"+nombre1
    extend=ExtendUser(user=user1,pseudo=pseudo)
    extend.save()
    extend.followers.add(User.objects.get(id = user2.id))
    if user2 in extend.followers.all():
        seguido = "true"

    extend.delete()
    user1.delete()
    user2.delete()

    assert seguido == "true"
    
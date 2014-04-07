# Create your views here.
from post.models import *
from django.shortcuts import redirect
import datetime



def del_post(request, post_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		Post.objects.filter(id = post_id).delete()
		return redirect('/home/')
		
def newreply(request, post_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:

		reply=Reply.objects.create(
		creator = request.user,
		created = datetime.datetime.now(),
		body = request.POST.get('mensaje'),)
		post=Post.objects.get(id = post_id)
		post.reply.add(reply)	
	return redirect('/home/')
def delreply(request, post_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:

		reply=Reply.objects.get(id = post_id)
		
		reply.delete()	
	return redirect('/home/')

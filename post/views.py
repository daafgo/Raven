from post.models import Post, Reply
from post.forms import PostForm
import datetime
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        p = Post.objects.create(
            creator=request.user,
            created=datetime.datetime.now(),
            body=request.POST.get('body'),

        )
        p.save()
        return redirect('/')
    form=PostForm()
    return render(request,'post/post_form.html',{'form':form})

def del_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect('/home/')


def newreply(request, post_id):
    reply = Reply.objects.create(
        creator=request.user,
        created=datetime.datetime.now(),
        body=request.POST.get('mensaje'), )
    post = Post.objects.get(id=post_id)
    post.reply.add(reply)
    return redirect('/home/')


def delreply(request, post_id):
    reply = Reply.objects.get(id=post_id)
    reply.delete()
    return redirect('/home/')

class PostList(ListView):
    model = Post
class PostDetail(DetailView):
    model = Post

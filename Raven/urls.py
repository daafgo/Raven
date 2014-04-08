from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from post.views import new_post, del_post,newreply,delreply, PostList, PostDetail
from users.views import UserReg

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'Raven.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^post/(?P<pk>\d+)/edit$', login_required(PostUpdate.as_view()), name='post_update'),
    url(r'^post/create$', login_required(new_post), name='post_create'),
    url(r'^post/(?P<pk>\d+)/delete$', login_required(del_post), name='post_delete'),
    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view(), name="post_detail"),
    url(r'^$', PostList.as_view(), name="post_list"),
    url(r'^registration/', UserReg, name="user_form"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
)

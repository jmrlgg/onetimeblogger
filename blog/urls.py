"""blog.app.url configuration
The Views.
ARe.
Amazing."""

import os.path
from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib import admin


# from django.views.static import serve
# MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'docs')
# STATIC_DOC_ROOT = os.path.join(settings.BASE_DIR, 'imgs')


urlpatterns = [
	url(r'^login/', admin.site.urls),
	url(r'^$', views.blog_post, name='home'),
	url(r'^search/$', views.search, name="search"),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  # Post in-view ( view just one post post/<1 2 3 4>/ Than gives you the choice to edit if logged_in )
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),  # Post edit ( view and edit just one post [ post/<1 2 3 4>/ ] )
]


   #  url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	# url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	# url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
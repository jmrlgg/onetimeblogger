# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.


# def home(request):
#     return render(request, 'index.html')


# def blog_post(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     #posts = map(str, Post.objects.filter(published_date__lte=timezone.now().order_by('published_date'))


#     return render(request, 'blog/post_list.html', {'posts': posts})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import datetime
from blog.forms import ContactForm, PostForm
from django.core.mail import send_mail, get_connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from taggit.models import Tag
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def home(request):
    return render(request, 'blog/index.html')

def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'blog/search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            posts = Post.objects.filter(title__icontains=q)
            return render(request, 'blog/search_results.html', {'posts': posts, 'query': q})
    return render(request, 'blog/search_form.html', {'error': error})


def contact(request):
    """Contact View for users to be able to communicate with us."""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})

    return render(request, 'contact_form.html', {'form': form})


def blog_post(request):

    # posts = map(str, Post.objects.filter(published_date__lte=timezone.now().order_by('published_date'))

    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_list, 7) # Show 25 contacts per page
    page_request_var = 'abc'
    page = request.GET.get('page_request_var')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var

    }
    return render(request, 'blog/post_list.html', context)



def post_detail(request, pk):
    """Post from blog being displayed as a whole on a clean slate."""
    instance = get_object_or_404(Post, pk=pk)
    context = {
        "title": instance.title,
        "instance": instance
    }
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def post_edit(request, pk):
    """Gives admin or Staff ability to edit a post from the post detail page."""

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.up_date = datetime.datetime.now()
            post.save()
            return HttpResponseRedirect('post_detail.html', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         posts = Post.objects.filter(title__icontains=q)
#         return render(request, 'blog/search_results.html',
#                       {'posts': posts, 'query': q})
#     else:
#         return HttpResponse('Please submit a search term.')

# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return HttpResponseRedirect('post_detail', pk=comment.post.pk)

# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})



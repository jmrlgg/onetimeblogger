# -*- coding: utf-8 -*-
"""Admin."""

from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    """Admin Configurations for Staff to Create new Post."""

    list_display = ['title', 'heading', 'created_date', 'published_date']
    list_editable = ['heading']
    search_fields = ['title', 'created_date']
    ordering = ['-created_date', '-published_date']
    save_as = True

    class Meta:
        models = Post


admin.site.register(Post, PostModelAdmin)

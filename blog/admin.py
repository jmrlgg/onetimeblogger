# -*- coding: utf-8 -*-
"""Admin."""

from __future__ import unicode_literals

from django.contrib import admin
from .models import *



admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ('title', 'author', 'created_date')
	search_fields = ('title', 'author', 'created_date', 'tags')
	ordering = ('-created_date', '-published_date')
	save_as = True

	def get_queryset(self, request):
		return super(PostAdmin, self).get_queryset(request).prefetch_related('tags')

	def tag_list(self, obj):
		return u", ".join(o.name for o in obj.tags.all())




# -*- coding: utf-8 -*-
"""Admin."""

from __future__ import unicode_literals

from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Comment)

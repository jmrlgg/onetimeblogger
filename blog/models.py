# -*- coding: utf-8 -*-
"""Model defintions for Blog App."""

from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

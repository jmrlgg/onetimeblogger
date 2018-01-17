# -*- coding: utf-8 -*-
"""Model defintions for Blog App."""

from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class PostManager(models.Manager):
    def tag_count(self, keyword):
        return self.filter(tag__icontains=keyword).count()

class Post(models.Model):
    """Post Model."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def publish(self):
        """We are setting date and saving to db."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Post Model Return.

        Where the magic happens our title is returned
        we will be returning the date, and published date also.
        """
        return self.title

	class Meta:
		ordering = ['-published_date', '-created_date']

def create_slug(instance, new_slug=None):
    """ Creating a URL Ready NameSpace -.
    ex. TITLE: New Upcomer Wise = new-upcomer-wise."""

    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)


class TaggableManager():
    """Tagging Extenstion."""
    verbose_name = "Tags"
    help_text = "A comma-separated list of tags."
    through = None
    blank = False

        
# class Comment(models.Model):
#     post = models.ForeignKey('blog.Post', related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)

    # def __str__(self):
    #     return self.text

# WIll use this to create a Display post containing a certain tag
# class TagSortManager(models.Manager):
#     def get_queryset(self):
#         return super(TagSortManager, self).get_queryset().filter(tags=keyword)

# class FemaleManager(models.Manager):
#     def get_queryset(self):
#         return super(FemaleManager, self).get_queryset().filter(sex='F')

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     sex = models.CharField(max_length=1, 
#                            choices=(
#                                     ('M', 'Male'),  
#                                     ('F', 'Female')
#                            )
#                            )
#     people = models.Manager()
#     men = MaleManager()
#     women = FemaleManager()
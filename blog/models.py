from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class PostModel(models.Model):
    """
    Blog model.
    """

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post', on_delete=None)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    tags = TaggableManager()
    meta_title = models.CharField(max_length=70)
    meta_body = models.CharField(max_length=156)
    code_injection_header = models.CharField(max_length=10000)
    code_injection_footer = models.CharField(max_length=10000)
    twitter_card_title = models.CharField(max_length=1000)
    twitter_card_body = models.CharField(max_length=10000)
    twitter_card_image = models.ImageField(null=True, blank=True)
    facebook_card_title = models.CharField(max_length=1000)
    facebook_card_body = models.CharField(max_length=10000)
    facebook_card_image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

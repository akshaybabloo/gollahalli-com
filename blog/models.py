from django.contrib.auth.models import User
from django.db import models


class BlogModel(models.Model):
    """
    Blog model.
    """

    blog_id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    tags = models.CharField(max_length=10000)
    author = models.ForeignKey(User, related_name='blog_model', on_delete=None)
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
    created = models.DateTimeField(auto_now=True)


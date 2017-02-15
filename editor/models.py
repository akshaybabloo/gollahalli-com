from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    content = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")

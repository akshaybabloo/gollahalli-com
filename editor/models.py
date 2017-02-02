from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    content = JSONField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

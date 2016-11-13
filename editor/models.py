from django.db import models


class Content(models.Model):
    content_name = models.CharField(max_length=200, unique=False, default='Name of the field')
    content = models.TextField(default="Write about you.")

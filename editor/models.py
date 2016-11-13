from django.db import models


class ContentModel(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, default='1', unique=True)
    content = models.TextField(default="Write about you.")

import datetime
from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    content = JSONField()
    updated = models.DateTimeField(auto_now_add=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.updated = datetime.datetime.now()
        return super(ContentModel, self).save()

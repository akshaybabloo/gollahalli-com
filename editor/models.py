from django.db import models


class ContentModel(models.Model):
    ref_id = models.CharField(primary_key=True, max_length=120, unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.content

    class Meta:
        unique_together = ("content", "ref_id")

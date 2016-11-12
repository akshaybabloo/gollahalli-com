from django.db import models


class Content(models.Model):
    content_name = models.CharField(max_length=200, unique=False, default='Name of the field')
    content = models.TextField(default="Write about you.")


class Editor(models.Model):
    company_name = models.CharField(max_length=500, unique=False, default='Company name', blank=True)
    person_name = models.CharField(max_length=500, unique=False, default='Person name')
    maintenance = models.BooleanField(default=False)

from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")
    cv = models.CharField(default='CV URL', max_length=400)
    bio = models.CharField(default='Your Bio', max_length=1000)
    url = models.URLField(default='Website URL', max_length=400)
    name = models.CharField(default='Your Name', max_length=400)
    email_id = models.EmailField(default='Your email ID', max_length=400)
    github = models.URLField(default='GitHub URL', max_length=400)
    twitter = models.URLField(default='Twitter URL', max_length=400)
    linkedin = models.URLField(default='LinkedIn URL', max_length=400)
    education_json = JSONField(default={})
    experience_json = JSONField(default={})
    publication_json = JSONField(default={})
    research_area_json = JSONField(default={})
    skills_t1_json = JSONField(default={})
    skills_t2_json = JSONField(default={})
    projects_json = JSONField(default={})
    tutorials_json = JSONField(default={})

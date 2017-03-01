from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")

    def __str__(self):
        return str(self.ref_id)


class AboutMeModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    cv = models.CharField(default='CV URL', max_length=400)
    bio = models.CharField(default='Your Bio', max_length=1000)
    url = models.URLField(default='Website URL', max_length=400)
    name = models.CharField(default='Your Name', max_length=400)
    contact = models.EmailField(default='Your email ID', max_length=400)
    github = models.URLField(default='GitHub URL', max_length=400)
    twitter = models.URLField(default='Twitter URL', max_length=400)
    linkedin = models.URLField(default='LinkedIn URL', max_length=400)
    education_json = JSONField()
    experience_json = JSONField()
    publication_json = JSONField()
    research_area_json = JSONField()
    skills_t1_json = JSONField()
    skills_t2_json = JSONField()


class PortfolioModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    projects_json = JSONField()
    tutorials_json = JSONField()

from django.db import models
from django.contrib.postgres.fields import JSONField


class ContentModel(models.Model):
    ref_id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")
    cv = models.URLField(default='https://www.example.com', max_length=400)
    bio = models.CharField(default='Your Bio', max_length=10000)
    url = models.URLField(default='https://www.example.com', max_length=400)
    first_name = models.CharField(default='First Name', max_length=400)
    last_name = models.CharField(default='Last Name', max_length=400)
    email_id = models.EmailField(default='example@example.com', max_length=400)
    github = models.URLField(default='https://www.example.com', max_length=400)
    twitter = models.URLField(default='https://www.example.com', max_length=400)
    linkedin = models.URLField(default='https://www.example.com', max_length=400)
    education_json = JSONField(default={'example': 1})
    experience_json = JSONField(default={'example': 1})
    publication_json = JSONField(default={'example': 1})
    research_area_json = JSONField(default={'example': 1})
    skills_t1_json = JSONField(default={'example': 1})
    skills_t2_json = JSONField(default={'example': 1})
    projects_json = JSONField(default={'example': 1})
    tutorials_json = JSONField(default={'example': 1})

    def __str__(self):
        return str(self.ref_id)



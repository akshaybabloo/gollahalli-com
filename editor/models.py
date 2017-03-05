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


class EducationModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    to_date = models.DateField()
    from_date = models.DateField()
    where = models.CharField(default='where', max_length=500)
    current = models.BooleanField(default=False)


class ProjectsModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    category = models.CharField(default='category', max_length=500)
    file_name = models.CharField(default='file name', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000)
    short_description = models.CharField(default='short description', max_length=500)


class TutorialsModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    file_name = models.CharField(default='file name', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000)


class ExperienceModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    to_date = models.DateField()
    from_date = models.DateField()
    title = models.CharField(default='title', max_length=500)
    where_city = models.CharField(default='where city', max_length=100)
    where_country = models.CharField(default='where country', max_length=100)
    company = models.CharField(default='company', max_length=500)
    current = models.BooleanField(default=False)


class SkillsModel(models.Model):
    type_of_skill = models.CharField(default='type', primary_key=True, max_length=500)
    ref_id = models.ForeignKey(ContentModel)


class ContentSkillModel:
    type_of_skill = models.ForeignKey(SkillsModel)
    content = models.CharField(default='content', max_length=500)


class PublicationModel(models.Model):
    ref_id = models.ForeignKey(ContentModel)
    type_of_publication = models.CharField(default='type', primary_key=True, max_length=500)


class PosterPublicationModel(models.Model):
    type_of_publication = models.ForeignKey(PublicationModel)
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)


class JournalPublicationModel(models.Model):
    type_of_publication = models.ForeignKey(PublicationModel)
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)


class ThesisPublicationModel(models.Model):
    type_of_publication = models.ForeignKey(PublicationModel)
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)


class AbstractPublicationModel(models.Model):
    type_of_publication = models.ForeignKey(PublicationModel)
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)

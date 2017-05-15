from django.db import models
from django.conf import settings


class ContentModel(models.Model):
    ref_id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300, default="Enter your companies name")
    cv = models.FileField(null=True, blank=True)
    bio = models.CharField(default='Your Bio', max_length=10000)
    url = models.URLField(default='https://www.example.com', max_length=400)
    first_name = models.CharField(default='First Name', max_length=400)
    last_name = models.CharField(default='Last Name', max_length=400)
    email_id = models.EmailField(default='example@example.com', max_length=400)
    github = models.URLField(default='https://www.example.com', max_length=400)
    twitter = models.URLField(default='https://www.example.com', max_length=400)
    linkedin = models.URLField(default='https://www.example.com', max_length=400)
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.ref_id)


class EducationModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='education')
    title = models.CharField(default='title', max_length=500)
    from_date = models.DateField()
    to_date = models.DateField()
    where = models.CharField(default='where', max_length=500)
    current = models.BooleanField(default=False)
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)


class ProjectsModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='projects')
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    category = models.CharField(default='category', max_length=500)
    file_name = models.CharField(default='file name', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000, help_text="Markdown Enabled")
    short_description = models.CharField(default='short description', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)


class TutorialsModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='tutorials')
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    file_name = models.CharField(default='file name', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000, help_text="Markdown Enabled")
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)


class ExperienceModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='experience')
    from_date = models.DateField()
    to_date = models.DateField()
    title = models.CharField(default='title', max_length=500)
    where_city = models.CharField(default='where city', max_length=100)
    where_country = models.CharField(default='where country', max_length=100)
    company = models.CharField(default='company', max_length=500)
    current = models.BooleanField(default=False)


class SkillsModel(models.Model):
    ref_id = models.ForeignKey(ContentModel, related_name='skills')
    type_of_skill = models.CharField(default='type', primary_key=True, max_length=500)

    def __str__(self):
        return self.type_of_skill


class SkillsContentModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    type_of_skill = models.ForeignKey(SkillsModel, related_name='skills_content')
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.content


class PublicationsModel(models.Model):
    ref_id = models.ForeignKey(ContentModel, related_name='publications')
    type_of_publication = models.CharField(default='type', primary_key=True, max_length=500)

    def __str__(self):
        return self.type_of_publication


class PublicationsContentModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    type_of_publication = models.ForeignKey(PublicationsModel, related_name='publications_content')
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.content


class TestModel(models.Model):
    test_file_path = models.FilePathField(path=settings.MEDIA_ROOT)


class MetaContentModel(models.Model):
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    header = models.TextField(default="Header content.", help_text="{{header}}")
    footer = models.TextField(default="Footer Content", help_text="{{footer}}")
    meta = models.TextField(default="Meta tags", help_text="{{meta_header}}")

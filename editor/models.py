"""
All models for `editor`.
"""
from django.db import models


class ContentModel(models.Model):
    """
    `ContentModel`, primary model has `ref_id`-PK, `created`, `updated`, `website_name`, `cv`, `bio`, `url`, `first_name`
    `last_name`, `email_id`, `github`, `twitter`, `linkedin`, `file` and `image`
    """
    ref_id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
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
    image = models.ImageField(null=True, blank=True)

    def removed_on_cv_update(self):
        """
        Replaces the file if `CV` already present.
        """
        try:
            obj = ContentModel.objects.get(ref_id=self.ref_id)
        except ContentModel.DoesNotExist:
            return

        if obj.cv and self.cv and obj.cv != self.cv:
            obj.cv.delete()

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = ContentModel.objects.get(ref_id=self.ref_id)
        except ContentModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = ContentModel.objects.get(ref_id=self.ref_id)
        except ContentModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`
         
        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.cv.delete()
        self.file.delete()
        self.image.delete()
        return super(ContentModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`
        
        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_cv_update()
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(ContentModel, self).save()

    def __str__(self):
        return str(self.ref_id)


class EducationModel(models.Model):
    """
    `EducationModel` has `id`-PK, `ref_id`-FK, `title`, `from_date`, `to_date`, `where`, `current`, `file`, and `image`.
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='education')
    title = models.CharField(default='title', max_length=500)
    from_date = models.DateField()
    to_date = models.DateField()
    where = models.CharField(default='where', max_length=500)
    current = models.BooleanField(default=False)
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = EducationModel.objects.get(id=self.id)
        except EducationModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = EducationModel.objects.get(id=self.id)
        except EducationModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.file.delete()
        self.image.delete()
        return super(EducationModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(EducationModel, self).save()


class ProjectsModel(models.Model):
    """
    `ProjectModel` has `id`-PK, `ref_id`-FK, `link`, `title`, `category`, `long_description`, `short_description`
    `file` and `image`.
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='projects')
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    category = models.CharField(default='category', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000, help_text="Markdown Enabled")
    short_description = models.CharField(default='short description', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = ProjectsModel.objects.get(id=self.id)
        except ProjectsModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = ProjectsModel.objects.get(id=self.id)
        except ProjectsModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.file.delete()
        self.image.delete()
        return super(ProjectsModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(ProjectsModel, self).save()


class TutorialsModel(models.Model):
    """
    `TutorialsModel` has `id`-PK, `ref_id`-FK, `link`, `title`, `long_description`, `short_description`, `file` and `image`.
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    ref_id = models.ForeignKey(ContentModel, related_name='tutorials')
    link = models.URLField(default='https://www.example.com', max_length=500)
    title = models.CharField(default='title', max_length=500)
    long_description = models.CharField(default='long description', max_length=10000, help_text="Markdown Enabled")
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = TutorialsModel.objects.get(id=self.id)
        except TutorialsModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = TutorialsModel.objects.get(id=self.id)
        except TutorialsModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.file.delete()
        self.image.delete()
        return super(TutorialsModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(TutorialsModel, self).save()


class ExperienceModel(models.Model):
    """
    `ExperienceModel` has `id`-PK, `ref_id`-FK, `from_date`, `to_date`, `title`, `where_city`, `where_country`, `company` and
    `current`.
    """
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
    """
    `SkillsModel` has `ref_id`-FK and `type_of_skill`.
    """
    ref_id = models.ForeignKey(ContentModel, related_name='skills')
    type_of_skill = models.CharField(default='type', primary_key=True, max_length=500)

    def __str__(self):
        return self.type_of_skill


class SkillsContentModel(models.Model):
    """
    `SkillsContentModel` has `id`-PK, `type_of_skill`-FK, `content`, `file` and `image`
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    type_of_skill = models.ForeignKey(SkillsModel, related_name='skills_content')
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = SkillsContentModel.objects.get(id=self.id)
        except SkillsContentModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = SkillsContentModel.objects.get(id=self.id)
        except SkillsContentModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.file.delete()
        self.image.delete()
        return super(SkillsContentModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(SkillsContentModel, self).save()

    def __str__(self):
        return self.content


class PublicationsModel(models.Model):
    """
    `PublicationsModel` has `ref_id`-FK and `type_of_publication`.
    """
    ref_id = models.ForeignKey(ContentModel, related_name='publications')
    type_of_publication = models.CharField(default='type', primary_key=True, max_length=500)

    def __str__(self):
        return self.type_of_publication


class PublicationsContentModel(models.Model):
    """
    `PublicationsContentModel` has `id`-PK, `type_of_publication`-FK, `content`, `file` and `image`.
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    type_of_publication = models.ForeignKey(PublicationsModel, related_name='publications_content')
    content = models.CharField(default='content', help_text='Markdown Enabled', max_length=500)
    file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def removed_on_file_update(self):
        """
        Replaces the file if `file` already present.
        """
        try:
            obj = PublicationsContentModel.objects.get(id=self.id)
        except PublicationsContentModel.DoesNotExist:
            return

        if obj.file and self.file and obj.file != self.file:
            obj.file.delete()

    def removed_on_image_update(self):
        """
        Replaces the file if `image` already present.
        """
        try:
            obj = PublicationsContentModel.objects.get(id=self.id)
        except PublicationsContentModel.DoesNotExist:
            return

        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, using=None, keep_parents=False):
        """
        Overriding `delete` method of `models.Model`

        Parameters
        ----------
        using
        keep_parents

        Returns
        -------
        super
        """
        self.file.delete()
        self.image.delete()
        return super(PublicationsContentModel, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Overriding `save` method of `models.Model`

        Parameters
        ----------
        force_insert
        force_update
        using
        update_fields

        Returns
        -------
        super
        """
        self.removed_on_file_update()
        self.removed_on_image_update()
        return super(PublicationsContentModel, self).save()

    def __str__(self):
        return self.content


class MetaContentModel(models.Model):
    """
    `MetaContentModel` has `id`-PK, `header`, `footer` and `meta`.
    """
    id = models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False)
    header = models.TextField(default="Header content.", help_text="{{header}}")
    footer = models.TextField(default="Footer Content", help_text="{{footer}}")
    meta = models.TextField(default="Meta tags", help_text="{{meta_header}}")

"""
Schema file for retrieving all the contents of the `editor` models.
"""
import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug
from graphene_django.types import DjangoObjectType

from gollahalli_cms.editor.models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel, MetaContentModel


class ContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `ContentModel`
    """

    class Meta:
        model = ContentModel
        description = "Main content schema."

    def resolve_cv(self, info, **kwargs):
        """
        Resolves CV URL
        
        Parameters
        ----------
        args
        context
        info

        """
        if self.cv and hasattr(self.cv, 'url'):
            return settings.SHARE_URL[:-1] + self.cv.url

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL
        
        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL
        
        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class EducationSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `EducationModel`
    """

    class Meta:
        model = EducationModel
        description = "Education schema"

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL

        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL

        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class ProjectsSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `ProjectsModel`
    """

    class Meta:
        model = ProjectsModel
        description = "Number of projects"

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL

        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL

        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class TutorialsSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `TutorialsModel`
    """

    class Meta:
        model = TutorialsModel
        description = "All tutorial developed"

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL

        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL

        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class ExperienceSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `ExperienceModel`
    """

    class Meta:
        model = ExperienceModel
        description = "All experiences"


class SkillsSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `SkillsModel`
    """

    class Meta:
        model = SkillsModel
        description = "All skills"


class SkillsContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `SkillsContentModel`
    """

    class Meta:
        model = SkillsContentModel
        description = "All skills contents"

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL

        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL

        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class PublicationsSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `PublicationsModel`
    """

    class Meta:
        model = PublicationsModel
        description = "Type of publications"


class PublicationContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `PublicationsContentModel`
    """

    class Meta:
        model = PublicationsContentModel
        description = "All publication contents"

    def resolve_file(self, info, **kwargs):
        """
        Resolves file URL

        Parameters
        ----------
        self
        args
        context
        info

        """
        if self.file and hasattr(self.file, 'url'):
            return settings.SHARE_URL[:-1] + self.file.url

    def resolve_image(self, info, **kwargs):
        """
        Resolves image URL

        Parameters
        ----------
        args
        context
        info

        """
        if self.image and hasattr(self.image, 'url'):
            return settings.SHARE_URL[:-1] + self.image.file


class MetaContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `MetaContentModel`
    """

    class Meta:
        model = MetaContentModel
        description = "All meta tags, headers and footers."


# ----------------------------------------------------------------------------
# Query object
# ----------------------------------------------------------------------------


class Query:
    """
    Query all the contents.
    """
    all_contents = graphene.List(ContentSchema)
    all_education = graphene.List(EducationSchema)
    all_projects = graphene.List(ProjectsSchema)
    all_tutorials = graphene.List(TutorialsSchema)
    all_experience = graphene.List(ExperienceSchema)
    all_skills = graphene.List(SkillsSchema)
    all_skills_content = graphene.List(SkillsContentSchema)
    all_publications = graphene.List(PublicationsSchema)
    all_publications_content = graphene.List(PublicationContentSchema)
    all_meta_content = graphene.List(MetaContentSchema)

    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_contents(self, info, **kwargs):
        """
        Returns all contents of `ContentModel`
        """
        return ContentModel.objects.all()

    def resolve_all_educations(self, info, **kwargs):
        """
        Returns all contents of `EducationModel`
        """
        # We can easily optimize query count in the resolve method
        return EducationModel.objects.select_related('education').all()

    def resolve_all_projects(self, info, **kwargs):
        """
        Returns all contents of `ProjectsModel`
        """
        return ProjectsModel.objects.select_related('projects').all()

    def resolve_all_tutorials(self, info, **kwargs):
        """
        Returns all contents of `TutorialsModel`
        """
        return TutorialsModel.objects.select_related('tutorials').all()

    def resolve_all_experience(self, info, **kwargs):
        """
        Returns all contents of `ExperienceModel`
        """
        return ExperienceModel.objects.select_related('experience').all()

    def resolve_all_skills(self, info, **kwargs):
        """
        Returns all contents of `SkillsModel`
        """
        return SkillsModel.objects.select_related('skills').all()

    def resolve_all_skills_content(self, info, **kwargs):
        """
        Returns all contents of `SkillsContentModel`
        """
        return SkillsContentModel.objects.select_related('skills_content').all()

    def resolve_all_publications(self, info, **kwargs):
        """
        Returns all contents of `PublicationsModel`
        """
        return PublicationsModel.objects.select_related('publications').all()

    def resolve_all_publications_content(self, info, **kwargs):
        """
        Returns all contents of `PublicationsContentModel`
        """
        return PublicationsContentModel.objects.select_related('publications_content').all()

    def resolve_all_meta_content(self, info, **kwargs):
        """
        Returns all content for `MetaContentModel`
        """
        return MetaContentModel.objects.all()

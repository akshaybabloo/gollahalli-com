"""
Schema file for retrieving all the contents of the `editor` models.
"""
import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug
from graphene_django.types import DjangoObjectType

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel


class ContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `ContentModel`
    """

    class Meta:
        model = ContentModel

    def resolve_cv(self, args, context, info):
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

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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


class SkillsSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `SkillsModel`
    """

    class Meta:
        model = SkillsModel


class SkillsContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `SkillsContentModel`
    """

    class Meta:
        model = SkillsContentModel

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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


class PublicationContentSchema(DjangoObjectType):
    """
    Schema DjangoObjectType for `PublicationsContentModel`
    """

    class Meta:
        model = PublicationsContentModel

    def resolve_file(self, args, context, info):
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
            return settings.SHARE_URL[:-1] + self.file.file

    def resolve_image(self, args, context, info):
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


# ----------------------------------------------------------------------------
# Query object
# ----------------------------------------------------------------------------


class Query(graphene.AbstractType):
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

    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_contents(self, args, context, info):
        """
        Returns all contents of `ContentModel`
        """
        return ContentModel.objects.all()

    def resolve_all_educations(self, args, context, info):
        """
        Returns all contents of `EducationModel`
        """
        # We can easily optimize query count in the resolve method
        return EducationModel.objects.select_related('education').all()

    def resolve_all_projects(self, args, context, info):
        """
        Returns all contents of `ProjectsModel`
        """
        return ProjectsModel.objects.select_related('projects').all()

    def resolve_all_tutorials(self, args, context, info):
        """
        Returns all contents of `TutorialsModel`
        """
        return TutorialsModel.objects.select_related('tutorials').all()

    def resolve_all_experience(self, args, context, info):
        """
        Returns all contents of `ExperienceModel`
        """
        return ExperienceModel.objects.select_related('experience').all()

    def resolve_all_skills(self, args, context, info):
        """
        Returns all contents of `SkillsModel`
        """
        return SkillsModel.objects.select_related('skills').all()

    def resolve_all_skills_content(self, args, context, info):
        """
        Returns all contents of `SkillsContentModel`
        """
        return SkillsContentModel.objects.select_related('skills_content').all()

    def resolve_all_publications(self, args, context, info):
        """
        Returns all contents of `PublicationsModel`
        """
        return PublicationsModel.objects.select_related('publications').all()

    def resolve_all_publications_content(self, args, context, info):
        """
        Returns all contents of `PublicationsContentModel`
        """
        return PublicationsContentModel.objects.select_related('publications_content').all()

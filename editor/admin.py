from django import forms
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    ContentSkillModel, PublicationModel, PosterPublicationModel, AbstractPublicationModel, JournalPublicationModel, \
    ThesisPublicationModel

# ----------------------------------------------------------------------------
# Admin Forms
# ----------------------------------------------------------------------------


class ContentAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContentModel
        fields = '__all__'


# ----------------------------------------------------------------------------
# Admin Models
# ----------------------------------------------------------------------------


class ContentAdmin(SingleModelAdmin):
    list_display = ['ref_id', 'created', 'updated', 'website_name']
    form = ContentAdminForm


class EducationAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'to_date', 'from_date', 'where', 'current']

    class Meta:
        model = EducationModel


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'link', 'title', 'category', 'file_name', 'short_description', 'long_description']

    class Mata:
        model = ProjectsModel


class TutorialsAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'link', 'title', 'file_name', 'long_description']

    class Meta:
        model = TutorialsModel


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'to_date', 'from_date', 'title', 'where_city', 'where_country', 'company', 'current']

    class Meta:
        model = ExperienceModel


class SkillAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_skill']

    class Meta:
        model = SkillsModel


class ContentSkillAdmin(admin.ModelAdmin):
    list_display = ['type_of_skill', 'content']

    class Meta:
        model = ContentSkillModel


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_publication']

    class Meta:
        model = PublicationModel


class PosterPublicationAdmin(admin.ModelAdmin):
    list_display = ['type_of_publication', 'content']

    class Mata:
        model = PosterPublicationModel


class AbstractPublicationAdmin(admin.ModelAdmin):
    list_display = ['type_of_publication', 'content']

    class Meta:
        model = AbstractPublicationModel


class JournalPublicationAdmin(admin.ModelAdmin):
    list_display = ['type_of_publication', 'content']

    class Meta:
        model = JournalPublicationModel


class ThesisPublicationAdmin(admin.ModelAdmin):
    list_display = ['type_of_publication', 'content']

    class Meta:
        model = ThesisPublicationModel

# ----------------------------------------------------------------------------
# Admin Registrations
# ----------------------------------------------------------------------------

admin.site.register(ContentModel, ContentAdmin)
admin.site.register(EducationModel, EducationAdmin)
admin.site.register(ProjectsModel, ProjectAdmin)
admin.site.register(TutorialsModel, TutorialsAdmin)
admin.site.register(ExperienceModel, ExperienceAdmin)
admin.site.register(SkillsModel, SkillAdmin)
admin.site.register(ContentSkillModel, ContentSkillAdmin)
admin.site.register(PublicationModel, PublicationAdmin)
admin.site.register(AbstractPublicationModel, AbstractPublicationAdmin)
admin.site.register(PosterPublicationModel, PosterPublicationAdmin)
admin.site.register(JournalPublicationModel, JournalPublicationAdmin)
admin.site.register(ThesisPublicationModel, ThesisPublicationAdmin)

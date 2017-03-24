from django import forms
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    ContentSkillModel, PublicationModel, ContentPublicationModel


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


class EducationAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    to_date = forms.DateField(input_formats='%d-%m-%Y', help_text='dd-mm-yyyy')
    from_date = forms.DateField(input_formats='%d-%m-%Y', help_text='dd-mm-yyyy')

    class Meta:
        model = EducationModel
        fields = '__all__'


class ExperienceAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    to_date = forms.DateField(input_formats='%d-%m-%Y', help_text='dd-mm-yyyy')
    from_date = forms.DateField(input_formats='%d-%m-%Y', help_text='dd-mm-yyyy')

    class Meta:
        model = ExperienceModel
        fields = '__all__'

# ----------------------------------------------------------------------------
# Admin Models
# ----------------------------------------------------------------------------


class ContentAdmin(SingleModelAdmin):
    list_display = ['ref_id', 'created', 'updated', 'website_name']
    form = ContentAdminForm


class EducationAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'to_date', 'from_date', 'where', 'current']
    form = EducationAdminForm


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
    form = ExperienceAdminForm


class SkillAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_skill']

    class Meta:
        model = SkillsModel


class ContentSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_of_skill', 'content']

    class Meta:
        model = ContentSkillModel


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_publication']

    class Meta:
        model = PublicationModel


class ContentPublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_of_publication', 'content']

    class Mata:
        model = ContentPublicationModel


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
admin.site.register(ContentPublicationModel, ContentPublicationAdmin)

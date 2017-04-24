from django import forms
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel


# ----------------------------------------------------------------------------
# Admin Forms
# ----------------------------------------------------------------------------


class ContentAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    bio = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")

    class Meta:
        model = ContentModel
        fields = '__all__'


class EducationAdminForm(forms.ModelForm):
    """
    This object changes the ``to`` and ``from`` CharField to formatted date field.
    """
    to_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy', )
    from_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')

    class Meta:
        model = EducationModel
        fields = '__all__'


class ExperienceAdminForm(forms.ModelForm):
    """
    This object changes the ``to`` and ``from`` CharField to formatted date field.
    """
    to_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    from_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')

    class Meta:
        model = ExperienceModel
        fields = '__all__'


class ProjectAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")

    class Meta:
        model = ProjectsModel
        fields = '__all__'


class TutorialsAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")

    class Meta:
        model = TutorialsModel
        fields = '__all__'

# ----------------------------------------------------------------------------
# Admin Models
# ----------------------------------------------------------------------------


class ContentAdmin(SingleModelAdmin):
    list_display = ['ref_id', 'created', 'updated', 'website_name']
    form = ContentAdminForm


class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_date', 'from_date', 'where', 'current']
    form = EducationAdminForm


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'title', 'category', 'file_name', 'short_description', 'long_description']
    form = ProjectAdminForm


class TutorialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'title', 'file_name', 'long_description']
    form = TutorialsAdminForm


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'to_date', 'from_date', 'title', 'where_city', 'where_country', 'company', 'current']
    form = ExperienceAdminForm


class SkillAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_skill']

    class Meta:
        model = SkillsModel


class ContentSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_of_skill', 'content']

    class Meta:
        model = SkillsContentModel


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'type_of_publication']

    class Meta:
        model = PublicationsModel


class ContentPublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_of_publication', 'content']

    class Mata:
        model = PublicationsContentModel


# ----------------------------------------------------------------------------
# Admin Registrations
# ----------------------------------------------------------------------------

admin.site.register(ContentModel, ContentAdmin)
admin.site.register(EducationModel, EducationAdmin)
admin.site.register(ProjectsModel, ProjectAdmin)
admin.site.register(TutorialsModel, TutorialsAdmin)
admin.site.register(ExperienceModel, ExperienceAdmin)
admin.site.register(SkillsModel, SkillAdmin)
admin.site.register(SkillsContentModel, ContentSkillAdmin)
admin.site.register(PublicationsModel, PublicationAdmin)
admin.site.register(PublicationsContentModel, ContentPublicationAdmin)

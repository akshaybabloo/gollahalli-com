from django import forms
from django.contrib import admin

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel, TestModel, MetaContentModel


# ----------------------------------------------------------------------------
# Admin Forms
# ----------------------------------------------------------------------------


class ContentAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    bio = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")
    image = forms.ImageField()

    class Meta:
        model = ContentModel
        fields = '__all__'


class EducationAdminForm(forms.ModelForm):
    """
    This object changes the ``to`` and ``from`` CharField to formatted date field.
    """
    to_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy', )
    from_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    image = forms.ImageField()

    class Meta:
        model = EducationModel
        fields = '__all__'


class ExperienceAdminForm(forms.ModelForm):
    """
    This object changes the ``to`` and ``from`` CharField to formatted date field.
    """
    to_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    from_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    image = forms.ImageField()

    class Meta:
        model = ExperienceModel
        fields = '__all__'


class ProjectAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")
    image = forms.ImageField()

    class Meta:
        model = ProjectsModel
        fields = '__all__'


class TutorialsAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")
    image = forms.ImageField()

    class Meta:
        model = TutorialsModel
        fields = '__all__'


class PublicationContentAdminForm(forms.ModelForm):
    """
    
    """
    image = forms.ImageField()

    class Meta:
        model = PublicationsContentModel
        fields = '__all__'


class MetaContentAdminForm(forms.ModelForm):
    """
    This object has header, footer and meta CharField to Textarea
    """
    header = forms.CharField(widget=forms.Textarea, help_text="{{header}}")
    footer = forms.CharField(widget=forms.Textarea, help_text="{{footer}}")
    meta = forms.CharField(widget=forms.Textarea, help_text="{{meta_header}}")

    class Meta:
        model = MetaContentModel
        fields = '__all__'

# ----------------------------------------------------------------------------
# Admin Models
# ----------------------------------------------------------------------------


class ContentAdmin(admin.ModelAdmin):
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
        model = PublicationContentAdminForm


class MetaContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'header', 'footer', 'meta']

    class Mata:
        model = MetaContentAdminForm


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
admin.site.register(MetaContentModel, MetaContentAdmin)

# test
admin.site.register(TestModel)

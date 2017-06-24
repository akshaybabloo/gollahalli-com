from django import forms
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel, MetaContentModel


# ----------------------------------------------------------------------------
# Admin Forms
# ----------------------------------------------------------------------------


class ContentAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    ref_id = forms.CharField(widget=forms.NumberInput, initial=1, disabled=True)
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
    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = EducationModel
        fields = '__all__'


class ExperienceAdminForm(forms.ModelForm):
    """
    This object changes the ``to`` and ``from`` CharField to formatted date field.
    """
    to_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    from_date = forms.DateField(input_formats=['%d/%m/%Y'], help_text='dd/mm/yyyy')
    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = ExperienceModel
        fields = '__all__'


class ProjectAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")
    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = ProjectsModel
        fields = '__all__'


class TutorialsAdminForm(forms.ModelForm):
    """
    This object changes the bio CharField to Textarea.
    """
    long_description = forms.CharField(widget=forms.Textarea, help_text="Markdown Enabled")
    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = TutorialsModel
        fields = '__all__'


class PublicationAdminForm(forms.ModelForm):
    """
    Initialises `ref_id=1`.
    """

    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = PublicationsModel
        fields = '__all__'


class PublicationContentAdminForm(forms.ModelForm):
    """
    
    """

    class Meta:
        model = PublicationsContentModel
        fields = '__all__'


class SkillsAdminForm(forms.ModelForm):
    """
    Initialises `ref_id=1`.
    """
    ref_id = forms.ModelChoiceField(queryset=ContentModel.objects.all(), initial=1)

    class Meta:
        model = SkillsModel
        fields = '__all__'


class MetaContentAdminForm(forms.ModelForm):
    """
    This object has header, footer and meta CharField to Textarea
    """
    header = forms.CharField(widget=forms.Textarea, help_text="{{header}}", required=False)
    footer = forms.CharField(widget=forms.Textarea, help_text="{{footer}}", required=False)
    meta = forms.CharField(widget=forms.Textarea, help_text="{{meta_header}}", required=False)

    class Meta:
        model = MetaContentModel
        fields = '__all__'


# ----------------------------------------------------------------------------
# Admin Models
# ----------------------------------------------------------------------------


class ContentAdmin(SingleModelAdmin):
    """
    Admin model for `ContentModel`, it takes only one input.
    """
    list_display = ['ref_id', 'created', 'updated', 'website_name']
    form = ContentAdminForm


class EducationAdmin(admin.ModelAdmin):
    """
    Admin model for `EducationModel`.
    """
    list_display = ['id', 'to_date', 'from_date', 'where', 'current']
    form = EducationAdminForm


class ProjectAdmin(admin.ModelAdmin):
    """
    Admin model for `ProjectsModel`.
    """
    list_display = ['id', 'link', 'title', 'category', 'short_description', 'long_description']
    form = ProjectAdminForm


class TutorialsAdmin(admin.ModelAdmin):
    """
    Admin model for `TutorialsModel`.
    """
    list_display = ['id', 'link', 'title', 'long_description']
    form = TutorialsAdminForm


class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin model for `ExperienceModel`.
    """
    list_display = ['id', 'to_date', 'from_date', 'title', 'where_city', 'where_country', 'company', 'current']
    form = ExperienceAdminForm


class SkillAdmin(admin.ModelAdmin):
    """
    Admin model for `SkillsModel`.
    """
    list_display = ['ref_id', 'type_of_skill']
    form = SkillsAdminForm


class ContentSkillAdmin(admin.ModelAdmin):
    """
    Admin model for `SkillsContentModel`.
    """
    list_display = ['id', 'type_of_skill', 'content']

    class Meta:
        model = SkillsContentModel


class PublicationAdmin(admin.ModelAdmin):
    """
    Admin model for `PublicationsModel`.
    """
    list_display = ['ref_id', 'type_of_publication']
    form = PublicationAdminForm


class ContentPublicationAdmin(admin.ModelAdmin):
    """
    Admin model for `PublicationsContentModel`.
    """
    list_display = ['id', 'type_of_publication', 'content']
    form = PublicationContentAdminForm


class MetaContentAdmin(SingleModelAdmin):
    """
    Admin model for `MetaContentModel`, it takes only single entry.
    """
    list_display = ['id', 'header', 'footer', 'meta']
    form = MetaContentAdminForm


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

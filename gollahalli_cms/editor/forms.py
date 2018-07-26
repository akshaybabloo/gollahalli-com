from django import forms

from gollahalli_cms.editor.models import ContentModel, MetaContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel


class ContentModelForm(forms.ModelForm):
    ref_id = forms.CharField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField(required=False)

    class Meta:
        model = ContentModel
        fields = "__all__"


class EducationContentModelForm(forms.ModelForm):
    """
    Education content form.
    """
    id = forms.CharField(required=False)
    ref_id = forms.CharField(required=False)

    class Meta:
        model = EducationModel
        fields = "__all__"


class ProjectContentModelForm(forms.ModelForm):
    """
    Education content form.
    """
    id = forms.CharField(required=False)
    ref_id = forms.CharField(required=False)

    class Meta:
        model = ProjectsModel
        fields = "__all__"


class TutorialContentModelForm(forms.ModelForm):
    """
    Education content form.
    """
    id = forms.CharField(required=False)
    ref_id = forms.CharField(required=False)

    class Meta:
        model = TutorialsModel
        fields = "__all__"


class ExperienceContentModelForm(forms.ModelForm):
    """
    Education content form.
    """
    id = forms.CharField(required=False)
    ref_id = forms.CharField(required=False)

    class Meta:
        model = ExperienceModel
        fields = "__all__"


class MetaContentModelForm(forms.ModelForm):
    ref_id = forms.CharField(required=False)
    footer = forms.CharField(required=False)
    header = forms.CharField(required=False)
    meta = forms.CharField(required=False)

    class Meta:
        model = MetaContentModel
        fields = "__all__"

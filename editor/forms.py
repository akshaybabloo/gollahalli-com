from django import forms

from .models import ContentModel, MetaContentModel


class ContentModelForm(forms.ModelForm):
    ref_id = forms.CharField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField(required=False)

    class Meta:
        model = ContentModel
        fields = "__all__"


class MetaContentModelForm(forms.ModelForm):
    ref_id = forms.CharField(required=False)
    footer = forms.CharField(required=False)
    header = forms.CharField(required=False)
    meta = forms.CharField(required=False)

    class Meta:
        model = MetaContentModel
        fields = "__all__"

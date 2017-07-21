from django import forms

from .models import ContentModel


class ContentModelForm(forms.ModelForm):
    ref_id = forms.CharField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField(required=False)

    class Meta:
        model = ContentModel
        fields = "__all__"

from django import forms

import utility
from .models import ContentModel
import json


class ContentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, required=True)

    def clean(self):
        data = super(ContentForm, self).clean()
        content = data.get('content')
        if not utility.is_json(content):
            raise forms.ValidationError('The entered content is not a valid JSON string.', code='invalid')

        return content

    def equal(self, value):
        raise forms.ValidationError(value)


class ContentFormModel(forms.ModelForm):
    # def clean(self):
    #     cleaned_data = super(ContentFormModel, self).clean()
    #     content = cleaned_data.get('content')
    #     if not utility.is_json(content):
    #         raise forms.ValidationError('The entered content is not a valid JSON string.', code='invalid')
    #
    #     return content

    class Meta:
        model = ContentModel
        fields = ['content']

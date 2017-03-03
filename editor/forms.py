from django import forms

from .models import ContentModel


class ContentFormModel(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ContentModel
        fields = ['cv', 'bio', 'url', 'first_name', 'last_name', 'email_id', 'github', 'twitter', 'linkedin', 'education_json',
                  'experience_json', 'publication_json', 'research_area_json', 'skills_t1_json', 'skills_t2_json',
                  'projects_json', 'tutorials_json']

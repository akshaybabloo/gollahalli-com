from django import forms

from .models import ContentModel


class ContentFormModel(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields = ['ref_id', 'cv', 'bio', 'url', 'name', 'contact', 'github', 'twitter', 'linkedin', 'education_json',
                  'experience_json', 'publication_json', 'research_area_json', 'skills_t1_json', 'skills_t2_json',
                  'projects_json', 'tutorials_json']

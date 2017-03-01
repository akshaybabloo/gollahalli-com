from django import forms

from .models import ContentModel, AboutMeModel, PortfolioModel


class ContentFormModel(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields = ['ref_id']


class AboutMeFormModel(forms.ModelForm):
    class Meta:
        model = AboutMeModel
        fields = ['cv', 'bio', 'url', 'name', 'contact', 'github', 'twitter', 'linkedin', 'education_json',
                  'experience_json', 'publication_json', 'research_area_json', 'skills_t1_json', 'skills_t2_json']


class PortfolioFormModel(forms.ModelForm):
    class Meta:
        model = PortfolioModel
        fields = ['projects_json', 'tutorials_json']

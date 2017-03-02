from django.contrib import admin
from django import forms
from singlemodeladmin import SingleModelAdmin

from .models import ContentModel


class ContentAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContentModel
        fields = '__all__'


class ContentAdmin(SingleModelAdmin):
    list_display = ['ref_id', 'created', 'updated', 'website_name']
    form = ContentAdminForm


admin.site.register(ContentModel, ContentAdmin)

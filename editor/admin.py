from django.contrib import admin
from .models import *


class EditorAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'content', 'created', 'updated']

    class Meta:
        model = ContentModel

admin.site.register(ContentModel, EditorAdmin)

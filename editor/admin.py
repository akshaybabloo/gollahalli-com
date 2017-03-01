from django.contrib import admin
from .models import ContentModel, AboutMeModel, PortfolioModel


class ContentAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'created', 'updated', 'website_name']

    class Meta:
        model = ContentModel


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['cv']

    class Meta:
        model = AboutMeModel


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['projects_json', 'tutorials_json']

    class Meta:
        model = AboutMeModel

admin.site.register(ContentModel, ContentAdmin)
admin.site.register(AboutMeModel, AboutMeAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)

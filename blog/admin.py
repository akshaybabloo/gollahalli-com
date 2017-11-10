from django.contrib import admin

from blog.forms import BlogForm
from blog.models import BlogModel


class BlogAdmin(admin.ModelAdmin):
    """
    AuthenticatorModel admin.
    """
    list_display = ['blog_id', 'author', 'title', 'body']
    form = BlogForm


admin.site.register(BlogModel, BlogAdmin)

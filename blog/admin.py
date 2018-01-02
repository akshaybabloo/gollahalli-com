from django.contrib import admin

from blog.forms import PostForm
from blog.models import PostModel


class PostAdmin(admin.ModelAdmin):
    """
    AuthenticatorModel admin.
    """
    list_display = ['author', 'title']
    form = PostForm


admin.site.register(PostModel, PostAdmin)

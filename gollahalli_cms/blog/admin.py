from django.contrib import admin

from gollahalli_cms.blog.forms import PostForm
from gollahalli_cms.blog.models import PostModel


class PostAdmin(admin.ModelAdmin):
    """
    PostAdmin admin.
    """
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'tag_list']
    list_filter = ['status', 'created', 'publish', 'author', 'tags']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    form = PostForm

    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(PostModel, PostAdmin)

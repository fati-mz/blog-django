from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views',
                    'status', 'published_at', 'created_at')
    list_filter = ('status', 'author', 'category')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


admin.site.register(Category)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'message', 'aproved',
                    'created_at',)
    list_filter = ('post', 'aproved',)
    search_fields = ['name', 'post']
    summernote_fields = ('message',)

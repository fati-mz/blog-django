from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title' ,'counted_views','status','published_at','created_at')
    list_filter = ('status',)
    search_fields = ['title','content']
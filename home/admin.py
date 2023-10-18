from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('email',)
    search_fields = ['title', 'message']

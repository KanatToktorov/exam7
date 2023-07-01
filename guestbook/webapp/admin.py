from django.contrib import admin

from webapp.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'status', 'created_at']
    list_display_links = ['id', 'author_name']
    list_filter = ['author_name']
    search_fields = ['author_name', 'text']
    fields = ['author_name', 'author_email', 'text', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Guest, GuestAdmin)

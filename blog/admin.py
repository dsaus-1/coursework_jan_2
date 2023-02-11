from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'content', 'image_preview', 'date_created', 'publication_status', 'owner')
from django.contrib import admin
from .models import Sportnews, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')


admin.site.register(Sportnews, NewsAdmin)
admin.site.register(Comment)
# Register your models here.

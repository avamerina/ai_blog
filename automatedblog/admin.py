from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('date', 'topic', 'body', 'picture')
    list_filter = ('date', 'topic')
    search_fields = ('date', 'topic')

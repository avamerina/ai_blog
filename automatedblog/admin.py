from django.contrib import admin
from .models import Topic, Prompt


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('date', 'topic', 'body', 'picture')
    list_filter = ('date', 'topic')
    search_fields = ('date', 'topic')


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', )
    search_fields = ('id', 'body', )

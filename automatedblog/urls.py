from django.urls import path
from automatedblog.views import TopicListView, ArticleDetailView, GenerateContent
from automatedblog.schedulerstart import start

urlpatterns = [
    path('', TopicListView.as_view(), name='home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('start_script/', start, name='start_script'),
    path('cover_blanks/', GenerateContent.cover_blank_topic_fields, name='cover_blanks'),
    path('<int:pk>/generate_article/', GenerateContent.generate_article_manually, name='generate_article_manually')
]

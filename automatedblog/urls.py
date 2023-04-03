from django.urls import path
from automatedblog.views import TopicListView, GenerateContent

urlpatterns = [
    path('', TopicListView.as_view(), name='home'),
    path('generate_content_plan/', GenerateContent.create_content_plan, name='create_content_plan'),
    path('generate_article_for_today/', GenerateContent.create_daily_articles, name='create_article')
]

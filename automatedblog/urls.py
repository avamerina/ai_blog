from django.urls import path
from automatedblog.views import TopicListView, GenerateContent, ArticleDetailView

urlpatterns = [
    path('', TopicListView.as_view(), name='home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('generate_content_plan/', GenerateContent.create_content_plan, name='create_content_plan'),
    path('generate_article_for_today/', GenerateContent.create_daily_articles, name='create_article'),
    path('generate_full_content/', GenerateContent.create_articles_by_new_content_plan, name='create_full_content')
]

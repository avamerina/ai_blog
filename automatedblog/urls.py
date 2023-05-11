from django.urls import path
from automatedblog.views import TopicListView, ArticleDetailView
from automatedblog.job_updater import start

urlpatterns = [
    path('', TopicListView.as_view(), name='home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('start_script/', start, name='start_script')
]

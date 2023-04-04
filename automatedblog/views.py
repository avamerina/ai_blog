import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from automatedblog import generators, services, helpers
from automatedblog.models import Topic


def sass_page_handler(request):
    return render(request, 'index.html')


class TopicListView(ListView):
    """Отображение списка статей на месяц"""
    template_name = 'home.html'
    model = Topic
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    """Отображение детальной страницы статьи"""
    template_name = 'article.html'
    model = Topic
    context_object_name = 'article'


class GenerateContent:
    """Создание контента"""

    @staticmethod
    def create_content_plan(request, *args, **kwargs) -> None | HttpResponse:
        content_plan_text = generators.generate_full_content_plan()
        content_plan_parsed_list = helpers.parse_content_plan(content_plan_text)
        try:
            services.save_topic_to_db(content_plan_parsed_list)
            return redirect('home')
        except Exception as e:
            print(e)
            return HttpResponse('exception while saving topic')

    @staticmethod
    def create_daily_articles(request, *args, **kwargs) -> None | HttpResponse:
        today = datetime.date.today()
        topic_for_today = services.get_topic_for_today(str(today))
        generated_article = generators.generate_daily_article(topic_for_today)
        try:
            services.save_article_to_db(topic_for_today, generated_article)
            return redirect('home')
        except Exception as e:
            print(e)
            return HttpResponse('exception while saving article')

    @staticmethod
    def create_content_for_current_month(request, *args, **kwargs) -> HttpResponse:
        GenerateContent.create_content_plan(request)
        try:
            GenerateContent.create_daily_articles(request)
            return HttpResponse('Created')
        except Exception as e:
            print(e)
            return HttpResponse(e)

    @staticmethod
    def create_articles_by_new_content_plan(request, *args, **kwargs):
        new_topics = services.get_topics_with_no_body_yet()
        print(len(new_topics))
        for topic in new_topics:
            generated_article = generators.generate_daily_article(topic)
            try:
                services.save_article_to_db(topic, generated_article)
            except Exception as e:
                print(e)
        return redirect('home')



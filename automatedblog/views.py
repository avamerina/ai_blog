from typing import Dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from automatedblog import generators, services, helpers
from automatedblog.models import Topic
from automatedblog.exceptions import NoneTypeError
import logging

logger = logging.getLogger(__name__)

def sass_page_handler(request) -> HttpResponse:
    return render(request, 'index.html')


class TopicListView(ListView):
    """Отображение списка статей на месяц"""
    template_name = 'home.html'
    model = Topic
    context_object_name = 'articles'

    def get_context_data(self, *, object_list: list = None, **kwargs: Dict) -> Dict:
        return {'articles': services.get_topics_till_today()}


class ArticleDetailView(DetailView):
    """Отображение детальной страницы статьи"""
    template_name = 'article.html'
    model = Topic
    context_object_name = 'article'


class GenerateContent:
    """Создание контента"""

    @staticmethod
    def create_daily_article(date: str, *args: list, **kwargs: Dict) -> None | HttpResponse:
        """Create one article for current date"""
        try:
            topic = services.get_topic_for_today(str(date))
            logger.info(f'Topic for today: {topic.topic}')
        except AttributeError as a:
            logger.error('No topic for today: ', str(a), exc_info=True)
        try:
            generated_article = generators.generate_daily_article(topic)
            generated_image_url = generators.generate_picture(topic.topic)
            try:
                services.save_article_to_db(topic, generated_article)
                generated_image = helpers.download_image_to_local_media_storage(generated_image_url)
                services.save_image_to_db(topic, generated_image)
            except Exception as e:
                logger.error('An error occurred while saving article and image: %s', str(e), exc_info=True)
                return redirect('home')
        except AttributeError as e:
            if str(e).startswith("'NoneType'"):
                logger.error('Nonetype error daily article create method: ', exc_info=True)
                raise NoneTypeError('no content plan for today custom')
            return redirect('home')







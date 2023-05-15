import logging
from datetime import datetime
import requests
import openai
from django.http import HttpResponse
from django.shortcuts import redirect
from automatedblog import generators, services, helpers, views
from automatedblog.exceptions import NoneTypeError

logger = logging.getLogger(__name__)


def content_plan_script() -> None:
    """Content plan generation script"""
    content_plan_text = generators.generate_full_content_plan()
    content_plan_parsed_list = helpers.parse_content_plan(content_plan_text)
    services.save_topic_to_db(content_plan_parsed_list)


def main_script() -> None | HttpResponse:
    """Daily check up for beginning of the new month to generate content for new month"""
    try:
        today = datetime.today()
        if today.day == 1:
            try:
                services.remove_out_of_plan_topics(services.check_if_any_topic_exists_for_this_month(today))
            except Exception as e:
                logger.error(f'Exception on first day of month condition', str(e), exc_info=True)
                content_plan_script()
        try:
            views.GenerateContent.create_daily_article(date=today.strftime('%Y-%m-%d'))
        except NoneTypeError as n:
            content_plan_script()
            views.GenerateContent.create_daily_article(date=today.strftime('%Y-%m-%d'))
            logger.error('Nonetype error while daily article generation in non first day of month condition: ', str(n), exc_info=True)
            return redirect('home')
    except (Exception, openai.error.APIError, requests.exceptions.Timeout) as e:
        logger.error('In main script: ', str(e), exc_info=True)
        return redirect("home")

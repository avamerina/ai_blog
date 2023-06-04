import logging
import os
import openai
from automatedblog import helpers
from automatedblog.models import Topic


openai.api_key = os.environ.get('OPENAI_KEY')

logger = logging.getLogger(__name__)


def generate_full_content_plan() -> str:
    subject = 'автоматизация бизнес-процессов'
    dates = helpers.get_dates_till_the_end_of_month()
    prompt = f'Создай контент-план с темами для ежедневного выпуска статей по тематике "{subject}" по датам от {dates[0]} до {dates[-1]} в формате гггг-мм-дд - тема.'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    content_plan = response.choices[0].text
    logger.info(f'Generated content plan: {content_plan}')
    return content_plan


def generate_daily_article(topic: Topic) -> str:
    logger.info(f'Generation article by topic: {topic.topic}')
    prompt = f'Напиши подробную статью для блога на тему "{topic.topic}" длиной не менее 10000 символов в виде HTML разметки'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3700,
        n=1,
        stop=None,
        temperature=0.5,
        timeout=60
    )
    article = response.choices[0].text.strip('.')

    return article


def generate_picture(topic: str) -> str:
    """Generate image"""
    result = openai.Image.create(
        prompt=f"Создай изображение в стиле реализм и документализм на тему {topic}",
        n=1,
        size="1024x1024",
    )
    logger.info(f'Image generated: {result.data[0].url}')
    return result.data[0].url


def generate_new_extra_topic(old_title: str) -> str:
    """Generate new topic title"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Подбери новую тему для блога, чтобы она отличалась от '{old_title}'",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    logger.info(f'New topic title generated: {response.choices[0].text.strip()}')
    return response.choices[0].text.strip()



import openai
from automatedblog import helpers
from automatedblog.models import Topic

openai.api_key = "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"


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
    return content_plan


def generate_daily_article(topic: Topic) -> str:
    print('тема для генерации: ', topic.topic)
    prompt = f'Напиши подробную статью для блога на тему "{topic.topic}" длиной не менее 5000 символов c html-разметкой'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3700,
        n=1,
        stop=None,
        temperature=0.5,
    )
    article = response.choices[0].text.strip('.')

    return article


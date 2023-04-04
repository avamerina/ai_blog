from typing import Tuple, List
from automatedblog.models import Topic


def check_topic_if_does_not_exists(title: str) -> True | False:
    """Check if the topic with the given title exists"""
    return not Topic.objects.filter(topic=title).exists()


def save_topic_to_db(topic: List[Tuple]) -> True | False:
    """Save topic from the content plan to the database"""
    try:
        for date, title in topic:
            if check_topic_if_does_not_exists(title):
                new_topic = Topic.objects.create(
                    date=date,
                    topic=title,
                )
                print('CREATED:', new_topic)
    except Exception as e:
        print(e)
        return False
    return True


def get_topics_all() -> Topic:
    return Topic.objects.all()


def get_topic_for_today(today: str) -> Topic:
    """Get Topic corresponding to today's date"""
    return Topic.objects.filter(date=today).first()


def save_article_to_db(topic: Topic, generated_article: str) -> True | False:
    """Add article to Topic"""
    try:
        topic.body = generated_article
        topic.save()

    except Exception as e:
        print(e)
        return False
    return True


def get_article_for_today(today: str) -> str:
    """Get article corresponding to today's date"""
    return Topic.objects.filter(date=today).first().body


def get_topics_with_no_body_yet() -> List[Topic]:
    """Get list of recently generated topics"""
    return list(Topic.objects.all().filter(body=''))


import datetime
import os
import urllib.request
from django.conf import settings
from dateutil.relativedelta import relativedelta
import re
from typing import List, Tuple


def get_dates_till_the_end_of_month() -> List[str]:
    today = datetime.date.today()
    end_of_month = today + relativedelta(day=1, months=1) - datetime.timedelta(days=1)
    delta = end_of_month - today
    dates = [today + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    return [date.strftime('%Y-%m-%d') for date in dates]


def parse_content_plan(content_plan_full_text: str) -> List[Tuple]:
    """
    Парсит дату и тему из текста, содержащего строки в формате "yyyy-mm-dd - тема".
    Возвращает список кортежей с датой и темой.
    """
    pattern = r"(\d{4}-\d{2}-\d{2}) - (.+)"
    matches = re.findall(pattern, content_plan_full_text)
    return matches


def download_image_to_local_media_storage(url: str) -> str | None:
    """Download Image by url to local media storage"""
    try:
        file_name = os.path.basename(url)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        urllib.request.urlretrieve(url, file_path)
        return os.path.relpath(file_path, settings.MEDIA_ROOT)
    except Exception as e:
        print(e)

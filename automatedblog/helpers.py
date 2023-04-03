import datetime
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


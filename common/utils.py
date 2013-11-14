from datetime import date
from calendar import monthrange

def first_and_last_date_in_month(day):
    """Given a day, return the first and last date in that day's month"""
    num_of_days_in_month = monthrange(day.year, day.month)[1]
    start = date(day.year, day.month, 1)
    end = date(day.year, day.month, num_of_days_in_month)
    return (start, end)

def parse_date(date_string):
    if date_string:
        try:
            m, d, y = map(int, date_string.split('/'))
            return date(y, m, d)
        except Exception:
            pass
    return None
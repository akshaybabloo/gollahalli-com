import json

from django.utils.dateparse import parse_datetime


def is_json(my_json):
    try:
        json_object = json.loads(my_json)
        del json_object
    except ValueError as e:
        return False
    return True


def format_date_time(date_time):
    formatted_dt = parse_datetime(str(date_time))
    return formatted_dt.strftime('%b. %d, %Y, %I:%M %p')
import json


def is_json(my_json):
    try:
        json_object = json.loads(my_json)
        del json_object
    except ValueError as e:
        return False
    return True


def format_date_time(date_time):
    return date_time.strftime('%b. %d, %Y, %I:%M %p')
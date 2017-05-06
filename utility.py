import json


def is_json(my_json):
    """
    Checks if the input data is of JSON type.

    Parameters
    ----------
    my_json: JSON Object
        JSON Object to check.

    Returns
    -------
    bool
        `True` or `False`


    Examples
    --------

    >>> json_string = {"hello": "hi"}
    >>> is_json(json_string)
    True

    """
    try:
        json_object = json.loads(my_json)
        del json_object
    except ValueError as e:
        return False
    return True


def format_date_time(date_time):
    """
    Formats Django date and time to Python `datetime`

    Parameters
    ----------
    date_time: datetime
        `datetime` from the database.

    Returns
    -------
    datetime
        formatted datetime

    Examples
    --------

    >>> import datetime
    >>> format_date_time(datetime.datetime.now())
    Feb. 15, 2017, 07:12 PM

    """
    return date_time.strftime('%b. %d, %Y, %I:%M %p')

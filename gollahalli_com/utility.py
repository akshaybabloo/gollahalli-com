import datetime
import json
import os

import requests

GITHUB_KEY = os.environ['GITHUB_KEY']


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


def get_version():
    """
    Get's the latest released version.

    Returns
    -------
    response: dict:
        A dictionary of GitHub content.

    """
    response = requests.get('https://api.github.com/repos/akshaybabloo/gollahalli-me/releases/latest',
                            auth=('akshaybabloo', GITHUB_KEY))
    return json.loads(response.text)


def github_date_time_format(value):
    """
    Strips the date and time of GitHub's format.

    Parameters
    ----------
    value: str
        The vale should be of format `%Y-%m-%dT%H:%M:%Sz`.

    Returns
    -------
    date: datetime
        datetime object.
    """
    date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%Sz')
    return date


def custom_date(value):
    """
    Strips users date.

    >>> c_date = custom_date('10/10/2010')

    Parameters
    ----------
    value: str
        The vale should be of format `%d/%m/%Y`.

    Returns
    -------
    date: datetime
        datetime object
    """
    date = datetime.datetime.strptime(value, '%d/%m/%Y')
    return date

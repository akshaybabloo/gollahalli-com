from django import template
import markdown
import datetime
from pytz import timezone, UTC
from django.conf import settings


# A pytz.timezone object representing the Django project time zone
# Use TZ.localize(mydate) instead of tzinfo=TZ to ensure that DST rules
# are respected
register = template.Library()


@register.filter()
def custom_date(value):
    date = datetime.datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %Z')
    return date.strftime('%d, %b %Y')


@register.filter()
def custom_date_releases(value):
    date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%Sz')
    return date.strftime('%d, %b %Y')


@register.filter()
def markdown_data(value):
    return markdown.markdown(value)


@register.filter()
def url_replace(value):
    return value.replace("http://", "https://")


@register.filter()
def custom_blog_tags(value):
    return ', '.join([str(i.term) for i in value])


@register.filter(is_save=True)
def to_iso8601(dt):
    """
    TODO: Change the location of this to sitemap
    Return a datetime object in ISO 8601 format in UTC, without microseconds
    or time zone offset other than 'Z', e.g. '2011-06-28T00:00:00Z'.
    """
    fmt = '%Y-%m-%dT%H:%M:%SZ'
    if dt is None:
        return datetime.datetime.now().strftime(fmt)
    else:
        return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

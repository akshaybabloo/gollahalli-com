from django import template
import markdown
import datetime

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
    return ', '.join([str(i['term']) for i in value])

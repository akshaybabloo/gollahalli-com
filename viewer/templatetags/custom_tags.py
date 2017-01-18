from django import template
import markdown
import datetime

register = template.Library()


@register.filter()
def custom_date(value):
    date = datetime.datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')
    return date.strftime('%d, %b %Y')


@register.filter()
def markdown_data(value):
    return markdown.markdown(value)


@register.filter()
def url_replace(value):
    value = value.replace("http://", "https://")
    print(value)
    return value
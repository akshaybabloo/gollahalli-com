from django import template
import datetime

register = template.Library()


@register.filter()
def custom_date(value):
    date = datetime.datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')
    return date.strftime('%d, %b %Y')


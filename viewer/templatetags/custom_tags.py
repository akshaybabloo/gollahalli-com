from django import template
import markdown
import datetime
from bs4 import BeautifulSoup

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
    return value.replace("http://", "https://")


@register.filter()
def html_src_replace(value):
    html = BeautifulSoup(value, 'html.parser')
    changed_url = url_replace(html.img['src'])
    return """
    <img src="{}" alt="Akshay Raj Gollahalli"/>
    """.format(changed_url)

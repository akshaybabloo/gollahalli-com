import json

import cloudinary
import cloudinary.api
import feedparser
import markdown
from django.conf import settings
from django.shortcuts import render, redirect

from editor.models import ContentModel


def index(request):
    template = "viewer/home.html"
    try:
        json_content = ContentModel.objects.get(ref_id='1')
        json_object = json.loads(json_content.content)
        content_object = ContentDecode(json_object)
    except Exception as e:
        return redirect('/welcome/')
    context = {'content': content_object}
    return render(request, template, context)


def page_not_found(request):
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url, "error_code": 404,
               "error_message": "Oops, the page you're <br/> looking for does not exist.", "home_link": home_link}
    return render(request, template, context)


def server_error(request):
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url, "error_code": 500,
               "error_message": "Sorry, but the requested page is unavailable <br/> due to a server hiccup.",
               "home_link": home_link}
    return render(request, template, context)


class ContentDecode:
    # ToDo: Change this into nested classes
    def __init__(self, json_object):
        self.json = json_object

    # Bio
    def get_name(self):
        return self.json['about_me']['name']

    def get_bio(self):
        return "".join([markdown.markdown(a) for a in self.json['about_me']['bio']])

    def get_twitter(self):
        return self.json['about_me']['twitter']

    def get_linkedin(self):
        return self.json['about_me']['linkedin']

    def get_github(self):
        return self.json['about_me']['github']

    def get_education(self):
        json_data = self.json['about_me']['education']
        a = [json_data[a] for a in sorted(json_data.keys(), reverse=True)]
        return a

    @staticmethod
    def get_my_image():
        cloudinary.config(
            cloud_name='gollahalli',
            api_key='623378689359255',
            api_secret='bJPo6rNjc9IIDB5ihoyK-ogsRic'
        )

        return cloudinary.CloudinaryImage("akshay_b8wb1x.png").image(gravity="center", opacity=100, radius="max",
                                                                     width=200, x=0, y=0, zoom=0.75, crop="thumb",
                                                                     alt="Akshay Raj Gollahalli")

    def get_experience(self):
        json_data = self.json['experience']
        a = [json_data[a] for a in sorted(json_data.keys(), reverse=True)]
        return a

    # Blog
    @staticmethod
    def get_blog():
        data = feedparser.parse("https://blog.gollahalli.me/?format=rss")
        return data.entries

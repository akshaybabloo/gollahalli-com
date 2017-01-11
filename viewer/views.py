import json
import requests
import re
from urllib.request import urlopen

import cloudinary
import cloudinary.api
import feedparser
import markdown
from django.conf import settings
from django.shortcuts import render, redirect

from editor.models import ContentModel

DEFAULT_BASE_URL = "https://api.github.com/users/akshaybabloo/repos"
GITHUB_KEY = "4921a93fdc0a50ec345ef541a715bf07000303d1"


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


# ============================================================================================
#                                       Website Content Decoder
# ============================================================================================


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

    def get_experience(self):
        json_data = self.json['experience']
        a = [json_data[a] for a in sorted(json_data.keys(), reverse=True)]
        return a

    def get_skills(self):
        json_data = self.json['skills']
        return json_data

    # Portfolio
    def get_portfolio(self):
        json_data = self.json['projects']
        json_data1 = self.json['tutorials']
        a_data = [json_data[a] for a in sorted(json_data.keys(), reverse=True)]

        b1 = 0
        for a1 in a_data:
            a_data[b1]['long_description'] = markdown.markdown(a1['long_description'])
            b1 += 1

        a_data1 = [json_data1[a] for a in sorted(json_data1.keys(), reverse=True)]

        b2 = 0
        for a2 in a_data1:
            a_data1[b2]['long_description'] = markdown.markdown(a2['long_description'])
            b2 += 1

        a_data += a_data1

        category = []
        for a in a_data:
            category.append(a['category'])
        list(set(category))

        return {'portfolio': a_data, 'category': list(set(category))}

    # Blog
    @staticmethod
    def get_blog():
        data = feedparser.parse("https://blog.gollahalli.me/?format=rss")
        return data.entries

    # Other
    @staticmethod
    def get_meta():
        return """
            <meta name="description"
              content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work.">
        <meta name="keywords" content="computer science, brain computer interface, artificial intelligence"/>
        <meta name="author" content="Akshay Raj Gollahalli">
        <meta name="rights" content="All rights reserved by Akshay Raj Gollahalli"/>
        <meta name="theme-color" content="#ef3939"/>

        <meta property="og:title" content="Akshay Raj Gollahalli"/>
        <meta property="og:type" content="website"/>
        <meta property="og:url" content="https://www.gollahalli.me/"/>
        <meta property="og:image" content="https://cdn.gollahalli.me/assets/img/logo.jpg"/>
        <meta property="og:image:secure_url" content="https://cdn.gollahalli.me/assets/img/logo.jpg"/>
        <meta property="og:description"
              content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work."/>

        <meta name="twitter:card" content="summary"/>
        <meta name="twitter:title" content="Akshay Raj Gollahalli"/>
        <meta name="twitter:description"
              content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work."/>
        <meta name="twitter:image:src" content="https://cdn.gollahalli.me/assets/img/logo.jpg"/>
        <meta name="twitter:url" content="https://www.gollahalli.me"/>

        <meta property="fb:app_id" content="1562596197364195"/>
            """

    @staticmethod
    def get_my_image():
        cloudinary.config(
            cloud_name='gollahalli',
            api_key='623378689359255',
            api_secret='bJPo6rNjc9IIDB5ihoyK-ogsRic'
        )

        return re.sub(r'\bwidth="[^"]+"|\bheight="[^"]+"', '',
                      cloudinary.CloudinaryImage("akshay_b8wb1x.png").image(gravity="center", opacity=100, radius="max",
                                                                            width=200, height=200, x=0, y=0, zoom=0.75,
                                                                            crop="thumb", alt="Akshay Raj Gollahalli"))


# ============================================================================================
#                                       GitHub Repo
# ============================================================================================

class GitHubRepo:
    def __init__(self):
        response = urlopen(DEFAULT_BASE_URL)
        data = response.read().decode("utf-8")

        self.data = json.loads(data)
        self.index = len(self.data)
        del response
        del data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def get_github_repo(request):
    template = "viewer/repo.html"
    context = {'content': GitHubRepo}
    return render(request, template, context)


# ============================================================================================
#                                       Change Log
# ============================================================================================

class GitHubReleases:
    def __init__(self):
        response = requests.get('https://api.github.com/repos/akshaybabloo/gollahalli-me/releases',
                                auth=('akshaybabloo', GITHUB_KEY))

        self.data = json.loads(response.text)
        self.index = len(self.data)
        del response

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def get_gollahalli_me_change_log(request):
    template = "viewer/change-log.html"
    context = {'content': GitHubReleases}
    return render(request, template, context)

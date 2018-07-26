import json
import os
import re
from urllib.request import urlopen

import cloudinary
import feedparser
import markdown
import requests
from django.conf import settings
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render

from editor.models import ContentModel
from gollahalli.schema import query

DEFAULT_BASE_URL = "https://api.github.com/users/akshaybabloo/repos"


def index(request):
    """
    Entry point.

    Parameters
    ----------
    request: WSGIRequest
        WSGI request.

    Returns
    -------
    render: HttpResponse
        Returns renderer's.

    """
    try:
        content_object = ContentDecode()
    except ContentModel.DoesNotExist as e:
        raise HttpResponseServerError

    if request.GET.get('format') == 'amp':
        template = "viewer/amp.html"
    elif request.GET.get('format') == 'json':
        return HttpResponse(json.dumps(content_object.get_json), content_type="application/json")
    else:
        template = "viewer/home.html"

    context = {'content': content_object}

    return render(request, template, context)


def page_not_found(request):
    """
    Page not found - 404 page.
    
    Parameters
    ----------
    request: WSGIRequest
        URL request.

    Returns
    -------
    render: HttpResponse
        Returns an rendered HTML page.
    """
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url[1:], "error_code": 404,
               "error_message": "Oops, the page you're <br/> looking for does not exist.", "home_link": home_link}
    return render(request, template, context)


def server_error(request):
    """
    Server error - 500 page.
    
    Parameters
    ----------
    request: WSGIRequest
        URL request.

    Returns
    -------
    render: HttpResponse
        Returns an rendered HTML page.
    """
    url = request.get_full_path()
    home_link = settings.SHARE_URL
    template = "error.html"
    context = {"url": home_link + url[1:], "error_code": 500,
               "error_message": "Sorry, but the requested page is unavailable <br/> due to a server hiccup.",
               "home_link": home_link}
    return render(request, template, context)


# ============================================================================================
#                                       Website Content Decoder
# ============================================================================================


class ContentDecode:
    """
    Content decoder object.
    """

    def __init__(self):
        query_local = '''
                {
                  allContents {
                    refId
                    created
                    updated
                    websiteName
                    cv
                    bio
                    url
                    firstName
                    lastName
                    emailId
                    github
                    twitter
                    linkedin
                    file
                    image
                    education {
                      id
                      title
                      fromDate
                      toDate
                      where
                      current
                      file
                      image
                    }
                    projects {
                      id
                      link
                      title
                      category
                      longDescription
                      shortDescription
                      file
                      image
                    }
                    tutorials {
                      id
                      link
                      title
                      longDescription
                      file
                      image
                    }
                    experience {
                      id
                      fromDate
                      toDate
                      title
                      whereCity
                      whereCountry
                      company
                      current
                    }
                    skills {
                      skillsContent {
                        id
                        typeOfSkill {
                          typeOfSkill
                        }
                        content
                        file
                        image
                      }
                    }
                    publications {
                      publicationsContent {
                        id
                        typeOfPublication {
                          typeOfPublication
                        }
                        content
                        file
                        image
                      }
                    }
                  }
                  allMetaContent {
                    id
                    header
                    footer
                    meta
                  }
                }

                '''
        self.content = query.execute(query_local)
        self.json = json.loads(json.dumps(self.content.data))

    # JSON format
    @property
    def get_json(self):
        return self.json

    # Bio
    @property
    def get_name(self):
        return self.json['allContents'][0]['firstName'] + ' ' + self.json['allContents'][0]['lastName']

    @property
    def get_bio(self):
        return "".join([markdown.markdown(a) for a in self.json['allContents'][0]['bio']])

    @property
    def get_twitter(self):
        return self.json['allContents'][0]['twitter']

    @property
    def get_linkedin(self):
        return self.json['allContents'][0]['linkedin']

    @property
    def get_github(self):
        return self.json['allContents'][0]['github']

    @property
    def get_education(self):
        json_data = self.json['allContents'][0]['education']

        return reversed(json_data)

    @property
    def get_experience(self):
        json_data = self.json['allContents'][0]['experience']
        return reversed(json_data)

    # @property
    # def get_skills(self):
    #     return self.json['skills']
    #
    # @property
    # def get_research_area(self):
    #     return self.json['research_area']
    #
    # @property
    # def get_publications(self):
    #     return self.json['publication']
    #
    # @staticmethod
    # def get_version():
    #     response = requests.get('https://api.github.com/repos/akshaybabloo/gollahalli-me/releases/latest')
    #
    #     return json.loads(response.text)
    #
    # # Portfolio
    # @property
    # def get_portfolio(self):
    #     json_data = self.json['projects']
    #     json_data1 = self.json['tutorials']
    #     a_data = [json_data[a] for a in sorted(json_data.keys(), reverse=True)]
    #
    #     b1 = 0
    #     for a1 in a_data:
    #         a_data[b1]['long_description'] = markdown.markdown(a1['long_description'])
    #         b1 += 1
    #
    #     a_data1 = [json_data1[a] for a in sorted(json_data1.keys(), reverse=True)]
    #
    #     b2 = 0
    #     for a2 in a_data1:
    #         a_data1[b2]['long_description'] = markdown.markdown(a2['long_description'])
    #         b2 += 1
    #
    #     a_data += a_data1
    #
    #     category = []
    #     for a in a_data:
    #         category.append(a['category'])
    #     list(set(category))
    #
    #     return {'portfolio': a_data, 'category': list(set(category))}

    # Blog
    @staticmethod
    def get_blog():
        data = feedparser.parse("https://blog.gollahalli.com/rss")
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
        <meta name="pocket-site-verification" content="4b775d75ad6c86203b944b08a92d21" />

        <meta property="og:title" content="Akshay Raj Gollahalli"/>
        <meta property="og:type" content="website"/>
        <meta property="og:url" content="https://www.gollahalli.com/"/>
        <meta property="og:image" content="https://cdn.gollahalli.com/assets/img/logo.jpg"/>
        <meta property="og:image:secure_url" content="https://cdn.gollahalli.com/assets/img/logo.jpg"/>
        <meta property="og:description"
              content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work."/>

        <meta name="twitter:card" content="summary"/>
        <meta name="twitter:title" content="Akshay Raj Gollahalli"/>
        <meta name="twitter:description"
              content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work."/>
        <meta name="twitter:image:src" content="https://cdn.gollahalli.com/assets/img/logo.jpg"/>
        <meta name="twitter:url" content="https://www.gollahalli.com"/>

        <meta property="fb:app_id" content="1562596197364195"/>
            """

    @staticmethod
    def get_my_image():
        cloudinary.config(
            cloud_name='gollahalli',
            api_key=os.environ['CLOUDINARY_API'],
            api_secret=os.environ['CLOUDINARY_API_SECRET'],
            secure=True
        )

        return re.sub(r'\bwidth="[^"]+"|\bheight="[^"]+"', '',
                      cloudinary.CloudinaryImage("akshay_b8wb1x.png").image(gravity="center", opacity=100, radius="max",
                                                                            width=200, height=200, x=0, y=0, zoom=0.75,
                                                                            crop="thumb", alt="Akshay Raj Gollahalli"))

    @staticmethod
    def get_schema_data():
        return """
        <!-- Schema.org -->

        <script type='application/ld+json'>
            {
              "@context": "http://www.schema.org",
              "@type": "person",
              "name": "Akshay Raj Gollahalli",
              "image" : "https://res.cloudinary.com/gollahalli/image/upload/c_lfill,g_auto,h_200,q_auto:best,w_200/v1477524340/akshay_b8wb1x.jpg",
              "url": "https://www.gollahalli.com/",
              "homeLocation": {
                "@type": "PostalAddress",
                "addressLocality": "Auckland",
                "addressCountry": "New Zealand"
              },
              "email": "akshay@gollahalli.com"
            }

        </script>
        """

    @staticmethod
    def get_site_performance_header():
        return """
            <!-- Google Analytics -->
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

            ga('create', 'UA-74123356-1', 'auto');
            ga('require', 'linkid', {
                'cookieName': '_ela',
                'duration': 45,
                'levels': 5
            });
            ga('send', 'pageview');

        </script>
        """

    @staticmethod
    def get_site_performance_body():
        return """
        <!-- Google Tag Manager -->
        <noscript>
            <iframe src="//www.googletagmanager.com/ns.html?id=GTM-56JZX4"
                    height="0" width="0" style="display:none;visibility:hidden"></iframe>
        </noscript>
        <script>(function (w, d, s, l, i) {
                w[l] = w[l] || [];
                w[l].push({
                    'gtm.start': new Date().getTime(), event: 'gtm.js'
                });
                var f = d.getElementsByTagName(s)[0],
                    j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
                j.async = true;
                j.src =
                    '//www.googletagmanager.com/gtm.js?id=' + i + dl;
                f.parentNode.insertBefore(j, f);
            })(window, document, 'script', 'dataLayer', 'GTM-56JZX4');</script>
        <!-- End Google Tag Manager -->
        """

    @staticmethod
    def get_site_performance_footer():
        return """
        <!-- Facebook app -->
        <script>
            window.fbAsyncInit = function () {
                FB.init({
                    appId: '1562596197364195',
                    xfbml: true,
                    version: 'v2.5'
                });
            };

            (function (d, s, id) {
                var js, fjs = d.getElementsByTagName(s)[0];
                if (d.getElementById(id)) {
                    return;
                }
                js = d.createElement(s);
                js.id = id;
                js.src = "//connect.facebook.net/en_US/sdk.js";
                fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));
        </script>
        """

    @staticmethod
    def get_meta_amp():
        return """
        <title>Akshay Raj Gollahalli</title>
        <meta name="author" content="Akshay Raj Gollahalli" />
        <meta name="description" content="Akshay Raj Gollahalli is a Computer Science researcher currently doing his Ph.D. This website showcases his work." />
        <meta name="keywords" content="computer science, brain computer interface, artificial intelligence" />
        <link rel="canonical" href="https://www.gollahalli.com" />
        <meta name="viewport" content="width=device-width,minimum-scale=1,maximum-scale=1,initial-scale=1">

        """

    @property
    def get_projects_amp(self):
        json_data = self.json['projects']
        return [json_data[a] for a in sorted(json_data.keys(), reverse=True)]

    @property
    def get_tutorials_amp(self):
        json_data = self.json['tutorials']
        return [json_data[a] for a in sorted(json_data.keys(), reverse=True)]


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
        response = requests.get('https://api.github.com/repos/akshaybabloo/gollahalli-me/releases')

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


# ============================================================================================
#                                       Change Log
# ============================================================================================

def get_cookie_policy(request):
    template = "cookie-policy.html"
    context = {}
    return render(request, template, context)

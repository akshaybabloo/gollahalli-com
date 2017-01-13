import datetime

from django.contrib import sitemaps
from django.urls import reverse


class Sitemap(sitemaps.Sitemap):
    def __init__(self, names, priority):
        self.names = names
        self.priority = priority

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)

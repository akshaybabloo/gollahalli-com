import datetime

from django.contrib import sitemaps
from django.urls import reverse


class Sitemap(sitemaps.Sitemap):
    """
    Sitemap object.
    """
    def __init__(self, names, priority):
        """

        Parameters
        ----------
        names
        priority
        """
        self.names = names
        self.priority = priority

    def items(self):
        """

        Returns
        -------

        """
        return self.names

    def changefreq(self, obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

        """
        return 'weekly'

    def lastmod(self, obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

        """
        return datetime.datetime.now()

    def location(self, obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

        """
        return reverse(obj)

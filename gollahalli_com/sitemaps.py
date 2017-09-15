import os

from django.conf import settings
from django.contrib import sitemaps
from django.http import HttpResponse
from django.urls import reverse


class Sitemap(sitemaps.Sitemap):
    """
    Sitemap object.
    """

    def __init__(self, names, priority, changefreq, lastmod):
        """
        The values should be of list and should have the same length as the `names`.
        Parameters
        ----------
        names: list
            List of url names.
        priority: list
            list of priority values.
        changefreq: list
            list of change frequency.
        lastmod: list
            List datetime objects.
        """
        self.names = names
        self.priority = priority
        self.changefreq = self._changefreq(changefreq)
        self.lastmod = self._lastmod(lastmod)

    def items(self):
        """
        Returns URL.
        Returns
        -------
        name: str
            Returns URL
        """
        return self.names

    def _changefreq(self, obj):
        """
        Frequency of updates.
        Parameters
        ----------
        obj: list
            Change frequencies.
        Returns
        -------
        string: str
            Return change frequency.
        """
        return obj

    def _lastmod(self, obj):
        """
        Returns datetime object.
        Parameters
        ----------
        obj: datetiime
            Datetime format.
        Returns
        -------
        obj: datetime
            Returns datetime.
        """

        return obj

    def location(self, obj):
        """
        Parameters
        ----------
        obj: str
            URL name.
        Returns
        -------
        obj: str
            Returns reverse URL.
        """
        return reverse(obj)

    def _urls(self, page, protocol, domain):
        urls = []
        latest_lastmod = None
        all_items_lastmod = False  # track if all items have a lastmod
        for count, item in enumerate(self.paginator.page(page).object_list):
            loc = "%s://%s%s" % (protocol, domain, self.__get('location', item))
            priority = self.__get('priority', item)
            lastmod = self.__get('lastmod', item)[count]
            if all_items_lastmod:
                all_items_lastmod = lastmod is not None
                if (all_items_lastmod and
                        (latest_lastmod is None or lastmod > latest_lastmod)):
                    latest_lastmod = lastmod

            url_info = {
                'item': item,
                'location': loc,
                'lastmod': lastmod,
                'changefreq': self.__get('changefreq', item)[count],
                'priority': str(priority[count] if priority is not None else ''),
            }
            urls.append(url_info)
        if all_items_lastmod and latest_lastmod:
            self.latest_lastmod = latest_lastmod
        return urls


def xsl_content_type(request):
    """
    Converts the MIME type of `sitemap.xsl`.

    Returns
    -------
    HttpResponse: HttpResponse
        Returns `sitemap.xsl`.

    """

    filename = open(os.path.join(settings.STATIC_ROOT, 'sitemap.xsl'))
    print(filename)
    return HttpResponse(filename.read(), content_type="text/xsl")

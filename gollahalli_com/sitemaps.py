from django.contrib import sitemaps
from django.urls import reverse


class Sitemap(sitemaps.Sitemap):
    """
    Sitemap object.
    """

    def __init__(self, names, priority, changefreq, lastmod):
        """

        Parameters
        ----------
        names
        priority
        """
        self.names = names
        self.priority = priority
        self.changefreq = self._changefreq(changefreq)
        self.lastmod = self._lastmod(lastmod)
        # self.

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
        obj

        Returns
        -------
        string: str
            Return `weekly`
        """
        return obj

    def _lastmod(self, obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

        """

        return obj

    def location(self, obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

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

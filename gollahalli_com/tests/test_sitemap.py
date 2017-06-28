from django.test import TestCase, RequestFactory
from gollahalli_com.sitemaps import Sitemap, xsl_content_type
from gollahalli_com.utility import custom_date
from django.test import Client


class SiteMapTest(TestCase):
    """
    Test case for ``sitemap`` urls
    """

    def setUp(self):
        # Testing the URLs

        self.urls = {
            'sitemap index': '/sitemap.xml',
            'sitemap of pages': '/sitemap-pages.xml',
            'sitemap of other': '/sitemap-other.xml'
        }

    def test_sitemap_index(self):
        """
        Test ``sitemap.xml``
        """

        c = Client()
        response = c.get('/sitemap.xml')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('sitemapindex' in response.content.decode('utf-8'))

    def test_sitemap_pages(self):
        """
        Test ``sitemap-pages.xml``
        """
        c = Client()
        response = c.get('/sitemap-pages.xml')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('<priority>1.0</priority>' in response.content.decode('utf-8'))

    def test_sitemap_other(self):
        """
        Test ``sitemap-other.xml``
        """
        c = Client()
        response = c.get('/sitemap-other.xml')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('repo' in response.content.decode('utf-8'))
        self.assertTrue('change-log' in response.content.decode('utf-8'))


class SitemapObjectTest(TestCase):
    """
    Test for ``Sitemap``
    """

    def setUp(self):
        self.sitemap_object = Sitemap(
            ['index'],
            [1.0],
            ['monthly'],
            [custom_date('10/01/2017')]
        )

    def test_items(self):
        """
        Testing ``names``
        """
        self.assertEqual(self.sitemap_object.items(), ['index'])

    def test_changefreq(self):
        """
        Testing ``changefreq``
        """
        self.assertEqual(self.sitemap_object.changefreq, ['monthly'])

    def test_lastmod(self):
        """
        Testing ``lastmod``
        """
        self.assertEqual(self.sitemap_object.lastmod, [custom_date('10/01/2017')])

    def test_location(self):
        """
        Testing ``location``
        """
        self.assertEqual(self.sitemap_object.location('index'), '/')


class XlsTest(TestCase):
    """
    Test case for ``xsl_content_type``
    """

    def setUp(self):
        self.urls = {
            'sitemap index': '/static/sitemap.xsl'
        }

    def test_xls(self):
        """
        Testing ``xsl_content_type``
        """
        c = Client()
        response = c.get('/static/sitemap.xsl')
        self.assertTrue(response.status_code, 200)
        content = list(response.streaming_content)[0].decode('utf-8')
        self.assertTrue('xsl' in content)

    def test_xls_content_type(self):
        """
        Testing ``xsl_content_type`` type
        """
        content_type = xsl_content_type()
        self.assertTrue(content_type['Content-Type'], 'text/xsl')

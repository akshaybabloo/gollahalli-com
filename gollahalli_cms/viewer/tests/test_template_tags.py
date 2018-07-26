from django.test import TestCase

from gollahalli_cms.viewer.templatetags.custom_tags import custom_date, custom_date_releases, markdown_data, url_replace, \
    custom_blog_tags


class TemplateTagsTestings(TestCase):
    """
    Test case for ``custom_tags``.
    """

    def test_custom_date(self):
        """
        Testing ``custom_date``
        """
        date_time_str = 'Sat, 01 Jul 2017 19:22:54 GMT'
        out_dt = "01, Jul 2017"

        cd = custom_date(date_time_str)
        self.assertEqual(str(cd), out_dt)

    def test_custom_date_releases(self):
        """
        Testing ``custom_date_releases``
        """
        date_time_str = '2017-06-13T03:54:17Z'
        out_dt = "13, Jun 2017"

        cd = custom_date_releases(date_time_str)
        self.assertEqual(str(cd), out_dt)

    def test_markdown_data(self):
        """
        Testing ``markdown_data``
        """
        in_data = '# hello'
        out_data = '<h1>hello</h1>'

        data = markdown_data(in_data)
        self.assertEqual(data, out_data)

    def test_url_replace(self):
        """
        Testing ``url_replace``
        """
        in_data = 'http://example.com'
        out_data = 'https://example.com'

        data = url_replace(in_data)
        self.assertEqual(data, out_data)

    def test_custom_blog_tags(self):
        """
        Testing ``custom_blog_tags``
        """
        in_data = {'tags': [{'scheme': None, 'term': 'Car-ND', 'label': None},
                            {'scheme': None, 'term': 'Python', 'label': None},
                            {'scheme': None, 'term': 'Computer Vision', 'label': None}]}
        out_data = 'Car-ND, Python, Computer Vision'

        data = custom_blog_tags(in_data['tags'])
        self.assertEqual(data, out_data)

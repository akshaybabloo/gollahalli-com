import datetime
import json

from django.test import TestCase

from gollahalli_com import utility


class UtilityTest(TestCase):
    """
    Test case for Utility
    """

    def test_json(self):
        """
        Testing ``is_json``
        """
        json_string = {"hello": "hi"}
        self.assertTrue(utility.is_json(json.dumps(json_string)))

    def test_format_date_time(self):
        """
        Testing ``format_date_time``
        """
        date_time_str = datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)

        self.assertEqual(utility.format_date_time(date_time_str), 'Dec. 06, 2007, 03:29 PM')

    def test_get_version(self):
        """
        Testing ``get_version``
        """
        github_version = utility.get_version()

        self.assertEqual(github_version['target_commitish'], 'master')

    def test_github_date_time_format(self):
        """
        Testing ``github_date_time_format``
        """

        date_time_str = '2017-06-13T03:54:17Z'
        out_dt = "2017-06-13 03:54:17"

        date_time_str = str(utility.github_date_time_format(date_time_str))

        self.assertEqual(date_time_str, out_dt)

    def test_custom_date(self):
        """
        Testing ``custom_date``
        """

        in_d = '10/10/2010'
        out_d = "2010-10-10 00:00:00"

        self.assertEqual(str(utility.custom_date(in_d)), out_d)

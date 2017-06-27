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

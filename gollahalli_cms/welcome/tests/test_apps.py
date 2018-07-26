from django.apps import apps
from django.test import TestCase

from welcome.apps import WelcomeConfig


class WelcomeConfigTests(TestCase):
    """
    Test case for ``EditorConfig``
    """

    def test_welcome_config(self):
        """
        Testing ``EditorConfig`` class.
        """
        app = WelcomeConfig

        self.assertEqual(app.name, 'welcome')
        self.assertEqual(apps.get_app_config('welcome').name, 'welcome')

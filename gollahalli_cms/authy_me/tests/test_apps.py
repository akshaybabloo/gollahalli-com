from django.test import TestCase
from django.apps import apps

from authy_me.apps import AuthyMeConfig


class AuthyMeConfigTests(TestCase):
    """
    Test case for ``AuthyMeConfig``
    """

    def test_authy_me_config(self):
        """
        Testing ``AuthyMeConfig`` class.
        """
        app = AuthyMeConfig

        self.assertEqual(app.name, 'authy_me')
        self.assertEqual(apps.get_app_config('authy_me').name, 'authy_me')

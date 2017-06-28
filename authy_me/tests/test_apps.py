from django.test import TestCase

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

        self.assertTrue(app.name, 'authy_me')

from django.test import TestCase

from viewer.apps import ViewerConfig


class ViewerConfigTests(TestCase):
    """
    Test case for ``ViewerConfig``
    """

    def test_editor_config(self):
        """
        Testing ``ViewerConfig`` class.
        """
        app = ViewerConfig

        self.assertTrue(app.name, 'viewer')

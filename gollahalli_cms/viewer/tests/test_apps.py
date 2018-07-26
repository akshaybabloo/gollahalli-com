from django.apps import apps
from django.test import TestCase

from gollahalli_cms.viewer.apps import ViewerConfig


class ViewerConfigTests(TestCase):
    """
    Test case for ``ViewerConfig``
    """

    def test_viewer_config(self):
        """
        Testing ``ViewerConfig`` class.
        """
        app = ViewerConfig

        self.assertEqual(app.name, 'viewer')
        self.assertEqual(apps.get_app_config('viewer').name, 'viewer')

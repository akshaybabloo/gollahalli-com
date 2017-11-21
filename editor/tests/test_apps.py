from django.apps import apps
from django.test import TestCase

from editor.apps import EditorConfig


class EditorConfigTests(TestCase):
    """
    Test case for ``EditorConfig``
    """

    def test_editor_config(self):
        """
        Testing ``EditorConfig`` class.
        """
        app = EditorConfig

        self.assertEqual(app.name, 'editor')
        self.assertEqual(apps.get_app_config('editor').name, 'editor')

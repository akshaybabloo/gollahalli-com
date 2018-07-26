from django.test import TestCase
from gollahalli_cms.custom_storage import MediaStorage, StaticStorage
from django.conf import settings


class MediaStorageTests(TestCase):
    """
    Test case for ``MediaStorage``.
    """
    def test_location(self):
        """
        Testing ``location`` variable.
        """
        media = MediaStorage()

        self.assertEqual(media.location, settings.MEDIAFILES_LOCATION)


class StaticStorageTests(TestCase):
    """
    Test case for ``StaticStorage``.
    """
    def test_location(self):
        """
        Testing ``location`` variable.
        """
        media = StaticStorage()

        self.assertEqual(media.location, settings.STATICFILES_LOCATION)

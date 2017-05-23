from io import BytesIO
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from editor.models import ContentModel
from PIL import Image

import unittest.mock as mock
import pytz
import datetime


def mock_datetime_now():
    """
    Date and time with timezone.

    Returns
    -------
    datetime- datetime
        Datetime object.
    """
    return datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)


class ContentModelTest(TestCase):
    """
    Test case for `ContentModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `ContentModel` and mocks django `timezone`
        
        """
        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        ContentModel.objects.create(ref_id=1,
                                    website_name="Akshay Raj Gollahalli",
                                    cv=SimpleUploadedFile('best_file_eva.txt',
                                                          'these are the file contents!'.encode('utf-8')),
                                    bio="bio",
                                    url="https://www.example.com",
                                    first_name="Some name",
                                    last_name="last name",
                                    email_id="name@example.com",
                                    github="https://www.github.com",
                                    twitter="https://www.twitter.com",
                                    linkedin="https://www.linkedin.com",
                                    file=SimpleUploadedFile('best_file_eva1.txt',
                                                            'these are the file contents!'.encode('utf-8')),
                                    image=InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', im_io,
                                                               None))

    def test_model(self):
        """
        Tests `ref_id`, `website_name`, `bio`, `url`, `first_name`, `last_name`, `email_id`, `github`, `twitter` and 
        `linkedin`.

        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.ref_id, 1)
        self.assertEqual(content.website_name, "Akshay Raj Gollahalli")
        self.assertEqual(content.bio, "bio")
        self.assertEqual(content.url, "https://www.example.com")
        self.assertEqual(content.first_name, "Some name")
        self.assertEqual(content.last_name, "last name")
        self.assertEqual(content.email_id, "name@example.com")
        self.assertEqual(content.github, "https://www.github.com")
        self.assertEqual(content.twitter, "https://www.twitter.com")
        self.assertEqual(content.linkedin, "https://www.linkedin.com")

    def test_timedate(self):
        """
        Tests `created` and `updated` date and time.
        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.created, mock_datetime_now())
        self.assertEqual(content.updated, mock_datetime_now())

    def test_uploads(self):
        """
        Tests file uploads of `cv`, `file`, and `image`
        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.cv, content.cv.name)
        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class EducationModelTest(TestCase):
    pass


class ProjectsModelTest(TestCase):
    pass


class TutorialsModelTest(TestCase):
    pass


class ExperienceModelTest(TestCase):
    pass


class SkillsModelTest(TestCase):
    pass


class SkillsContentModelTest(TestCase):
    pass


class PublicationsModelTest(TestCase):
    pass


class PublicationsContentModelTest(TestCase):
    pass


class MetaContentModelTest(TestCase):
    pass

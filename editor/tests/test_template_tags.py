import os
import shutil
from io import BytesIO

from PIL import Image
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile
from django.test import TestCase

from editor.models import ContentModel
from editor.templatetags.model_tags import check_model_exists
from editor.templatetags.nav_tags import has_string_in_path


class TestTemplateTagsNav(TestCase):
    """
    Test case for ``templatetags/nav_tags.py``
    """

    def test_has_string_in_path(self):
        """
        Tests ``has_string_in_path``
        """
        content = '/portal/index/'
        content = has_string_in_path(content, 'portal')

        self.assertTrue(content, True)

    def test_has_string_in_path_false(self):
        """
        Tests ``has_string_in_path``
        """
        content = '/portal/index/'
        content = has_string_in_path(content, 'hello')

        self.assertFalse(content, False)


# class TestTemplateTagsModel(TestCase):
#     """
#     Test case for ``templatetags/model_tags.py``
#     """
#
#     def setUp(self):
#
#         im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
#         im_io = BytesIO()  # a BytesIO object for saving image
#         im.save(im_io, 'JPEG')  # save the image to im_io
#         im_io.seek(0)
#
#         ContentModel.objects.create(ref_id=1,
#                                     website_name="Akshay Raj Gollahalli",
#                                     cv=SimpleUploadedFile('best_file_eva.txt',
#                                                           'these are the file contents!'.encode('utf-8')),
#                                     bio="bio",
#                                     url="https://www.example.com",
#                                     first_name="Some name",
#                                     last_name="last name",
#                                     email_id="name@example.com",
#                                     github="https://www.github.com",
#                                     twitter="https://www.twitter.com",
#                                     linkedin="https://www.linkedin.com",
#                                     file=SimpleUploadedFile('content_model.txt',
#                                                             'these are the file contents!'.encode('utf-8')),
#                                     image=InMemoryUploadedFile(im_io, None, 'content_model.jpg', 'image/jpeg', im_io,
#                                                                None))
#
#     def test_check_model_exists(self):
#         """
#         Tests ``check_model_exists``
#         """
#
#         content = check_model_exists()
#
#         self.assertTrue(content, True)
#
#     def test_check_model_exists_false(self):
#         """
#         Tests ``check_model_exists`` false.
#         """
#
#         ContentModel.objects.all().delete()
#
#         content = check_model_exists()
#
#         self.assertFalse(content, False)
#
#     def tearDown(self):
#
#         for file_object in os.listdir(settings.MEDIA_ROOT):
#             file_object_path = os.path.join(settings.MEDIA_ROOT, file_object)
#             if os.path.isfile(file_object_path):
#                 os.unlink(file_object_path)
#             else:
#                 shutil.rmtree(file_object_path)

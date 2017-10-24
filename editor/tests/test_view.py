from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile, InMemoryUploadedFile
from django.test import TestCase, Client
from io import BytesIO
from PIL import Image


class ViewsTests(TestCase):
    """
    Test case for ``views``
    """

    def setUp(self):
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.user = User.objects.create_user('local_user', 'example@example.com', 'local_pass')

        c = Client()
        c.login(username=self.my_admin.username, password=password)

    def test_portal_home(self):
        """
        Tests `portal_home`
        """
        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.get('/portal', follow=True)

        self.assertEqual(response.status_code, 200)

    def test_editor_home(self):
        """
        Tests `editor_home`
        """

        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.get('/portal/editor', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['content'], False)

    def test_content_home(self):
        """
        Tests `content_home`.
        """

        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.get('/portal/editor/content')

        self.assertEqual(response.status_code, 200)

    def test_content_home_post(self):
        """
        Tests `content_home` post.
        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.post('/portal/editor/content', data={'ref_id': 1,
                                                          'website_name': "Akshay Raj Gollahalli",
                                                          'cv': SimpleUploadedFile('best_file_eva.txt',
                                                                                   'these are the file contents!'.encode(
                                                                                       'utf-8')),
                                                          'bio': "bio",
                                                          'url': "https://www.example.com",
                                                          'first_name': "Some name",
                                                          'last_name': "last name",
                                                          'email_id': "name@example.com",
                                                          'github': "https://www.github.com",
                                                          'twitter': "https://www.twitter.com",
                                                          'linkedin': "https://www.linkedin.com",
                                                          'file': SimpleUploadedFile('content_model.txt',
                                                                                     'these are the file contents!'.encode(
                                                                                         'utf-8')),
                                                          'image': InMemoryUploadedFile(im_io, None,
                                                                                        'content_model.jpg',
                                                                                        'image/jpeg', im_io,
                                                                                        None)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form_msg'], 'Updates saved')

    def test_meta_home(self):
        """
        Tests `meta_home`.
        """

        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.get('/portal/editor/meta')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['content'], False)

    def test_meta_home_post(self):
        """
        Tests `meta_home` post.
        """

        c = Client()
        c.login(username=self.my_admin.username, password='mypassword')

        response = c.post('/portal/editor/meta', data={'ref_id': 1,
                                                       'header': "some header",
                                                       'footer': "some footer",
                                                       'meta': "some meta"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form_msg'], 'Updates saved')

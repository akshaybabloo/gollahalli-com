import json

from django.contrib.auth.models import User
from django.test import TestCase, Client


class PagesTest(TestCase):
    """
    Tests HTML pages.
    """
    # def setUp(self):
    #     User.objects.all().delete()

    def test_home(self):
        """
        Tests ``home`` page.
        """

        c = Client()
        response = c.get('/welcome', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertInHTML('Welcome!', response.content.decode('utf-8'))

    # def test_home_post(self):
    #     """
    #     Tests ``home`` post.
    #     """
    #
    #     c = Client()
    #     response = c.post('/welcome/',
    #                       data={'first_name': 'John', 'last_name': 'Doe', 'username': 'john',
    #                             'email': 'test@testing.com', 'password': 'testpassword'})
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertInHTML('Welcome!', response.content.decode('utf-8'))

    # def tearDown(self):
    #     User.objects.all().delete()


class JSONReturnTest(TestCase):
    """
    Tests JSON objects returned.
    """

    def test_db_url(self):
        """
        Tests ``db`` url.
        """

        c = Client()
        response = c.get('/welcome/check/db', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

    def test_aws_url(self):
        """
        Tests ``aws`` url.
        """

        c = Client()
        response = c.get('/welcome/check/aws', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

    def test_ssl_url(self):
        """
        Tests ``ssl`` url.
        """

        c = Client()
        response = c.get('/welcome/check/ssl', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

    def test_s3_url(self):
        """
        Tests ``s3`` url.
        """

        c = Client()
        response = c.get('/welcome/check/s3', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

    def test_smtp_url(self):
        """
        Tests ``smtp`` url.
        """

        c = Client()
        response = c.get('/welcome/check/smtp', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

    def test_authy_url(self):
        """
        Tests ``authy`` url.
        """

        c = Client()
        response = c.get('/welcome/check/authy', follow=True)

        self.assertIn('expression', response.content.decode('utf-8'))

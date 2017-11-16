from django.test import TestCase, Client
import json

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

        self.assertEqual(response.content, b'{"expression": true}')

    def test_aws_url(self):
        """
        Tests ``aws`` url.
        """

        c = Client()
        response = c.get('/welcome/check/aws', follow=True)

        content = json.loads(response.content)

        self.assertEqual(response.content.decode('utf-8'), json.dumps(content))

    def test_ssl_url(self):
        """
        Tests ``ssl`` url.
        """

        c = Client()
        response = c.get('/welcome/check/ssl', follow=True)

        content = json.loads(response.content)

        self.assertEqual(response.content.decode('utf-8'), json.dumps(content))

    def test_s3_url(self):
        """
        Tests ``s3`` url.
        """

        c = Client()
        response = c.get('/welcome/check/s3', follow=True)

        content = json.loads(response.content)

        self.assertEqual(response.content.decode('utf-8'), json.dumps(content))

    def test_smtp_url(self):
        """
        Tests ``smtp`` url.
        """

        c = Client()
        response = c.get('/welcome/check/smtp', follow=True)

        content = json.loads(response.content)

        self.assertEqual(response.content.decode('utf-8'), json.dumps(content))

    def test_authy_url(self):
        """
        Tests ``authy`` url.
        """

        c = Client()
        response = c.get('/welcome/check/authy', follow=True)

        content = json.loads(response.content)

        self.assertEqual(response.content.decode('utf-8'), json.dumps(content))

from django.test import TestCase, Client


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

        self.assertEqual(response.content,
                         b'{"expression": false, "error": "An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records."}')

    def test_ssl_url(self):
        """
        Tests ``ssl`` url.
        """

        c = Client()
        response = c.get('/welcome/check/ssl', follow=True)

        self.assertEqual(response.content,
                         b'{"expression": false, "error": "This connection is not secured, you can still continue but I would\'nt recommend it."}'
                         )

    def test_s3_url(self):
        """
        Tests ``s3`` url.
        """

        c = Client()
        response = c.get('/welcome/check/s3', follow=True)

        self.assertEqual(response.content, b'{"expression": false}')

    def test_smtp_url(self):
        """
        Tests ``smtp`` url.
        """

        c = Client()
        response = c.get('/welcome/check/smtp', follow=True)

        self.assertEqual(response.content, b'{"expression": false, "error": "User matching query does not exist."}')

    def test_authy_url(self):
        """
        Tests ``authy`` url.
        """

        c = Client()
        response = c.get('/welcome/check/authy', follow=True)

        self.assertEqual(response.content, b'{"expression": true}')

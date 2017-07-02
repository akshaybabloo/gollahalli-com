from django.test import TestCase, Client
from django.contrib.auth.models import User
from authy_me.views import users_js, log_me_in, auth_2fa


class ViewsTests(TestCase):
    """
    Test case for ``views``
    """

    def setUp(self):
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

        c = Client()
        c.login(username=self.my_admin.username, password=password)

    def test_users_js(self):
        """
        Testing ``users_js``
        """
        c = Client()
        response = c.get('/static/js/users.js', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/javascript')

    def test_log_me_in_admin(self):
        """
        Testing ``log_me_in`` redirect to admin if already logged in.
        """
        c = Client()
        c.login(username='myuser', password='mypassword')
        response = c.get('/login/')

        self.assertRedirects(response, '/admin/')



    def test_auth_2fa(self):
        pass

    def tearDown(self):
        pass

from django.test import TestCase, Client
from django.contrib.auth.models import User
from authy_me.models import AuthenticatorModel


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

    def test_log_me_in_post_wrong_user(self):
        """
        Testing ``log_me_in`` for post with wrong user.
        """

        c = Client()
        response = c.post('/login/', data={'username': 'user', 'password': 'pass'})
        self.assertIn("Your username and password didn\'t match. Please try again.", response.content.decode('utf-8'))

    # def test_log_me_in_post_not_staff(self):
    #     """
    #     Testing ``log_me_in`` for post with not staff.
    #     """
    #
    #     c = Client()
    #     response = c.post('/login/', data={'username': 'local_user', 'password': 'local_pass'})
    #     self.assertRedirects(response, '/')

    def test_log_me_in_post_is_staff(self):
        """
        Testing ``log_me_in`` for post with is staff.
        """

        c = Client()
        response = c.post('/login/', data={'username': 'myuser', 'password': 'mypassword'})
        self.assertRedirects(response, '/admin/authy_me/authenticatormodel/')

    def test_auth_2fa(self):
        """
        Testing ``auth_2fa``
        """

        auth = AuthenticatorModel.objects.create(id=self.my_admin.id, user_id=self.my_admin, first_name='Akshay Raj',
                                                 last_name='Gollahalli', phone_number='+123456789',
                                                 email_id='example@example.com', authy_id='1234567')

        c = Client()
        response = c.post('/login/', data={'username': 'myuser', 'password': 'mypassword'})

        self.assertRedirects(response, '/login/2fa/')
        auth.delete()

    def tearDown(self):
        self.my_admin.delete()
        self.user.delete()

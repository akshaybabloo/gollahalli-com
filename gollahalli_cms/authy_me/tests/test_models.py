from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from authy_me.models import AuthenticatorModel


class AuthenticatorModelTest(TestCase):
    """
    Test case for `AuthenticatorModel`
    """

    def setUp(self):
        """
        Sets up `AuthenticatorModel`.
        """
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

        c = Client()
        c.login(username=self.my_admin.username, password=password)

        self.auth = AuthenticatorModel.objects.create(id=self.my_admin.id, user_id=self.my_admin, first_name='Akshay Raj',
                                                      last_name='Gollahalli', phone_number='+123456789',
                                                      email_id='example@example.com', authy_id='1234567')

    def test_model(self):
        """
        Tests `id`, `first_name`, `last_name`, `phone_number`, `email_id` and `authy_id`
        """
        content = AuthenticatorModel.objects.get(id=self.my_admin.id)

        self.assertEqual(content.id, self.my_admin.id)
        self.assertEqual(content.first_name, 'Akshay Raj')
        self.assertEqual(content.last_name, 'Gollahalli')
        self.assertEqual(content.phone_number, '+123456789')
        self.assertEqual(content.email_id, 'example@example.com')
        self.assertEqual(content.authy_id, '1234567')

    def tearDown(self):
        self.auth.delete()
        self.my_admin.delete()

from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client, RequestFactory
from mock import Mock

from authy_me.models import AuthenticatorModel
from authy_me.utils import is_int, has_2fa, get_user_from_sid, get_uuid_json, generate_password, check_hashed_password


class UtilityTests(TestCase):
    """
    Test case for ``Utility``
    """

    def setUp(self):
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.my_admin_false = User.objects.create_superuser('myuser1', 'myemail@test.com', password)

        self.c = Client()
        self.c.login(username=self.my_admin.username, password=password)

        self.factory = RequestFactory()
        self.request = self.factory.get("/admin/auth/user/{}/change/".format(self.my_admin.id), follow=True)
        self.factory.user = self.my_admin

        self.c2 = Client()
        self.c2.login(username=self.my_admin_false.username, password=password)

        self.factory2 = RequestFactory()
        self.request2 = self.factory.get("/admin/auth/user/{}/change/".format(self.my_admin_false.id), follow=True)
        self.factory2.user = self.my_admin_false

        self.auth = AuthenticatorModel.objects.create(id=self.my_admin.id, user_id=self.my_admin,
                                                      first_name='Akshay Raj',
                                                      last_name='Gollahalli', phone_number='+123456789',
                                                      email_id='example@example.com', authy_id='1234567')

    def test_is_int(self):
        """
        Testing ``is_int``
        """
        int_true = is_int(1)
        int_false = is_int("a")

        self.assertTrue(int_true)
        self.assertFalse(int_false)

    def test_has_2fa(self):
        """
        Testing ``has_2fa``
        """

        response = has_2fa(self.factory)
        response_false = has_2fa(self.factory2)

        self.assertTrue(response)
        self.assertFalse(response_false)

    def test_has_2fa_assertion(self):
        """
        Testing ``has_2fa``
        """
        response = has_2fa(MockUserName())

        self.assertFalse(response)
        self.assertRaises(User.DoesNotExist)

    def test_get_user_from_sid(self):
        """
        Testing ``get_user_from_sid``
        """
        c = Client()
        c.login(username="myuser1", password="mypassword")
        session_id = get_user_from_sid(c.session.session_key)

        self.assertEqual(session_id, str(self.my_admin_false.id))

    def test_mock_class(self):
        """
        Testing ``Mock`` class
        """

        cl = MockUserName()

        self.assertEqual(cl.user(), 'unknown_user')

    def test_uuid(self):
        """
        Testing uuids.
        """

        content = get_uuid_json()

        self.assertTrue(type(content), type(dict))
        self.assertTrue(type(content['uuid']), type(list))

    def test_generate_password(self):
        """
        Tests `generate_password`
        """

        content = generate_password('hello', '123')

        self.assertTrue(type(content), type(str))

    def test_check_hashed_password(self):
        """
        Tests `check_hashed_password`
        """

        content = generate_password('hello')
        content = check_hashed_password('hello', content)

        self.assertTrue(content, True)

    def test_check_hashed_password_false(self):
        """
        Tests `check_hashed_password` false.
        """

        content = generate_password('hello')
        content = check_hashed_password('hello1', content)

        self.assertFalse(content, False)

    def tearDown(self):
        self.auth.delete()
        self.my_admin.delete()
        # self.my_admin_false.delete()


class MockUserName:
    """
    Mock object for username.
    """

    def user(self):
        return "unknown_user"

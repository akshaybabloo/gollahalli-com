from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client

from authy_me.models import AuthenticatorModel
from authy_me.utils import is_int, has_2fa, get_user_from_sid, get_uuid_json, generate_password, check_hashed_password, \
    check_users


class UtilityTests(TestCase):
    """
    Test case for ``Utility``
    """

    def setUp(self):
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.my_admin_false = User.objects.create_superuser('myuser1', 'myemail@test.com', password)

        c = Client()
        c.login(username=self.my_admin.username, password=password)

        self.auth = AuthenticatorModel.objects.create(id=self.my_admin.id, user_id=self.my_admin,
                                                      first_name='Akshay Raj',
                                                      last_name='Gollahalli', phone_number='+123456789',
                                                      email_id='example@example.com', authy_id='1234567')
        self.auth_false = AuthenticatorModel.objects.create(id=43, user_id=self.my_admin_false,
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
        response = has_2fa(self.my_admin)
        response_false = has_2fa(self.my_admin_false)

        self.assertTrue(response)
        self.assertFalse(response_false)

    def test_has_2fa_assertion(self):
        """
        Testing ``has_2fa``
        """
        response = has_2fa(Mock())

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

        cl = Mock()

        self.assertEqual(cl.username(), 'unknown_user')

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

    def test_check_users(self):
        """
        Tests ``check_users``
        """

        content = check_users()

        self.assertTrue(content, True)

    def tearDown(self):
        self.auth.delete()
        self.my_admin.delete()
        self.my_admin_false.delete()


class UtilityTestsNoUser(TestCase):
    """
    Tests without user.
    """

    def setUp(self):
        try:
            User.objects.all().delete()
        except User.DoesNotExist:
            pass

    def test_check_users_false(self):
        """
        Tests ``check_users`` false.
        """

        content = check_users()
        self.assertFalse(content, False)


class Mock:
    """
    Mock object for username.
    """

    def username(self):
        return "unknown_user"

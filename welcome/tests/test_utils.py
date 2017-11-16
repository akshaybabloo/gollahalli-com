from django.contrib.auth.models import User
from django.test import TestCase, Client

from welcome.utils import check_users


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

    def test_check_users(self):
        """
        Tests ``check_users``
        """

        content = check_users()

        self.assertTrue(content, True)

    def tearDown(self):
        self.my_admin.delete()
        self.my_admin_false.delete()

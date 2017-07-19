from django import forms
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
import json

from authy_me.forms import AuthenticatorAdminForm, AuthyForm, LoginForm
from authy_me.models import AuthenticatorModel


class AuthenticatorAdminFormTests(TestCase):
    """
    Test case for ``authy_me/forms.py``
    """

    def setUp(self):
        password = 'mypassword'

        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

        c = Client()
        c.login(username=self.my_admin.username, password=password)

        self.auth = AuthenticatorModel.objects.create(id=1, user_id=self.my_admin, first_name='Akshay Raj',
                                                      last_name='Gollahalli', phone_number='+123456789',
                                                      email_id='example@example.com', authy_id='1234567')

    def test_authenticator_admin_form_post(self):
        """
        Testing ``AuthenticatorModel`` post.
        """
        form_data = {'id': 1, 'user_id': 'myuser', 'first_name': 'Akshay Raj', 'last_name': 'Gollahalli',
                     'phone_number': '+123456789',
                     'email_id': 'example@example.com', 'authy_id': '1234567'}

        c = Client()
        c.login(username='myuser', password='mypassword')

        change_url = reverse('admin:authy_me_authenticatormodel_add')
        response = c.post(change_url, form_data)
        self.assertTrue(response.status_code, 200)

    def test_authenticator_admin_form(self):
        """
        Testing ``AuthenticatorModel``.
        """
        form_data = {'id': 2, 'user_id': 1, 'first_name': 'Akshay Raj', 'last_name': 'Gollahalli',
                     'phone_number': '+64211111111',
                     'email_id': 'example@example.com', 'authy_id': '1234567', 'uuids': json.dumps({'test': 1})}

        form = AuthenticatorAdminForm(data=form_data)
        self.assertTrue(form.is_valid())

    def tearDown(self):
        self.auth.delete()
        self.my_admin.delete()


class AuthyFormTests(TestCase):
    """
    Test case for ``AuthyForm``
    """

    def test_authy_form(self):
        """
        Testing ``AuthyForm`` validation.
        """

        form_data = {'authy': 123456, 'is_personal': True}
        form = AuthyForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_authy_form_fail2(self):
        """
        Testing ``AuthyForm`` fail.
        """

        form_data = {'authy': "123eew#$$", 'is_personal': True}
        form = AuthyForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('The string should be all numbers.', str(form.errors))
        self.assertRaises(forms.ValidationError)


class LoginFormTests(TestCase):
    """
    Test case for ``LoginForm``
    """

    def setUp(self):
        password = 'mypassword'
        self.my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

        c = Client()
        c.login(username=self.my_admin.username, password=password)

    def test_login_form(self):
        """
        Testing ``login_form`` fail.
        """

        form_data = {'remember_me': True, 'username': 'myuser', 'password': 'mypassword'}

        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_fail(self):
        """
        Testing ``login_form`` fail.
        """

        form_data = {'remember_me': True}

        form = LoginForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('Sorry, that login was invalid. Please try again.', str(form.errors))
        self.assertRaises(forms.ValidationError)

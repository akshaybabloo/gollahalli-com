from django import forms


class WelcomeForm(forms.Form):
    """
    Welcome forms.
    """

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(widget=forms.EmailInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

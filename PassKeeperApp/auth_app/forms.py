from django import forms
from django.contrib.auth.forms import UserCreationForm
from PassKeeperApp.auth_app.models import AppUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')


from cryptography.fernet import Fernet
from django import forms
from django.conf import settings

from PassKeeperApp.my_credentials.models import MyCredentials


class VerificationForm(forms.Form):
    code = forms.CharField(widget=forms.PasswordInput(), label='Enter your code here')


class MyCredentialsCreateForm(forms.ModelForm):
    # Temporary password field to accept string password
    temp_password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    class Meta:
        model = MyCredentials
        fields = ('username', 'temp_password', 'comment', 'category')  # 'temp_password' instead of 'password'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("temp_password")

        # Encrypt the password here and save it in the actual 'password' field
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        ciphered_text = cipher_suite.encrypt(password.encode())
        cleaned_data['password'] = ciphered_text  # Store the encrypted password as binary
        return cleaned_data


class MyCredentialsEditForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = MyCredentials
        fields = ['username', 'new_password', 'comment', 'category']
from django import forms


class VerificationForm(forms.Form):
    code = forms.CharField(widget=forms.PasswordInput(), label='Enter your code here')
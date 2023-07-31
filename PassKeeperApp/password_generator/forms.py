from django import forms
from PassKeeperApp.password_generator.models import PasswordGenerator


class PasswordGeneratorForm(forms.ModelForm):
    class Meta:
        model = PasswordGenerator
        fields = ['length', 'use_uppercase', 'use_numbers', 'use_special']
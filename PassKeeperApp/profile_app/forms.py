from django import forms
from .models import Profile


# Custom form for editing the Profile model
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

    # Call the parent class's __init__ method to initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form field attributes if needed
        # For example, adding placeholder text to the first_name and last_name fields
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
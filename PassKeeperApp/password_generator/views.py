from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, redirect
from .forms import PasswordGeneratorForm
import string
import random

UserModel = get_user_model()


#  This view is for rendering a form where users can specify their preferences for generating a password,
#  and to handle the form submission to generate the password.
class PasswordGeneratorView(View):
    template_name = 'index.html'

    # Create an empty form instance
    def get(self, request, *args, **kwargs):
        form = PasswordGeneratorForm()
        # Render the form
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # Create a form instance with the data from the request
        form = PasswordGeneratorForm(request.POST)
        password = ''
        # If the form is valid, process the form data
        if form.is_valid():
            # If the form is valid, process the form data
            length = form.cleaned_data['length']
            use_uppercase = form.cleaned_data['use_uppercase']
            use_numbers = form.cleaned_data['use_numbers']
            use_special = form.cleaned_data['use_special']

            # Initialize the set of characters to be used for the password
            characters = string.ascii_lowercase
            # Add additional character sets based on the form data
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_numbers:
                characters += string.digits
            if use_special:
                characters += string.punctuation

            # Generate the password
            password = ''.join(random.choice(characters) for i in range(length))

            # If the user clicked the 'generate' button
            if 'generate' in request.POST:
                # Generate a password and render the form again with the generated password.
                # The save button is not clicked yet so we don't save the password generator settings.
                return render(request, self.template_name, {'form': form, 'password': password})

            # If the user clicked the 'save' button
            elif 'save' in request.POST:
                if request.user.is_authenticated:
                    # Saving the password generator settings for the user
                    password_generator = form.save(commit=False)
                    password_generator.user = self.request.user
                    password_generator.save()
                    # Save the password in the session and have the password filed display the generated password
                    request.session['generated_password'] = password
                    # Redirect to the 'credentials create' page
                    return redirect('create credentials')
                else:
                    # If the user is not authenticated, redirect to the login page
                    return redirect('login user')

        #TODO: make validations
        # If the form is not valid, we render the form again with the form errors.
        return render(request, self.template_name, {'form': form, 'password': password})
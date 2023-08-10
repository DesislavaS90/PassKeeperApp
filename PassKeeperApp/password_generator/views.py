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
        form = PasswordGeneratorForm(request.POST)
        # Try to get an existing generated password from the session
        password = request.session.get('generated_password', '')

        if form.is_valid():
            # If the user clicked the 'generate' button
            if 'generate' in request.POST:
                # Fetch the criteria from the form
                length = form.cleaned_data['length']
                use_uppercase = form.cleaned_data['use_uppercase']
                use_numbers = form.cleaned_data['use_numbers']
                use_special = form.cleaned_data['use_special']

                characters = string.ascii_lowercase
                if use_uppercase:
                    characters += string.ascii_uppercase
                if use_numbers:
                    characters += string.digits
                if use_special:
                    characters += string.punctuation

                # Generate a fresh password and update the session variable
                password = ''.join(random.choice(characters) for i in range(length))
                request.session['generated_password'] = password

            # If the user clicked the 'save' button
            elif 'save' in request.POST:
                if request.user.is_authenticated:
                    password_generator = form.save(commit=False)
                    password_generator.user = self.request.user
                    password_generator.save()

                    # Here, we don't generate a new password, we simply save the existing one from the session
                    return redirect('create credentials')
                else:
                    return redirect('login user')

        return render(request, self.template_name, {'form': form, 'password': password})

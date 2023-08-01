from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, redirect
from .forms import PasswordGeneratorForm
import string
import random

UserModel = get_user_model()


#  This view is for rendering a form where users can specify settings for generating a password,
#  and to handle the form submission to generate the password.
class PasswordGeneratorView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = PasswordGeneratorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordGeneratorForm(request.POST)
        password = ''
        if form.is_valid():
            length = form.cleaned_data['length']
            use_uppercase = form.cleaned_data['use_uppercase']
            use_numbers = form.cleaned_data['use_numbers']
            use_special = form.cleaned_data['use_special']

            # generate the password here
            characters = string.ascii_lowercase
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_numbers:
                characters += string.digits
            if use_special:
                characters += string.punctuation

            password = ''.join(random.choice(characters) for i in range(length))

            if 'generate' in request.POST:
                # Generate a password and render the form again with the generated password.
                # The save button is not clicked yet so we don't save the password generator settings.
                return render(request, self.template_name, {'form': form, 'password': password})

            elif 'save' in request.POST:
                if request.user.is_authenticated:
                    # Saving the password generator settings for the user
                    password_generator = form.save(commit=False)
                    password_generator.user = self.request.user
                    password_generator.save()
                    return redirect('credentials create')
                else:
                    return redirect('login user')

        # If the form is not valid, we render the form again with the form errors.
        return render(request, self.template_name, {'form': form, 'password': password})
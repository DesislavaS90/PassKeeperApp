
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from PassKeeperApp.auth_app.forms import RegistrationForm

UserModel = get_user_model()


# View for registering a new user
class RegisterUserView(views.CreateView):
    # Use the custom RegistrationForm to handle user registration
    form_class = RegistrationForm
    # Template for rendering the registration form
    template_name = 'login_register.html'

    # The method is overridden to log the user in after successful registration
    def form_valid(self, form):
        # Save the user form and get the user object
        user = form.save()
        # Perform the login for the new user
        login(self.request, user)
        # Return the HTTP response from the parent class (CreateView)
        return super().form_valid(form)

    # Method to get the URL to redirect after successful user registration
    def get_success_url(self):
        # Redirect to the profile details page with the updated profile's pk
        url = reverse('edit profile', kwargs={'pk': self.object.pk})
        return url


# View for user login using Django's built-in LoginView
class LoginUserView(auth_views.LoginView):
    # Template for rendering the login form
    template_name = 'login_register.html'


# View for user logout using Django's built-in LogoutView
class LogoutUserView(auth_views.LogoutView):
    # No additional logic needed, using the default behavior
    pass

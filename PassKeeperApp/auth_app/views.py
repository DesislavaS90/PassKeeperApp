from django.contrib import messages
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from PassKeeperApp.auth_app.forms import RegistrationForm

UserModel = get_user_model()


# View for registering a new user
class RegisterUserView(views.CreateView):
    # Use the custom RegistrationForm to handle user registration
    form_class = RegistrationForm
    # Template for the registration form
    template_name = 'login_register.html'

    # The method is overridden to log the user in after successful registration
    def form_valid(self, form):
        # Save the user form
        form.save()
        # Perform the login for the new user
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
        # Perform the login for the new user
        login(self.request, user)

        # The user will receive a short message, that he has an email confirmation
        messages.success(self.request, 'You have successfully registered! Please check your email.')
        # Get the URL to redirect after successful user registration to edit page so the user can add more info
        return HttpResponseRedirect(reverse('edit profile', kwargs={'pk': user.pk}))


# View for user login using Django's built-in LoginView
class LoginUserView(auth_views.LoginView):

    template_name = 'login_register.html'


# View for user logout using Django's built-in LogoutView
class LogoutUserView(auth_views.LogoutView):
    # No additional logic needed, using the default behavior
    pass

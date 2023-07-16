from django.shortcuts import render
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from PassKeeperApp.auth_app.forms import RegistrationForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    # TODO: success_ur to profile_edit details so i can make the user complete the registration details
    success_url = reverse_lazy('register user')


class LoginUserView(auth_views.LoginView):
    template_name = 'register.html'


class LogoutUserView(auth_views.LogoutView):
    pass

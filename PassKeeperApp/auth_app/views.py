
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from PassKeeperApp.auth_app.forms import RegistrationForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        # Perform the login
        login(self.request, user)

        return response

    def get_success_url(self):

        # Construct the URL with the desired 'pk' value
        url = reverse('edit profile', kwargs={'pk': self.object.pk})
        return url


class LoginUserView(auth_views.LoginView):
    template_name = 'register.html'




class LogoutUserView(auth_views.LogoutView):
    pass

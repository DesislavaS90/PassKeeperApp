from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from PassKeeperApp.auth_app.models import AppUser
from PassKeeperApp.my_credentials.forms import VerificationForm

UserModel = get_user_model()


class CodeVerificationView(LoginRequiredMixin, views.FormView):
    template_name = 'verify_code.html'  # use your actual template name here
    form_class = VerificationForm  # use your actual form here

    def form_valid(self, form):
        # Check if the hashed code entered by the user matches the user's stored code
        entered_code = form.cleaned_data.get('code')
        is_valid_code = check_password(entered_code, self.request.user.access_code)

        if is_valid_code:
            # The entered code matches the stored code.
            return redirect('credentials list')  # Redirects to the credentials page
        else:
            # The entered code does not match the stored code.
            form.add_error('code', 'The verification code is incorrect.')  # Show an error if the codes don't match
            return self.form_invalid(form)


class CredentialsCreateView(LoginRequiredMixin, views.CreateView):
    pass


class CredentialsListView(LoginRequiredMixin, views.ListView):
    pass


class CredentialsEditView(LoginRequiredMixin, views.UpdateView):
    pass


class CredentialsDeleteView(LoginRequiredMixin, views.DeleteView):
    pass


# Category VIEWS

class CategoryCreateView(LoginRequiredMixin, views.CreateView):
    pass


class CategoryListView(LoginRequiredMixin, views.ListView):
    pass


class CategoryEditView(LoginRequiredMixin, views.UpdateView):
    pass


class CategoryDeleteView(LoginRequiredMixin, views.DeleteView):
    pass
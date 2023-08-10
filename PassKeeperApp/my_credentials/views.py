from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from PassKeeperApp.my_credentials.forms import VerificationForm, MyCredentialsCreateForm, MyCredentialsEditForm, \
    MyCategoryCreateForm
from PassKeeperApp.my_credentials.models import MyCredentials, Category

UserModel = get_user_model()


class CodeVerificationView(LoginRequiredMixin, views.FormView):
    template_name = 'verify_code.html'
    form_class = VerificationForm

    def form_valid(self, form):
        entered_code = form.cleaned_data.get('code')
        is_valid_code = check_password(entered_code, self.request.user.access_code)

        if is_valid_code:
            self.request.session['code_verified'] = True
            return redirect('list credentials')
        else:
            form.add_error('code', 'The verification code is incorrect.')
            return self.form_invalid(form)


class CredentialsCreateView(LoginRequiredMixin, views.CreateView):
    model = MyCredentials
    form_class = MyCredentialsCreateForm
    template_name = 'credentials_create.html'

    def get_form_kwargs(self):
        kwargs = super(CredentialsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super().get_initial()
        # Get the generated password from the session (or None if it's not there)
        generated_password = self.request.session.get('generated_password', None)
        if generated_password is not None:
            # If a password was generated, add it to the initial form data

            initial['temp_password'] = generated_password
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.password = form.cleaned_data.get('password')  # Get encrypted password from cleaned data

        # Remove the password from the session
        if 'generated_password' in self.request.session:
            del self.request.session['generated_password']

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get the generated password from the session (or None if it's not there)
        generated_password = self.request.session.get('generated_password')
        # Add it to the context
        context['generated_password'] = generated_password
        return context

    def get_success_url(self):
        # Redirect to the newly created credential's detail view
        return reverse('list credentials')


class CredentialsListView(LoginRequiredMixin, views.ListView):
    model = MyCredentials
    template_name = 'credentials_list.html'  # Use the actual template name here
    context_object_name = 'credentials'  # The name of the context variable in your template

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add the list of categories to the context
        user_categories = Category.objects.filter(user=self.request.user)
        context['categories'] = user_categories

        return context

    def get_queryset(self):
        # Only return credentials belonging to the current user
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        # If a category ID was provided, filter by that category
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def dispatch(self, request, *args, **kwargs):
        credentials_exist = MyCredentials.objects.filter(user=request.user).exists()
        if credentials_exist and not request.session.get('code_verified', False):
            return redirect('verify code')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            return redirect('create credentials')
        return super().get(request, *args, **kwargs)


class CredentialsEditView(LoginRequiredMixin, views.UpdateView):
    model = MyCredentials
    form_class = MyCredentialsEditForm
    template_name = 'credentials_edit.html'
    context_object_name = 'credential'  # The name of the context variable in the template

    def get_form_kwargs(self):
        kwargs = super(CredentialsEditView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.temp_password = obj.decrypt_password
        return obj

    def form_valid(self, form):
        password = form.cleaned_data.get('new_password')
        if password:  # only encrypt if a new password has been entered
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            ciphered_text = cipher_suite.encrypt(password.encode())
            form.instance.password = ciphered_text
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list credentials')


class CredentialsDeleteView(LoginRequiredMixin, views.DeleteView):
    model = MyCredentials
    template_name = 'credentials_delete.html'
    success_url = reverse_lazy('list credentials')  # This is the URL to redirect to after a successful delete

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)  # Only allow deleting credentials belonging to the current user


# Category VIEWS

class CategoryCreateView(LoginRequiredMixin, views.CreateView):
    model = Category
    form_class = MyCategoryCreateForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('list categories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryListView(LoginRequiredMixin, views.ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        # Check if there are any categories for this user
        if not self.get_queryset().exists():
            # If not, redirect to the "create category" view
            return redirect('create category')
        return super().get(request, *args, **kwargs)


class CategoryEditView(LoginRequiredMixin, views.UpdateView):
    model = Category
    template_name = 'category_edit.html'
    success_url = reverse_lazy('list categories')
    fields = ('name', 'comment')


class CategoryDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('list credentials')  # This is the URL to redirect to after a successful delete

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


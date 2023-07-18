from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from PassKeeperApp.profile_app.forms import ProfileForm
from PassKeeperApp.profile_app.models import Profile

UserModel = get_user_model()


class DetailsProfileView(LoginRequiredMixin, views.DetailView):
    template_name = 'details.html'
    model = Profile

    def get_object(self, queryset=None):
        # Return the profile of the logged-in user
        return self.request.user


class EditProfileView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('edit profile')

    def get_object(self, queryset=None):
        # Return the profile of the logged-in user
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        # Save the updated profile instance
        profile = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the profile details page with the updated object's pk
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    model = UserModel
    success_url = reverse_lazy('login user')

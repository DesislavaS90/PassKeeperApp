from django.urls import path

from PassKeeperApp.profile_app.views import DetailsProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('<int:pk>/details', DetailsProfileView.as_view(), name='details profile'),
    path('<int:pk>/edit', EditProfileView.as_view(), name='edit profile'),
    path('<int:pk>/delete', DeleteProfileView.as_view(), name='delete profile'),
]
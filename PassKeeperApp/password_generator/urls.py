from django.urls import path
from PassKeeperApp.password_generator.views import PasswordGeneratorView

urlpatterns = [
    path('create_password/', PasswordGeneratorView.as_view(), name='password generator'),

]
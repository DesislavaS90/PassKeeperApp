from django.urls import path
from PassKeeperApp.my_passwords_app.views import PasswordGeneratorView

urlpatterns = [
    path('create_password/', PasswordGeneratorView.as_view(), name='password'),

]
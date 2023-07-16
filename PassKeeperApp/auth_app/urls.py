from django.urls import path

from PassKeeperApp.auth_app.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),

]

from .signals import *

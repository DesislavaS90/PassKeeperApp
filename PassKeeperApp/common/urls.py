from django.urls import path
from PassKeeperApp.common import views

urlpatterns = [
    path('', views.index, name='index'),
]
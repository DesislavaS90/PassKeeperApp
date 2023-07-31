from django.contrib.auth import get_user_model
from django.db import models
from PassKeeperApp.auth_app.models import AppUser

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )


class MyCredentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    comment = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

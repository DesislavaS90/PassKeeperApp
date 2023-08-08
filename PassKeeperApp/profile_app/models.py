from django.db import models
from PassKeeperApp.auth_app.models import AppUser


class Profile(models.Model):
    # Field to store user's first name, can be null and not required
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    # Field to store user's last name, can be null and not required
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    # One-to-one relationship between User and Profile models.
    # If the Profile is deleted, the User will be deleted as well (models.CASCADE)
    user = models.OneToOneField(
        AppUser, on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )



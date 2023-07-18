from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Profile(models.Model):

    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )



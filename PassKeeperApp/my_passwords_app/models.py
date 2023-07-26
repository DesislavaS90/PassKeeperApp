from django.db import models
from PassKeeperApp.auth_app.models import AppUser


# The model have fields representing different parameters of the password generation, such as length, whether
# to include uppercase letters, numbers, special characters and store the user's password generation preferences.
# Including the user field in the PasswordGenerator model allows you to keep track of which user created each
# PasswordGenerator instance. For example, if a user has specific preferences for how passwords should be generated
# (like the password length, whether to use uppercase letters, numbers, or special characters),
# you can save these preferences in a PasswordGenerator instance associated with that user.
# This can be useful for improving the user experience by remembering the user's preferences.
class PasswordGenerator(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    length = models.PositiveIntegerField()
    use_uppercase = models.BooleanField(default=False)
    use_numbers = models.BooleanField(default=False)
    use_special = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
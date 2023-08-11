from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from PassKeeperApp.auth_app.models import AppUser

# Retrieves the user model currently active in the project
UserModel = get_user_model()


# This model allows you to keep track of which user created each password.
# This can be useful for improving the user experience by remembering the user's preferences.
class PasswordGenerator(models.Model):
    # This line creates a foreign key relationship between PasswordGenerator and AppUser.
    # Each password generator is associated with a user. on_delete=models.CASCADE means that when the associated user
    # is deleted, all PasswordGenerator instances associated with that user are also deleted.
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    length = models.PositiveIntegerField(validators=[MinValueValidator(8, 'Make sure your password is at least 8 characters long!')])
    use_uppercase = models.BooleanField(default=False)
    use_numbers = models.BooleanField(default=False)
    use_special = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.length}"
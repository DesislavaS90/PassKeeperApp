from django.db import models
from django.contrib.auth import models as auth_models


# Custom manager for AppUser model to manage user creation
class AppUserManager(auth_models.BaseUserManager):
    # Method to create a user with the given username, email, and password
    def _create_user(self, username, email, password=None, **extra_fields):
        # Check if username and email are provided, raise ValueError if not
        if not username:
            raise ValueError('The Username field must be set.')
        if not email:
            raise ValueError('The Email field must be set.')

        # Normalize the email (convert to lowercase)
        email = self.normalize_email(email)
        # Create a new AppUser instance with the given attributes
        user = self.model(username=username, email=email, **extra_fields)
        # Set the user's password
        user.set_password(password)
        # Save the user to the database using the default database
        user.save(using=self._db)
        # Return the newly created user
        return user

    # Method to create a regular user (not staff or superuser)
    def create_user(self, username, email, password=None, **extra_fields):
        # Set 'is_staff' and 'is_superuser' to False for regular users
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # Call _create_user method to create and save the user
        return self._create_user(username, email, password, **extra_fields)

    # Method to create a superuser with staff and superuser permissions
    def create_superuser(self, username, email, password=None, **extra_fields):
        # Set 'is_staff' and 'is_superuser' to True for superusers
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # Call _create_user method to create and save the superuser
        return self._create_user(username, email, password, **extra_fields)


# Custom AppUser model that inherits from AbstractBaseUser and PermissionsMixin
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # Fields for the user model
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Optional field for access code
    access_code = models.CharField(max_length=128, blank=True, null=True)

    # Associate the custom AppUserManager with the objects attribute
    objects = AppUserManager()

    # Set the 'username' field as the USERNAME_FIELD for authentication
    USERNAME_FIELD = 'username'
    # Set the 'email' field as the EMAIL_FIELD for authentication
    EMAIL_FIELD = 'email'


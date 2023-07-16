from django.db import models
from django.contrib.auth import models as auth_models


class AppUserManager(auth_models.BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set.')
        if not email:
            raise ValueError('The Email field must be set.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    access_code = models.CharField(max_length=128, blank=True, null=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'


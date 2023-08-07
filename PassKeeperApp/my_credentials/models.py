from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from cryptography.fernet import Fernet
from PassKeeperApp.auth_app.models import AppUser
from django.conf import settings


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
    password = models.BinaryField()  # store encrypted password as binary
    comment = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    slug = models.SlugField(unique=True, null=False, default='', blank=True, max_length=255, editable=False)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def encrypt_password(self):
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        ciphered_text = cipher_suite.encrypt(self.password.encode())  # Required to be bytes
        return ciphered_text

    @property
    def decrypt_password(self):
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        unciphered_text = (cipher_suite.decrypt(bytes(self.password))).decode("utf-8")  # Decode bytes to string
        return unciphered_text

    def save(self, *args, **kwargs):
        # Generate slug if it's not set
        if not self.slug:
            self.slug = slugify(self.username)
        # Encrypt password before saving
        # self.password = self.encrypt_password()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


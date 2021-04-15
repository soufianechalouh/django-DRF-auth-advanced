from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models


class UserManager(BaseUserManager):
    """Custom user manager"""

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError("User should have Username")

        if email is None:
            raise TypeError("User should have email")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError("User should have Password")


        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

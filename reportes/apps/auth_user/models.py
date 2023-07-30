from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers.userManagers import UserManagers


class User(AbstractUser, PermissionsMixin):
    profile = models.FileField(upload_to="users/profile")
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects_create = UserManagers()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        # db_table_comment = "User Default Model"
        default_related_name = "User"

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"

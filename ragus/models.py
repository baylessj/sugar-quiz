"""Defines the database models used by the Ragus app."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Defines a User that can access the apartment building."""

    doors = models.ManyToManyField(to="Door", related_name="users", blank=True)

    class Meta:
        """Defines metadata associated with User."""

        db_table = "auth_user"


class Door(models.Model):
    """Defines a door that can be used by a User."""

    name = models.CharField(max_length=32, null=False)
    acme_device_id = models.CharField(max_length=8, null=False)

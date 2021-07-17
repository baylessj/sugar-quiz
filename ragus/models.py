from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   doors = models.ManyToManyField(to='Door', related_name='users', blank=True)

   class Meta:
      db_table = "auth_user"

class Door(models.Model):
   name = models.CharField(max_length=32, null=False)
   acme_device_id = models.CharField(max_length=8, null=False)

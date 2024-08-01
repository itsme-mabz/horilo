from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CookieData(models.Model):
    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Data {self.id} at {self.created_at}"

class User(AbstractUser):
  groups = models.ManyToManyField(Group,
                                  related_name='custom_user_set',
                                  blank=True,
                                  help_text='The groups this user belongs to.',
                                  verbose_name='groups')
  user_permissions = models.ManyToManyField(
      Permission,
      related_name='custom_user_set',
      blank=True,
      help_text='Specific permissions for this user.',
      verbose_name='user permissions')

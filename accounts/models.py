# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import pytz

class CookieData(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Data {self.id} at {self.created_at}"

class User(AbstractUser):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        # Add more languages as needed
    ]

    company_name = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='en')
    newsletter_opt_in = models.BooleanField(default=True)

    # Address fields
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    # Global activity timeframe
    timezone = models.CharField(max_length=100, choices=[(tz, tz) for tz in pytz.all_timezones], default='UTC')
    activity_timeframe = models.JSONField(default=dict)
    # 2FA fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_2fa_enabled = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
        
    def __str__(self):
        return self.username

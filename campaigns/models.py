from django.db import models
from django.conf import settings

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('archived', 'Archived'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('mid', 'Mid'),
        ('low', 'Low'),
    ]

    name = models.CharField(max_length=255, null=True)
    campaign_type = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    kpis = models.JSONField(null=True) 
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True) 
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='campaigns', null=True)
    
    def __str__(self):
        return self.name

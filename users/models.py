from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLE_CHOICES = (
        ('USER', 'User'),
        ('FINANCE_MANAGER', 'Finance Manager'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USER')
    phone = models.CharField(max_length=20, blank=True, null=True)
    financial_preferences = models.JSONField(default=dict, blank=True)
    monthly_budget_preference = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    currency_preference = models.CharField(max_length=3, default='USD')
    notification_preference = models.BooleanField(default=True)

    def __str__(self):
        return self.username

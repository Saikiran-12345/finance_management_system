from django.db import models
from django.conf import settings
from accounts.models import Account

class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
        
class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incomes')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='incomes')
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"

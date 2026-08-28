from django.db import models
from django.conf import settings
from expenses.models import ExpenseCategory

class Budget(models.Model):
    STATUS_CHOICES = (
        ('SAFE', 'Safe'),
        ('WARNING', 'Warning'),
        ('EXCEEDED', 'Exceeded'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, null=True, blank=True)
    month = models.DateField(help_text='First day of the month for this budget')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SAFE')
    
    @property
    def remaining_amount(self):
        return self.amount - self.amount_spent
        
    @property
    def percentage_used(self):
        if self.amount > 0:
            return (self.amount_spent / self.amount) * 100
        return 0

    def __str__(self):
        return f"Budget: {self.amount} for {self.month}"

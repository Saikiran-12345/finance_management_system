import os

MODELS = {
    "users": """from django.db import models
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
""",
    "accounts": """from django.db import models
from django.conf import settings

class Account(models.models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings Account'),
        ('CURRENT', 'Current Account'),
        ('CASH', 'Cash Account'),
        ('INVESTMENT', 'Investment Account'),
        ('OTHER', 'Other Account'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='CASH')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()}) - {self.user.username}"
""",
    "income": """from django.db import models
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
""",
    "expenses": """from django.db import models
from django.conf import settings
from accounts.models import Account

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=50)
    is_recurring = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name if self.category else 'Misc'} - {self.amount}"
""",
    "transactions": """from django.db import models
from django.conf import settings
from accounts.models import Account

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
        ('TRANSFER', 'Transfer'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions_as_primary')
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='transactions_as_destination')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    category_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.date}"
""",
    "budgets": """from django.db import models
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
""",
    "savings": """from django.db import models
from django.conf import settings

class SavingsGoal(models.Model):
    STATUS_CHOICES = (
        ('ON_TRACK', 'On Track'),
        ('BEHIND', 'Behind'),
        ('ACHIEVED', 'Achieved'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='savings_goals')
    name = models.CharField(max_length=150)
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)
    current_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    target_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ON_TRACK')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def remaining_amount(self):
        return self.target_amount - self.current_amount

    @property
    def progress_percentage(self):
        if self.target_amount > 0:
            return (self.current_amount / self.target_amount) * 100
        return 0

    def __str__(self):
        return f"Goal: {self.name} - {self.target_amount}"
""",
    "notifications": """from django.db import models
from django.conf import settings

class Notification(models.Model):
    TYPE_CHOICES = (
        ('BUDGET_WARNING', 'Budget Warning'),
        ('BUDGET_EXCEEDED', 'Budget Exceeded'),
        ('SAVINGS_PROGRESS', 'Savings Goal Progress'),
        ('LARGE_EXPENSE', 'Large Expense Warning'),
        ('RECURRING_REMINDER', 'Recurring Transaction Reminder'),
        ('SYSTEM', 'System Notification'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} for {self.user.username}"
""",
    "audit": """from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    action = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.user} in {self.module} at {self.timestamp}"
"""
}

def write_models():
    for app, content in MODELS.items():
        with open(os.path.join(app, "models.py"), "w") as f:
            f.write(content)

if __name__ == "__main__":
    write_models()
    print("Models generated.")

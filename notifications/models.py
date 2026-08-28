from django.db import models
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

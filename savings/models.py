from django.db import models
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

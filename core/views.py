from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Account
from transactions.models import Transaction
from budgets.models import Budget
from django.db.models import Sum
from django.utils import timezone

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Total Balance
        accounts = Account.objects.filter(user=user)
        total_balance = accounts.aggregate(Sum('balance'))['balance__sum'] or 0
        
        # Recent Transactions
        recent_transactions = Transaction.objects.filter(user=user).order_by('-date', '-created_at')[:10]
        
        # Current month calculations
        now = timezone.now()
        current_month = now.replace(day=1)
        
        income_this_month = Transaction.objects.filter(
            user=user, 
            transaction_type='INCOME',
            date__gte=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        expense_this_month = Transaction.objects.filter(
            user=user, 
            transaction_type='EXPENSE',
            date__gte=current_month
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        context['total_balance'] = total_balance
        context['recent_transactions'] = recent_transactions
        context['income_this_month'] = income_this_month
        context['expense_this_month'] = expense_this_month
        context['savings_this_month'] = income_this_month - expense_this_month
        
        return context

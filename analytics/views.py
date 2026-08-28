from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from budgets.models import Budget
from savings.models import SavingsGoal
from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta

class AnalyticsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # We process lots of data for the charts
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=365)
        
        transactions = Transaction.objects.filter(user=user, date__gte=start_date, date__lte=end_date)
        
        # 1. Monthly Income vs Expense
        monthly_stats = {}
        for t in transactions:
            month_key = t.date.strftime('%Y-%m')
            if month_key not in monthly_stats:
                monthly_stats[month_key] = {'income': 0, 'expense': 0}
            if t.transaction_type == 'INCOME':
                monthly_stats[month_key]['income'] += float(t.amount)
            elif t.transaction_type == 'EXPENSE':
                monthly_stats[month_key]['expense'] += float(t.amount)
                
        context['monthly_stats'] = monthly_stats
        
        # 2. Expense by Category
        expenses = transactions.filter(transaction_type='EXPENSE')
        cat_stats = expenses.values('category_name').annotate(total=Sum('amount')).order_by('-total')
        context['category_stats'] = list(cat_stats)
        
        # 3. Income by Source
        incomes = transactions.filter(transaction_type='INCOME')
        income_source_stats = incomes.values('category_name').annotate(total=Sum('amount')).order_by('-total')
        context['income_source_stats'] = list(income_source_stats)
        
        # Add more context variables...
        context['page_title'] = 'Advanced Analytics'
        
        return context

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from transactions.models import Transaction
from accounts.models import Account
from django.utils import timezone
import csv

class ReportsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/dashboard.html'
    
class TransactionCSVExportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="transactions_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'Date', 'Type', 'Account', 'Category', 'Amount', 'Description'])
        
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        
        for t in transactions:
            writer.writerow([
                t.id,
                t.date.strftime('%Y-%m-%d'),
                t.transaction_type,
                t.account.name if t.account else 'N/A',
                t.category_name,
                t.amount,
                t.description
            ])
            
        return response
        
class AccountBalanceCSVExportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="account_balances.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'Account Name', 'Type', 'Current Balance'])
        
        accounts = Account.objects.filter(user=request.user)
        
        for a in accounts:
            writer.writerow([
                a.id,
                a.name,
                a.get_account_type_display(),
                a.balance
            ])
            
        return response

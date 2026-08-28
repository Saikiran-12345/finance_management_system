import os

def write_reports():
    os.makedirs("reports/templates/reports", exist_ok=True)
    
    views_code = """from django.views.generic import TemplateView, View
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
"""
    with open("reports/views.py", "w") as f:
        f.write(views_code)
        
    urls_code = """from django.urls import path
from .views import ReportsDashboardView, TransactionCSVExportView, AccountBalanceCSVExportView

urlpatterns = [
    path('', ReportsDashboardView.as_view(), name='reports'),
    path('export/transactions/', TransactionCSVExportView.as_view(), name='export-transactions'),
    path('export/accounts/', AccountBalanceCSVExportView.as_view(), name='export-accounts'),
]
"""
    with open("reports/urls.py", "w") as f:
        f.write(urls_code)

    html = """{% extends 'base.html' %}
{% block title %}Financial Reports{% endblock %}
{% block content %}
<div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Financial Reports & Exports</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
            <h3 class="text-xl font-bold text-gray-700 mb-2">Transactions Report</h3>
            <p class="text-gray-600 mb-4">Export all your historical transactions as a CSV file for import into Excel or other accounting software.</p>
            <a href="{% url 'export-transactions' %}" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded inline-block">
                Download CSV
            </a>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
            <h3 class="text-xl font-bold text-gray-700 mb-2">Account Balances</h3>
            <p class="text-gray-600 mb-4">Export a snapshot of all your current account balances.</p>
            <a href="{% url 'export-accounts' %}" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded inline-block">
                Download CSV
            </a>
        </div>
    </div>
</div>
{% endblock %}
"""
    with open("reports/templates/reports/dashboard.html", "w") as f:
        f.write(html)
        
    # Update main urls
    with open("config/urls.py", "r") as f:
        urls = f.read()
    if "'reports.urls'" not in urls:
        urls = urls.replace(
            "path('analytics/', include('analytics.urls')),",
            "path('analytics/', include('analytics.urls')),\n    path('reports/', include('reports.urls')),"
        )
        with open("config/urls.py", "w") as f:
            f.write(urls)

if __name__ == "__main__":
    write_reports()
    print("Reports generated.")

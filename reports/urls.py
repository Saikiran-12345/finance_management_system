from django.urls import path
from .views import ReportsDashboardView, TransactionCSVExportView, AccountBalanceCSVExportView

urlpatterns = [
    path('', ReportsDashboardView.as_view(), name='reports'),
    path('export/transactions/', TransactionCSVExportView.as_view(), name='export-transactions'),
    path('export/accounts/', AccountBalanceCSVExportView.as_view(), name='export-accounts'),
]

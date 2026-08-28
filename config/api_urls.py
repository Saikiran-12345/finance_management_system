from django.urls import path, include

urlpatterns = [
    path('users/', include('users.api_urls')),
    path('accounts/', include('accounts.api_urls')),
    path('income/', include('income.api_urls')),
    path('expenses/', include('expenses.api_urls')),
    path('transactions/', include('transactions.api_urls')),
    path('budgets/', include('budgets.api_urls')),
    path('savings/', include('savings.api_urls')),
    path('notifications/', include('notifications.api_urls')),
    path('audit/', include('audit.api_urls')),
]

from django.contrib import admin
from django.urls import path, include
from core.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('users/', include('users.urls')),
    path('accounts-app/', include('accounts.urls')),
    path('income/', include('income.urls')),
    path('expenses/', include('expenses.urls')),
    path('transactions/', include('transactions.urls')),
    path('budgets/', include('budgets.urls')),
    path('savings/', include('savings.urls')),
    path('analytics/', include('analytics.urls')),
    path('reports/', include('reports.urls')),
    path('ml/', include('ml.urls')),
]

urlpatterns += [path('api/v1/', include('config.api_urls'))]

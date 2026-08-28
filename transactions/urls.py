from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='transaction-list'),
    path('new/', views.TransactionCreateView.as_view(), name='transaction-create'),
    path('<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('<int:pk>/update/', views.TransactionUpdateView.as_view(), name='transaction-update'),
    path('<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),
]

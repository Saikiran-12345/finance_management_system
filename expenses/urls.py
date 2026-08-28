from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expense-list'),
    path('new/', views.ExpenseCreateView.as_view(), name='expense-create'),
    path('<int:pk>/', views.ExpenseDetailView.as_view(), name='expense-detail'),
    path('<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense-delete'),
]

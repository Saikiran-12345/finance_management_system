from django.urls import path
from . import views

app_name = 'income'

urlpatterns = [
    path('', views.IncomeListView.as_view(), name='income-list'),
    path('new/', views.IncomeCreateView.as_view(), name='income-create'),
    path('<int:pk>/', views.IncomeDetailView.as_view(), name='income-detail'),
    path('<int:pk>/update/', views.IncomeUpdateView.as_view(), name='income-update'),
    path('<int:pk>/delete/', views.IncomeDeleteView.as_view(), name='income-delete'),
]

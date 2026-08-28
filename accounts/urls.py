from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountListView.as_view(), name='account-list'),
    path('new/', views.AccountCreateView.as_view(), name='account-create'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='account-detail'),
    path('<int:pk>/update/', views.AccountUpdateView.as_view(), name='account-update'),
    path('<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account-delete'),
]

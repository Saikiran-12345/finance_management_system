from django.urls import path
from . import views

app_name = 'savings'

urlpatterns = [
    path('', views.SavingsGoalListView.as_view(), name='savingsgoal-list'),
    path('new/', views.SavingsGoalCreateView.as_view(), name='savingsgoal-create'),
    path('<int:pk>/', views.SavingsGoalDetailView.as_view(), name='savingsgoal-detail'),
    path('<int:pk>/update/', views.SavingsGoalUpdateView.as_view(), name='savingsgoal-update'),
    path('<int:pk>/delete/', views.SavingsGoalDeleteView.as_view(), name='savingsgoal-delete'),
]

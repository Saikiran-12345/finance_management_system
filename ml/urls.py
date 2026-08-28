from django.urls import path
from .views import MLInsightsView

urlpatterns = [
    path('', MLInsightsView.as_view(), name='ml_insights'),
]

from rest_framework.routers import DefaultRouter
from .api_views import SavingsGoalViewSet

router = DefaultRouter()
router.register(r'savingsgoals', SavingsGoalViewSet, basename='savingsgoal')

urlpatterns = router.urls

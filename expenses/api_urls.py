from rest_framework.routers import DefaultRouter
from .api_views import ExpenseCategoryViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'expensecategorys', ExpenseCategoryViewSet, basename='expensecategory')
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = router.urls

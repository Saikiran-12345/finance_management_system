from rest_framework.routers import DefaultRouter
from .api_views import IncomeCategoryViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'incomecategorys', IncomeCategoryViewSet, basename='incomecategory')
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = router.urls

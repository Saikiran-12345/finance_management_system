from rest_framework.routers import DefaultRouter
from .api_views import AuditLogViewSet

router = DefaultRouter()
router.register(r'auditlogs', AuditLogViewSet, basename='auditlog')

urlpatterns = router.urls

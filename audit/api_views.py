from rest_framework import viewsets, permissions
from .models import AuditLog
from .serializers import AuditLogSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return AuditLog.objects.all()
        # Assume user field exists for most models
        if hasattr(AuditLog, 'user'):
            return AuditLog.objects.filter(user=self.request.user)
        return AuditLog.objects.all()

    def perform_create(self, serializer):
        if hasattr(AuditLog, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


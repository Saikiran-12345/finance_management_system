from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Notification.objects.all()
        # Assume user field exists for most models
        if hasattr(Notification, 'user'):
            return Notification.objects.filter(user=self.request.user)
        return Notification.objects.all()

    def perform_create(self, serializer):
        if hasattr(Notification, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


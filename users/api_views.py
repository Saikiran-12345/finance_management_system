from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return User.objects.all()
        # Assume user field exists for most models
        if hasattr(User, 'user'):
            return User.objects.filter(user=self.request.user)
        return User.objects.all()

    def perform_create(self, serializer):
        if hasattr(User, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


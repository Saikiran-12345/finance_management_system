from rest_framework import viewsets, permissions
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Account.objects.all()
        # Assume user field exists for most models
        if hasattr(Account, 'user'):
            return Account.objects.filter(user=self.request.user)
        return Account.objects.all()

    def perform_create(self, serializer):
        if hasattr(Account, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


from rest_framework import viewsets, permissions
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Transaction.objects.all()
        # Assume user field exists for most models
        if hasattr(Transaction, 'user'):
            return Transaction.objects.filter(user=self.request.user)
        return Transaction.objects.all()

    def perform_create(self, serializer):
        if hasattr(Transaction, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


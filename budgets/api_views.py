from rest_framework import viewsets, permissions
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Budget.objects.all()
        # Assume user field exists for most models
        if hasattr(Budget, 'user'):
            return Budget.objects.filter(user=self.request.user)
        return Budget.objects.all()

    def perform_create(self, serializer):
        if hasattr(Budget, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


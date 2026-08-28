from rest_framework import viewsets, permissions
from .models import IncomeCategory, Income
from .serializers import IncomeCategorySerializer, IncomeSerializer

class IncomeCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return IncomeCategory.objects.all()
        # Assume user field exists for most models
        if hasattr(IncomeCategory, 'user'):
            return IncomeCategory.objects.filter(user=self.request.user)
        return IncomeCategory.objects.all()

    def perform_create(self, serializer):
        if hasattr(IncomeCategory, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Income.objects.all()
        # Assume user field exists for most models
        if hasattr(Income, 'user'):
            return Income.objects.filter(user=self.request.user)
        return Income.objects.all()

    def perform_create(self, serializer):
        if hasattr(Income, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


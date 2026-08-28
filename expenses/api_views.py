from rest_framework import viewsets, permissions
from .models import ExpenseCategory, Expense
from .serializers import ExpenseCategorySerializer, ExpenseSerializer

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return ExpenseCategory.objects.all()
        # Assume user field exists for most models
        if hasattr(ExpenseCategory, 'user'):
            return ExpenseCategory.objects.filter(user=self.request.user)
        return ExpenseCategory.objects.all()

    def perform_create(self, serializer):
        if hasattr(ExpenseCategory, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return Expense.objects.all()
        # Assume user field exists for most models
        if hasattr(Expense, 'user'):
            return Expense.objects.filter(user=self.request.user)
        return Expense.objects.all()

    def perform_create(self, serializer):
        if hasattr(Expense, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


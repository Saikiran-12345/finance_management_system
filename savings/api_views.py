from rest_framework import viewsets, permissions
from .models import SavingsGoal
from .serializers import SavingsGoalSerializer

class SavingsGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return SavingsGoal.objects.all()
        # Assume user field exists for most models
        if hasattr(SavingsGoal, 'user'):
            return SavingsGoal.objects.filter(user=self.request.user)
        return SavingsGoal.objects.all()

    def perform_create(self, serializer):
        if hasattr(SavingsGoal, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


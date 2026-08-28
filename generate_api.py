import os

APPS_MODELS = {
    'users': ['User'],
    'accounts': ['Account'],
    'income': ['IncomeCategory', 'Income'],
    'expenses': ['ExpenseCategory', 'Expense'],
    'transactions': ['Transaction'],
    'budgets': ['Budget'],
    'savings': ['SavingsGoal'],
    'notifications': ['Notification'],
    'audit': ['AuditLog'],
}

def write_api_code():
    for app, models in APPS_MODELS.items():
        # 1. Serializers
        serializers_code = f"from rest_framework import serializers\n"
        serializers_code += f"from .models import {', '.join(models)}\n\n"
        for model in models:
            serializers_code += f"""class {model}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model}
        fields = '__all__'

"""
        with open(os.path.join(app, "serializers.py"), "w") as f:
            f.write(serializers_code)

        # 2. ViewSets
        api_views_code = f"from rest_framework import viewsets, permissions\n"
        api_views_code += f"from .models import {', '.join(models)}\n"
        api_views_code += f"from .serializers import {', '.join([m + 'Serializer' for m in models])}\n\n"
        for model in models:
            api_views_code += f"""class {model}ViewSet(viewsets.ModelViewSet):
    serializer_class = {model}Serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'ADMIN':
            return {model}.objects.all()
        # Assume user field exists for most models
        if hasattr({model}, 'user'):
            return {model}.objects.filter(user=self.request.user)
        return {model}.objects.all()

    def perform_create(self, serializer):
        if hasattr({model}, 'user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()

"""
        with open(os.path.join(app, "api_views.py"), "w") as f:
            f.write(api_views_code)
            
        # 3. API URLs
        api_urls_code = f"from rest_framework.routers import DefaultRouter\n"
        api_urls_code += f"from .api_views import {', '.join([m + 'ViewSet' for m in models])}\n\n"
        api_urls_code += f"router = DefaultRouter()\n"
        for model in models:
            api_urls_code += f"router.register(r'{model.lower()}s', {model}ViewSet, basename='{model.lower()}')\n"
        api_urls_code += f"\nurlpatterns = router.urls\n"
        
        with open(os.path.join(app, "api_urls.py"), "w") as f:
            f.write(api_urls_code)

    # 4. Master API URLs
    master_urls = "from django.urls import path, include\n\nurlpatterns = [\n"
    for app in APPS_MODELS.keys():
        master_urls += f"    path('{app}/', include('{app}.api_urls')),\n"
    master_urls += "]\n"
    
    with open("config/api_urls.py", "w") as f:
        f.write(master_urls)
        
    # 5. Update main urls.py to include API
    with open("config/urls.py", "a") as f:
        f.write("\nurlpatterns += [path('api/v1/', include('config.api_urls'))]\n")

if __name__ == "__main__":
    write_api_code()
    print("REST APIs generated.")

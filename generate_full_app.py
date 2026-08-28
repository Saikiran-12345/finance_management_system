import os

def generate_views(app_name, model_name):
    return f'''from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import {model_name}
from .forms import {model_name}Form
import logging

logger = logging.getLogger(__name__)

class {model_name}ListView(LoginRequiredMixin, ListView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_list.html'
    context_object_name = '{model_name.lower()}s'
    paginate_by = 10

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        logger.info(f"Fetching {model_name} list for user {{self.request.user}}")
        qs = super().get_queryset().filter(user=self.request.user)
        # Apply filtering here if necessary
        return qs.order_by('-id')

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = '{model_name}s'
        context['total_count'] = self.get_queryset().count()
        return context


class {model_name}DetailView(LoginRequiredMixin, DetailView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_detail.html'
    context_object_name = '{model_name.lower()}'

    def get_queryset(self):
        """
        Ensure users can only view their own records.
        """
        return super().get_queryset().filter(user=self.request.user)


class {model_name}CreateView(LoginRequiredMixin, CreateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = reverse_lazy('{app_name}:{model_name.lower()}-list')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.instance.user = self.request.user
        messages.success(self.request, "{model_name} created successfully.")
        logger.info(f"{model_name} created by user {{self.request.user}}")
        return super().form_valid(form)
        
    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(self.request, "Please correct the errors below.")
        logger.warning(f"Failed to create {model_name} by user {{self.request.user}}")
        return super().form_invalid(form)


class {model_name}UpdateView(LoginRequiredMixin, UpdateView):
    model = {model_name}
    form_class = {model_name}Form
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = reverse_lazy('{app_name}:{model_name.lower()}-list')

    def get_queryset(self):
        """
        Ensure users can only update their own records.
        """
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        messages.success(self.request, "{model_name} updated successfully.")
        logger.info(f"{model_name} updated by user {{self.request.user}}")
        return super().form_valid(form)


class {model_name}DeleteView(LoginRequiredMixin, DeleteView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_confirm_delete.html'
    success_url = reverse_lazy('{app_name}:{model_name.lower()}-list')

    def get_queryset(self):
        """
        Ensure users can only delete their own records.
        """
        return super().get_queryset().filter(user=self.request.user)
        
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        messages.success(self.request, "{model_name} deleted successfully.")
        logger.info(f"{model_name} deleted by user {{self.request.user}}")
        return super().delete(request, *args, **kwargs)
'''

def generate_urls(app_name, model_name):
    return f'''from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.{model_name}ListView.as_view(), name='{model_name.lower()}-list'),
    path('new/', views.{model_name}CreateView.as_view(), name='{model_name.lower()}-create'),
    path('<int:pk>/', views.{model_name}DetailView.as_view(), name='{model_name.lower()}-detail'),
    path('<int:pk>/update/', views.{model_name}UpdateView.as_view(), name='{model_name.lower()}-update'),
    path('<int:pk>/delete/', views.{model_name}DeleteView.as_view(), name='{model_name.lower()}-delete'),
]
'''

def generate_forms(app_name, model_name):
    return f'''from django import forms
from .models import {model_name}

class {model_name}Form(forms.ModelForm):
    class Meta:
        model = {model_name}
        exclude = ('user', 'created_at', 'updated_at')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'
'''

def generate_templates(app_name, model_name):
    templates = {}
    
    # Base layout
    base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Personal Finance Management{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f3f4f6; }
    </style>
</head>
<body class="bg-gray-100 font-sans leading-normal tracking-normal">
    <nav class="bg-blue-800 p-4 shadow-lg">
        <div class="container mx-auto flex justify-between items-center text-white">
            <a class="font-bold text-xl" href="/">FinanceManager</a>
            <div>
                {% if user.is_authenticated %}
                    <span class="mr-4">Welcome, {{ user.username }}</span>
                    <a href="{% url 'dashboard' %}" class="hover:text-blue-200 mr-4">Dashboard</a>
                    <a href="{% url 'logout' %}" class="hover:text-blue-200">Logout</a>
                {% else %}
                    <a href="{% url 'login' %}" class="hover:text-blue-200 mr-4">Login</a>
                    <a href="{% url 'register' %}" class="hover:text-blue-200">Register</a>
                {% endif %}
            </div>
        </div>
    </nav>
    <div class="container mx-auto mt-8 px-4 flex">
        {% if user.is_authenticated %}
        <aside class="w-64 bg-white rounded-lg shadow-md p-6 mr-6 hidden md:block h-screen sticky top-8">
            <h2 class="text-xl font-bold mb-6 text-gray-800 border-b pb-2">Menu</h2>
            <ul class="space-y-4">
                <li><a href="{% url 'dashboard' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Dashboard</a></li>
                <li><a href="{% url 'accounts:account-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Accounts</a></li>
                <li><a href="{% url 'income:income-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Income</a></li>
                <li><a href="{% url 'expenses:expense-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Expenses</a></li>
                <li><a href="{% url 'transactions:transaction-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Transactions</a></li>
                <li><a href="{% url 'budgets:budget-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Budgets</a></li>
                <li><a href="{% url 'savings:savingsgoal-list' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Savings Goals</a></li>
                <li><a href="{% url 'reports' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Reports</a></li>
                <li><a href="{% url 'analytics' %}" class="text-gray-600 hover:text-blue-600 transition-colors">Analytics</a></li>
                <li><a href="{% url 'ml_insights' %}" class="text-gray-600 hover:text-blue-600 transition-colors">ML Insights</a></li>
            </ul>
        </aside>
        {% endif %}
        <main class="flex-1 bg-white p-6 rounded-lg shadow-md">
            {% if messages %}
                {% for message in messages %}
                    <div class="p-4 mb-4 text-sm {% if message.tags == 'error' %}text-red-700 bg-red-100{% else %}text-green-700 bg-green-100{% endif %} rounded-lg" role="alert">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
            {% block content %}{% endblock %}
        </main>
    </div>
</body>
</html>"""
    
    # List template
    templates[f'{model_name.lower()}_list.html'] = f"""{{% extends 'base.html' %}}
{{% block title %}}{model_name}s{{% endblock %}}
{{% block content %}}
<div class="flex justify-between items-center mb-6">
    <h1 class="text-3xl font-bold text-gray-800">{model_name}s</h1>
    <a href="{{% url '{app_name}:{model_name.lower()}-create' %}}" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300">
        Add {model_name}
    </a>
</div>

<div class="overflow-x-auto bg-white rounded-lg shadow">
    <table class="min-w-full leading-normal">
        <thead>
            <tr>
                <th class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                    ID
                </th>
                <th class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                    Details
                </th>
                <th class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                    Actions
                </th>
            </tr>
        </thead>
        <tbody>
            {{% for item in {model_name.lower()}s %}}
            <tr>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                    <p class="text-gray-900 whitespace-no-wrap">{{{{ item.id }}}}</p>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                    <p class="text-gray-900 whitespace-no-wrap">{{{{ item }}}}</p>
                </td>
                <td class="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                    <a href="{{% url '{app_name}:{model_name.lower()}-detail' item.pk %}}" class="text-blue-600 hover:text-blue-900 mr-3">View</a>
                    <a href="{{% url '{app_name}:{model_name.lower()}-update' item.pk %}}" class="text-green-600 hover:text-green-900 mr-3">Edit</a>
                    <a href="{{% url '{app_name}:{model_name.lower()}-delete' item.pk %}}" class="text-red-600 hover:text-red-900">Delete</a>
                </td>
            </tr>
            {{% empty %}}
            <tr>
                <td colspan="3" class="px-5 py-5 border-b border-gray-200 bg-white text-sm text-center">
                    No {model_name}s found.
                </td>
            </tr>
            {{% endfor %}}
        </tbody>
    </table>
</div>
{{% if is_paginated %}}
<div class="mt-4 flex justify-center">
    <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
        {{% if page_obj.has_previous %}}
        <a href="?page={{{{ page_obj.previous_page_number }}}}" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            Previous
        </a>
        {{% endif %}}
        
        <span class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
            Page {{{{ page_obj.number }}}} of {{{{ page_obj.paginator.num_pages }}}}
        </span>
        
        {{% if page_obj.has_next %}}
        <a href="?page={{{{ page_obj.next_page_number }}}}" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            Next
        </a>
        {{% endif %}}
    </nav>
</div>
{{% endif %}}
{{% endblock %}}"""

    # Form template
    templates[f'{model_name.lower()}_form.html'] = f"""{{% extends 'base.html' %}}
{{% block title %}}{{% if form.instance.pk %}}Edit{{% else %}}New{{% endif %}} {model_name}{{% endblock %}}
{{% block content %}}
<div class="max-w-2xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">{{% if form.instance.pk %}}Edit{{% else %}}Create{{% endif %}} {model_name}</h1>
    <div class="bg-white rounded-lg shadow overflow-hidden p-6 border border-gray-200">
        <form method="post" class="space-y-6">
            {{% csrf_token %}}
            {{% for field in form %}}
            <div>
                <label for="{{{{ field.id_for_label }}}}" class="block text-sm font-medium text-gray-700 mb-1">
                    {{{{ field.label }}}}
                </label>
                {{{{ field }}}}
                {{% if field.help_text %}}
                <p class="mt-1 text-sm text-gray-500">{{{{ field.help_text }}}}</p>
                {{% endif %}}
                {{% for error in field.errors %}}
                <p class="mt-1 text-sm text-red-600">{{{{ error }}}}</p>
                {{% endfor %}}
            </div>
            {{% endfor %}}
            <div class="flex items-center justify-end space-x-4 mt-8 pt-4 border-t border-gray-100">
                <a href="{{% url '{app_name}:{model_name.lower()}-list' %}}" class="text-gray-600 hover:text-gray-900 font-medium transition duration-150">Cancel</a>
                <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded transition duration-300 shadow-sm">
                    Save {model_name}
                </button>
            </div>
        </form>
    </div>
</div>
{{% endblock %}}"""

    # Detail template
    templates[f'{model_name.lower()}_detail.html'] = f"""{{% extends 'base.html' %}}
{{% block title %}}{model_name} Details{{% endblock %}}
{{% block content %}}
<div class="max-w-3xl mx-auto">
    <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800">{model_name} Details</h1>
        <div>
            <a href="{{% url '{app_name}:{model_name.lower()}-update' {model_name.lower()}.pk %}}" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2 transition duration-300">Edit</a>
            <a href="{{% url '{app_name}:{model_name.lower()}-delete' {model_name.lower()}.pk %}}" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition duration-300">Delete</a>
        </div>
    </div>
    <div class="bg-white shadow overflow-hidden sm:rounded-lg border border-gray-200">
        <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">Information</h3>
        </div>
        <div class="border-t border-gray-200">
            <dl>
                <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt class="text-sm font-medium text-gray-500">ID</dt>
                    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{{{ {model_name.lower()}.id }}}}</dd>
                </div>
                <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                    <dt class="text-sm font-medium text-gray-500">Details</dt>
                    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{{{{ {model_name.lower()} }}}}</dd>
                </div>
                <!-- Additional fields can be added here manually later -->
            </dl>
        </div>
    </div>
    <div class="mt-6">
        <a href="{{% url '{app_name}:{model_name.lower()}-list' %}}" class="text-blue-600 hover:text-blue-800 font-medium">&larr; Back to {model_name}s list</a>
    </div>
</div>
{{% endblock %}}"""

    # Delete template
    templates[f'{model_name.lower()}_confirm_delete.html'] = f"""{{% extends 'base.html' %}}
{{% block title %}}Delete {model_name}{{% endblock %}}
{{% block content %}}
<div class="max-w-xl mx-auto mt-10">
    <div class="bg-white shadow sm:rounded-lg border border-red-200">
        <div class="px-4 py-5 sm:p-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">
                Delete {model_name}
            </h3>
            <div class="mt-2 max-w-xl text-sm text-gray-500">
                <p>
                    Are you sure you want to delete this {model_name}? This action cannot be undone.
                </p>
                <p class="mt-2 font-bold text-gray-700">{{{{ {model_name.lower()} }}}}</p>
            </div>
            <div class="mt-5">
                <form method="post">
                    {{% csrf_token %}}
                    <button type="submit" class="inline-flex items-center justify-center px-4 py-2 border border-transparent font-medium rounded-md text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:text-sm">
                        Confirm Delete
                    </button>
                    <a href="{{% url '{app_name}:{model_name.lower()}-list' %}}" class="ml-3 inline-flex items-center justify-center px-4 py-2 border border-gray-300 font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:text-sm">
                        Cancel
                    </a>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}"""

    return base_html, templates


APPS_TO_PROCESS = {
    'accounts': 'Account',
    'income': 'Income',
    'expenses': 'Expense',
    'transactions': 'Transaction',
    'budgets': 'Budget',
    'savings': 'SavingsGoal',
}

def generate_tests(app_name, model_name):
    return f'''from django.test import TestCase
from django.urls import reverse
from users.models import User
from .models import {model_name}

class {model_name}Tests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        # We might need additional setup depending on the model, this is a base
        
    def test_list_view_unauthenticated(self):
        response = self.client.get(reverse('{app_name}:{model_name.lower()}-list'))
        self.assertEqual(response.status_code, 302) # Redirect to login
        
    def test_list_view_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('{app_name}:{model_name.lower()}-list'))
        self.assertEqual(response.status_code, 200)
'''

def main():
    base_html_written = False
    for app, model in APPS_TO_PROCESS.items():
        print(f"Generating scaffolding for {{app}}...")
        
        # Write views
        with open(os.path.join(app, "views.py"), "w") as f:
            f.write(generate_views(app, model))
            
        # Write forms
        with open(os.path.join(app, "forms.py"), "w") as f:
            f.write(generate_forms(app, model))
            
        # Write urls
        with open(os.path.join(app, "urls.py"), "w") as f:
            f.write(generate_urls(app, model))
            
        # Write tests
        with open(os.path.join(app, "tests.py"), "w") as f:
            f.write(generate_tests(app, model))
            
        # Create templates dir
        template_dir = os.path.join("templates", app)
        os.makedirs(template_dir, exist_ok=True)
        
        base_html, templates = generate_templates(app, model)
        
        if not base_html_written:
            with open(os.path.join("templates", "base.html"), "w") as f:
                f.write(base_html)
            base_html_written = True
            
        for name, content in templates.items():
            with open(os.path.join(template_dir, name), "w") as f:
                f.write(content)
                
    # Update main urls.py
    main_urls_path = os.path.join("config", "urls.py")
    with open(main_urls_path, "w") as f:
        f.write("""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts-app/', include('accounts.urls')),
    path('income/', include('income.urls')),
    path('expenses/', include('expenses.urls')),
    path('transactions/', include('transactions.urls')),
    path('budgets/', include('budgets.urls')),
    path('savings/', include('savings.urls')),
]
""")

if __name__ == "__main__":
    main()
    print("Full app generation complete.")

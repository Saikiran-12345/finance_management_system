import os

def write_analytics():
    os.makedirs("analytics/templates/analytics", exist_ok=True)
    
    views_code = """from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from budgets.models import Budget
from savings.models import SavingsGoal
from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta

class AnalyticsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # We process lots of data for the charts
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=365)
        
        transactions = Transaction.objects.filter(user=user, date__gte=start_date, date__lte=end_date)
        
        # 1. Monthly Income vs Expense
        monthly_stats = {}
        for t in transactions:
            month_key = t.date.strftime('%Y-%m')
            if month_key not in monthly_stats:
                monthly_stats[month_key] = {'income': 0, 'expense': 0}
            if t.transaction_type == 'INCOME':
                monthly_stats[month_key]['income'] += float(t.amount)
            elif t.transaction_type == 'EXPENSE':
                monthly_stats[month_key]['expense'] += float(t.amount)
                
        context['monthly_stats'] = monthly_stats
        
        # 2. Expense by Category
        expenses = transactions.filter(transaction_type='EXPENSE')
        cat_stats = expenses.values('category_name').annotate(total=Sum('amount')).order_by('-total')
        context['category_stats'] = list(cat_stats)
        
        # 3. Income by Source
        incomes = transactions.filter(transaction_type='INCOME')
        income_source_stats = incomes.values('category_name').annotate(total=Sum('amount')).order_by('-total')
        context['income_source_stats'] = list(income_source_stats)
        
        # Add more context variables...
        context['page_title'] = 'Advanced Analytics'
        
        return context
"""
    with open("analytics/views.py", "w") as f:
        f.write(views_code)
        
    urls_code = """from django.urls import path
from .views import AnalyticsDashboardView

urlpatterns = [
    path('', AnalyticsDashboardView.as_view(), name='analytics-dashboard'),
]
"""
    with open("analytics/urls.py", "w") as f:
        f.write(urls_code)

    # Let's generate a massive HTML template with embedded Chart.js
    html = """{% extends 'base.html' %}
{% block title %}Analytics Dashboard{% endblock %}
{% block content %}
<div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold mb-8 text-gray-800">Advanced Financial Analytics</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 mb-8">
        <!-- Chart 1 -->
        <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
            <h3 class="text-xl font-semibold mb-4 text-gray-700">Income vs Expenses (12 Months)</h3>
            <canvas id="incomeExpenseChart" height="250"></canvas>
        </div>
        
        <!-- Chart 2 -->
        <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
            <h3 class="text-xl font-semibold mb-4 text-gray-700">Expense Breakdown by Category</h3>
            <canvas id="categoryChart" height="250"></canvas>
        </div>
        
        <!-- Chart 3 -->
        <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
            <h3 class="text-xl font-semibold mb-4 text-gray-700">Income Sources</h3>
            <canvas id="incomeSourceChart" height="250"></canvas>
        </div>
        
        <!-- Chart 4 -->
        <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-100">
            <h3 class="text-xl font-semibold mb-4 text-gray-700">Savings Rate Trend</h3>
            <canvas id="savingsRateChart" height="250"></canvas>
        </div>
    </div>
    
    <!-- Complex Data Table -->
    <div class="bg-white p-6 rounded-xl shadow-lg border border-gray-100 mt-8">
        <h3 class="text-xl font-semibold mb-4 text-gray-700">Top Expense Categories</h3>
        <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Total Spent</th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    {% for cat in category_stats %}
                    <tr>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ cat.category_name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${{ cat.total|floatformat:2 }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // Data parsing
    const monthlyStats = {{ monthly_stats|safe }};
    const labels = Object.keys(monthlyStats).sort();
    const incomeData = labels.map(l => monthlyStats[l].income);
    const expenseData = labels.map(l => monthlyStats[l].expense);
    const savingsRateData = labels.map(l => {
        const inc = monthlyStats[l].income;
        const exp = monthlyStats[l].expense;
        return inc > 0 ? ((inc - exp) / inc * 100).toFixed(2) : 0;
    });
    
    // Category Data
    const catStats = {{ category_stats|safe }};
    const catLabels = catStats.map(c => c.category_name || 'Other');
    const catData = catStats.map(c => c.total);
    
    // Income Source Data
    const incStats = {{ income_source_stats|safe }};
    const incLabels = incStats.map(c => c.category_name || 'Other');
    const incData = incStats.map(c => c.total);

    // Chart 1: Income vs Expense
    new Chart(document.getElementById('incomeExpenseChart'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Income',
                    data: incomeData,
                    backgroundColor: 'rgba(34, 197, 94, 0.6)',
                    borderColor: 'rgb(34, 197, 94)',
                    borderWidth: 1
                },
                {
                    label: 'Expense',
                    data: expenseData,
                    backgroundColor: 'rgba(239, 68, 68, 0.6)',
                    borderColor: 'rgb(239, 68, 68)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Chart 2: Categories
    new Chart(document.getElementById('categoryChart'), {
        type: 'doughnut',
        data: {
            labels: catLabels,
            datasets: [{
                data: catData,
                backgroundColor: [
                    '#3b82f6', '#ef4444', '#10b981', '#f59e0b', '#6366f1',
                    '#ec4899', '#8b5cf6', '#14b8a6', '#f43f5e', '#84cc16'
                ]
            }]
        },
        options: { responsive: true }
    });
    
    // Chart 3: Income Sources
    new Chart(document.getElementById('incomeSourceChart'), {
        type: 'pie',
        data: {
            labels: incLabels,
            datasets: [{
                data: incData,
                backgroundColor: [
                    '#10b981', '#3b82f6', '#8b5cf6', '#f59e0b', '#6366f1'
                ]
            }]
        },
        options: { responsive: true }
    });

    // Chart 4: Savings Rate
    new Chart(document.getElementById('savingsRateChart'), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Savings Rate (%)',
                data: savingsRateData,
                fill: false,
                borderColor: 'rgb(99, 102, 241)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true, max: 100 }
            }
        }
    });
</script>
{% endblock %}
"""
    with open("analytics/templates/analytics/dashboard.html", "w") as f:
        f.write(html)
        
    # Update main urls
    with open("config/urls.py", "r") as f:
        urls = f.read()
    if "'analytics.urls'" not in urls:
        urls = urls.replace(
            "path('savings/', include('savings.urls')),",
            "path('savings/', include('savings.urls')),\n    path('analytics/', include('analytics.urls')),"
        )
        with open("config/urls.py", "w") as f:
            f.write(urls)

if __name__ == "__main__":
    write_analytics()
    print("Analytics generated.")

import os

def write_ml_ui():
    os.makedirs("ml/templates/ml", exist_ok=True)
    
    views_code = """from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ml.expense_prediction import ExpensePredictor
from ml.segmentation import UserSegmentation
from ml.anomaly_detection import AnomalyDetector
from ml.savings_prediction import SavingsPredictor
from transactions.models import Transaction

class MLInsightsView(LoginRequiredMixin, TemplateView):
    template_name = 'ml/insights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # 1. Expense Prediction
        exp_pred = ExpensePredictor(user)
        next_month_exp, exp_msg = exp_pred.predict_next_month()
        context['predicted_expense'] = next_month_exp
        context['expense_msg'] = exp_msg
        
        # 2. Segmentation
        seg = UserSegmentation()
        segment = seg.predict_user_segment(user)
        context['user_segment'] = segment
        
        # 3. Anomaly Detection
        anom = AnomalyDetector(user)
        anomaly_ids = anom.detect_anomalies()
        anomalies = Transaction.objects.filter(id__in=anomaly_ids) if anomaly_ids else []
        context['anomalies'] = anomalies
        
        # 4. Savings Prediction
        sav = SavingsPredictor(user)
        future_savings = sav.predict_future_savings(months_ahead=3)
        context['future_savings'] = future_savings
        
        return context
"""
    with open("ml/views.py", "w") as f:
        f.write(views_code)
        
    urls_code = """from django.urls import path
from .views import MLInsightsView

urlpatterns = [
    path('', MLInsightsView.as_view(), name='ml_insights'),
]
"""
    with open("ml/urls.py", "w") as f:
        f.write(urls_code)

    html = """{% extends 'base.html' %}
{% block title %}AI & ML Insights{% endblock %}
{% block content %}
<div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">AI & Machine Learning Insights</h1>
    
    <div class="bg-indigo-50 border-l-4 border-indigo-500 p-4 mb-8">
        <p class="text-indigo-700">These insights are generated using Machine Learning models running locally on your historical data.</p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <!-- Predict Expense -->
        <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
            <h3 class="text-xl font-bold text-gray-700 mb-2">Next Month's Expense Prediction</h3>
            {% if predicted_expense %}
                <p class="text-4xl font-bold text-red-600 mb-2">${{ predicted_expense|floatformat:2 }}</p>
                <p class="text-gray-500 text-sm">Based on polynomial regression of your past expenses.</p>
            {% else %}
                <p class="text-gray-500">{{ expense_msg }}</p>
            {% endif %}
        </div>
        
        <!-- Segmentation -->
        <div class="bg-white p-6 rounded-lg shadow border border-gray-200">
            <h3 class="text-xl font-bold text-gray-700 mb-2">Spending Behavior Segment</h3>
            <p class="text-3xl font-bold text-blue-600 mb-2">{{ user_segment }}</p>
            <p class="text-gray-500 text-sm">Calculated using K-Means clustering across all platform users.</p>
        </div>
    </div>
    
    <!-- Future Savings -->
    <div class="bg-white p-6 rounded-lg shadow border border-gray-200 mb-8">
        <h3 class="text-xl font-bold text-gray-700 mb-4">Predicted Savings (Next 3 Months)</h3>
        {% if future_savings %}
            <div class="grid grid-cols-3 gap-4">
            {% for pred in future_savings %}
                <div class="bg-gray-50 p-4 rounded text-center">
                    <p class="text-sm text-gray-500 mb-1">Month +{{ pred.month_ahead }}</p>
                    <p class="text-2xl font-bold text-green-600">${{ pred.predicted_savings|floatformat:2 }}</p>
                </div>
            {% endfor %}
            </div>
            <p class="mt-4 text-gray-500 text-sm">Based on Ridge Regression analysis of cumulative savings.</p>
        {% else %}
            <p class="text-gray-500">Not enough data to predict future savings.</p>
        {% endif %}
    </div>
    
    <!-- Anomalies -->
    <div class="bg-white p-6 rounded-lg shadow border border-gray-200 border-t-4 border-t-red-500">
        <h3 class="text-xl font-bold text-gray-700 mb-4">Unusual Expense Detection</h3>
        <p class="text-sm text-gray-600 mb-4">The following transactions were flagged as anomalous based on your normal spending habits using Isolation Forest.</p>
        
        {% if anomalies %}
            <div class="overflow-x-auto">
                <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Date</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Category</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
                            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white divide-y divide-gray-200">
                        {% for a in anomalies %}
                        <tr class="bg-red-50">
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ a.date }}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ a.category_name }}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-red-600">${{ a.amount }}</td>
                            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ a.description }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="p-4 bg-green-50 text-green-700 rounded border border-green-200">
                No unusual expenses detected! Your spending is consistent.
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
"""
    with open("ml/templates/ml/insights.html", "w") as f:
        f.write(html)
        
    # Update main urls
    with open("config/urls.py", "r") as f:
        urls = f.read()
    if "'ml.urls'" not in urls:
        urls = urls.replace(
            "path('reports/', include('reports.urls')),",
            "path('reports/', include('reports.urls')),\n    path('ml/', include('ml.urls')),"
        )
        with open("config/urls.py", "w") as f:
            f.write(urls)

if __name__ == "__main__":
    write_ml_ui()
    print("ML UI generated.")

from django.views.generic import TemplateView
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

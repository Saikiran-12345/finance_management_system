from django.core.management.base import BaseCommand
from users.models import User
from ml.expense_prediction import ExpensePredictor
from ml.segmentation import UserSegmentation
from ml.anomaly_detection import AnomalyDetector
from ml.savings_prediction import SavingsPredictor

class Command(BaseCommand):
    help = 'Trains ML models for all users'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting ML training process...'))
        
        users = User.objects.filter(role='USER')
        
        # 1. Global Segmentation
        self.stdout.write('Training Global User Segmentation Model...')
        seg_model = UserSegmentation()
        success, msg = seg_model.train()
        if success:
            self.stdout.write(self.style.SUCCESS(f'Segmentation: {msg}'))
        else:
            self.stdout.write(self.style.WARNING(f'Segmentation skipped: {msg}'))
            
        # 2. User specific models
        for user in users:
            self.stdout.write(f'Training models for user: {user.username}')
            
            # Expense Prediction
            exp_model = ExpensePredictor(user)
            success, msg = exp_model.train()
            if success:
                self.stdout.write(self.style.SUCCESS(f'  - Expense Predictor: {msg}'))
                
            # Anomaly Detection
            anom_model = AnomalyDetector(user)
            success, msg = anom_model.train()
            if success:
                self.stdout.write(self.style.SUCCESS(f'  - Anomaly Detector: {msg}'))
                
            # Savings Prediction
            sav_model = SavingsPredictor(user)
            success = sav_model.train()
            if success:
                self.stdout.write(self.style.SUCCESS(f'  - Savings Predictor: Success'))

        self.stdout.write(self.style.SUCCESS('Successfully trained all ML models.'))

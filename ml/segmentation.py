import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from users.models import User
from transactions.models import Transaction
from django.db.models import Sum, Count
import pickle
import os

class UserSegmentation:
    def __init__(self):
        self.model_path = "data/model_segmentation.pkl"
        self.scaler_path = "data/scaler_segmentation.pkl"

    def get_features(self):
        users = User.objects.all()
        data = []
        
        for user in users:
            expense_total = Transaction.objects.filter(user=user, transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
            income_total = Transaction.objects.filter(user=user, transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
            txn_count = Transaction.objects.filter(user=user).count()
            
            savings_rate = 0
            if income_total > 0:
                savings_rate = float((income_total - expense_total) / income_total)
                
            data.append({
                'user_id': user.id,
                'total_expense': float(expense_total),
                'txn_count': txn_count,
                'savings_rate': savings_rate
            })
            
        return pd.DataFrame(data)

    def train(self):
        df = self.get_features()
        if len(df) < 3:
            return False, "Not enough users to segment"
            
        features = df[['total_expense', 'txn_count', 'savings_rate']]
        
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(kmeans, f)
        with open(self.scaler_path, 'wb') as f:
            pickle.dump(scaler, f)
            
        return True, "Segmentation model trained"

    def predict_user_segment(self, user):
        if not os.path.exists(self.model_path):
            return "Unknown"
            
        expense_total = Transaction.objects.filter(user=user, transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
        income_total = Transaction.objects.filter(user=user, transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
        txn_count = Transaction.objects.filter(user=user).count()
        
        savings_rate = 0
        if income_total > 0:
            savings_rate = float((income_total - expense_total) / income_total)
            
        with open(self.scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
            
        scaled = scaler.transform([[float(expense_total), txn_count, savings_rate]])
        cluster = model.predict(scaled)[0]
        
        labels = {
            0: "Low Spending",
            1: "Moderate Spending",
            2: "High Spending"
        }
        
        return labels.get(cluster, "Unknown")

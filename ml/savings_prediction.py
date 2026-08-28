import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from transactions.models import Transaction
from django.utils import timezone
import pickle
import os

class SavingsPredictor:
    def __init__(self, user):
        self.user = user
        self.model_path = f"data/model_savings_user_{user.id}.pkl"

    def get_data(self):
        transactions = Transaction.objects.filter(user=self.user).order_by('date')
        if not transactions.exists():
            return None
            
        data = []
        for t in transactions:
            data.append({
                'date': t.date,
                'amount': float(t.amount) if t.transaction_type == 'INCOME' else -float(t.amount)
            })
            
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        
        df.set_index('date', inplace=True)
        monthly_data = df.resample('ME').sum().reset_index()
        monthly_data['month_index'] = np.arange(len(monthly_data))
        monthly_data['cumulative_savings'] = monthly_data['amount'].cumsum()
        return monthly_data

    def train(self):
        df = self.get_data()
        if df is None or len(df) < 3:
            return False
            
        X = df[['month_index']].values
        y = df['cumulative_savings'].values
        
        model = Ridge(alpha=1.0)
        model.fit(X, y)
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)
            
        return True

    def predict_future_savings(self, months_ahead=6):
        df = self.get_data()
        if df is None or len(df) < 3:
            return None
            
        if not os.path.exists(self.model_path):
            self.train()
            
        if not os.path.exists(self.model_path):
            return None
            
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
            
        last_month = df['month_index'].max()
        predictions = []
        
        for i in range(1, months_ahead + 1):
            pred = model.predict([[last_month + i]])[0]
            predictions.append({
                'month_ahead': i,
                'predicted_savings': max(0, pred)
            })
            
        return predictions

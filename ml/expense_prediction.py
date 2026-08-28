import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from django.utils import timezone
from transactions.models import Transaction
import pickle
import os

class ExpensePredictor:
    def __init__(self, user):
        self.user = user
        self.model_path = f"data/model_expense_user_{user.id}.pkl"
        self.model = None

    def get_data(self):
        transactions = Transaction.objects.filter(user=self.user, transaction_type='EXPENSE').order_by('date')
        if not transactions.exists():
            return None
            
        data = []
        for t in transactions:
            data.append({
                'date': t.date,
                'amount': float(t.amount)
            })
            
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        
        # Aggregate by month
        df.set_index('date', inplace=True)
        monthly_data = df.resample('ME').sum().reset_index()
        monthly_data['month_index'] = np.arange(len(monthly_data))
        return monthly_data
        
    def train(self):
        df = self.get_data()
        if df is None or len(df) < 3:
            return False, "Not enough data to train"
            
        X = df[['month_index']].values
        y = df['amount'].values
        
        self.model = make_pipeline(PolynomialFeatures(2), LinearRegression())
        self.model.fit(X, y)
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)
            
        return True, "Model trained successfully"
        
    def predict_next_month(self):
        df = self.get_data()
        if df is None or len(df) < 3:
            return None, "Not enough data"
            
        if not os.path.exists(self.model_path):
            success, _ = self.train()
            if not success:
                return None, "Training failed"
                
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        next_month_index = df['month_index'].max() + 1
        prediction = self.model.predict([[next_month_index]])
        return max(0, prediction[0]), "Success"

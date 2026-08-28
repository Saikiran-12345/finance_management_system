import pandas as pd
from sklearn.ensemble import IsolationForest
from transactions.models import Transaction
import pickle
import os

class AnomalyDetector:
    def __init__(self, user):
        self.user = user
        self.model_path = f"data/model_anomaly_user_{user.id}.pkl"

    def get_data(self):
        transactions = Transaction.objects.filter(user=self.user, transaction_type='EXPENSE')
        if not transactions.exists():
            return None
            
        data = []
        for t in transactions:
            data.append({
                'id': t.id,
                'amount': float(t.amount)
            })
        return pd.DataFrame(data)

    def train(self):
        df = self.get_data()
        if df is None or len(df) < 10:
            return False, "Not enough data"
            
        X = df[['amount']].values
        
        model = IsolationForest(contamination=0.05, random_state=42)
        model.fit(X)
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)
            
        return True, "Model trained"

    def detect_anomalies(self):
        df = self.get_data()
        if df is None or len(df) < 10:
            return []
            
        if not os.path.exists(self.model_path):
            self.train()
            
        if not os.path.exists(self.model_path):
            return []
            
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
            
        X = df[['amount']].values
        preds = model.predict(X)
        
        anomalies = []
        for i, pred in enumerate(preds):
            if pred == -1:
                anomalies.append(df.iloc[i]['id'])
                
        return anomalies

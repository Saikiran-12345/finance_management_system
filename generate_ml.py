import os

ml_models = {
    "expense_prediction": """import pandas as pd
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
""",
    "segmentation": """import pandas as pd
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
""",
    "anomaly_detection": """import pandas as pd
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
""",
    "savings_prediction": """import pandas as pd
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
"""
}

def write_ml_models():
    os.makedirs("ml", exist_ok=True)
    with open(os.path.join("ml", "__init__.py"), "w") as f:
        f.write("")
        
    for name, content in ml_models.items():
        with open(os.path.join("ml", f"{name}.py"), "w") as f:
            f.write(content)

if __name__ == "__main__":
    write_ml_models()
    print("ML modules generated.")

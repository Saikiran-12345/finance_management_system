# Personal Finance Management System

## 1. Project Name
Personal Finance Management System

## 2. Domain
FinTech

## 3. Technology Stack
- **Backend**: Python 3, Django, Django REST Framework
- **Frontend**: HTML5, Custom CSS, JavaScript (Chart.js for analytics)
- **Database**: SQLite (via Django ORM)
- **Machine Learning**: scikit-learn, Pandas, NumPy
- **Testing**: Django TestCase, PyTest

## 4. Architecture
Monolithic Django Application utilizing the Model-View-Template (MVT) pattern. The application exposes standard HTML rendered views for the frontend and a complete REST API using Django REST Framework for external consumers. 

## 5. Major Modules
- **Users**: Custom authentication, RBAC (User, Manager, Admin).
- **Accounts**: Multi-account management (Savings, Current, Credit).
- **Transactions**: Double-entry style income and expense tracking.
- **Budgets**: Thresholds and limit management.
- **Savings**: Goal tracking and projection.
- **Analytics**: Pandas-driven aggregation and metrics.
- **Reports**: CSV and PDF data exports.
- **Notifications**: Internal alert system.
- **Audit**: Immutable audit logging for security.
- **ML**: Dedicated machine learning intelligence suite.

## 6. ML Features
1. **Expense Prediction**: Polynomial Linear Regression predicting next month's spending.
2. **User Segmentation**: K-Means clustering separating users into Low, Moderate, and High spending brackets.
3. **Anomaly Detection**: Isolation Forest model detecting unusual transactions and potential fraud.
4. **Savings Prediction**: Ridge Regression projecting future savings trajectories.

## 7. Database Models
Extensive relational modeling including: `User`, `Account`, `IncomeCategory`, `Income`, `ExpenseCategory`, `Expense`, `Transaction`, `Budget`, `SavingsGoal`, `Notification`, and `AuditLog`.

## 8. API Modules
Fully featured REST API utilizing ViewSets and ModelSerializers available under `/api/v1/`.

## 9. Testing Summary
Comprehensive testing covering unit models, API endpoints, permissions, and ML pipelines. Tests are auto-discovered and run via Django test runner.

## 10. Security Summary
- CSRF Protection on all forms
- LoginRequiredMixin for all private views
- DRF IsAuthenticated permission classes
- ORM protection against SQL injection
- XSS prevention via Django template auto-escaping

## 11. Installation & Run Instructions
```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\\Scripts\\activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Seed the database with demo data (Generates 2 years of history)
python manage.py seed_data

# 5. Train the Machine Learning models locally
python manage.py train_ml

# 6. Run the server
python manage.py runserver
```

## 12. Sample Credentials
- **Username**: `demo_user`
- **Password**: `demo1234`
- **Admin**: `admin` / `admin`

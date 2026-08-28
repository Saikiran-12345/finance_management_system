import os

seed_data_code = """from django.core.management.base import BaseCommand
from users.models import User
from accounts.models import Account
from income.models import IncomeCategory, Income
from expenses.models import ExpenseCategory, Expense
from transactions.models import Transaction
from budgets.models import Budget
from savings.models import SavingsGoal
from notifications.models import Notification
from audit.models import AuditLog
from django.utils import timezone
from datetime import timedelta
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds the database with sample data for demonstration and ML testing'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting data seeding process...'))
        
        # 1. Create Users
        self.stdout.write('Creating users...')
        user, created = User.objects.get_or_create(
            username='demo_user',
            defaults={
                'email': 'demo@example.com',
                'first_name': 'Demo',
                'last_name': 'User',
                'role': 'USER'
            }
        )
        if created:
            user.set_password('demo1234')
            user.save()
            
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
                'role': 'ADMIN'
            }
        )
        if created:
            admin.set_password('admin')
            admin.save()
            
        # 2. Create Categories
        income_categories = ['Salary', 'Freelancing', 'Business', 'Bonus', 'Interest', 'Other']
        for cat in income_categories:
            IncomeCategory.objects.get_or_create(name=cat)
            
        expense_categories = ['Food', 'Travel', 'Shopping', 'Bills', 'Education', 'Healthcare', 'Entertainment', 'Rent', 'Transportation', 'Other']
        for cat in expense_categories:
            ExpenseCategory.objects.get_or_create(name=cat)

        # 3. Create Accounts
        checking, _ = Account.objects.get_or_create(
            user=user, name='Main Checking', account_type='CURRENT', defaults={'balance': Decimal('5000.00')}
        )
        savings, _ = Account.objects.get_or_create(
            user=user, name='High Yield Savings', account_type='SAVINGS', defaults={'balance': Decimal('12000.00')}
        )
        credit, _ = Account.objects.get_or_create(
            user=user, name='Rewards Credit Card', account_type='OTHER', defaults={'balance': Decimal('-1500.00')}
        )

        # 4. Generate Historical Transactions (2 years back)
        self.stdout.write('Generating 2 years of historical transactions...')
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=730)
        
        current_date = start_date
        
        income_cats = list(IncomeCategory.objects.all())
        expense_cats = list(ExpenseCategory.objects.all())
        
        # Salary is recurring
        salary_cat = IncomeCategory.objects.get(name='Salary')
        rent_cat = ExpenseCategory.objects.get(name='Rent')
        
        transactions = []
        
        while current_date <= end_date:
            # Monthly Salary
            if current_date.day == 1:
                transactions.append(Transaction(
                    user=user, account=checking, transaction_type='INCOME',
                    amount=Decimal('4500.00'), date=current_date, description='Monthly Salary',
                    category_name='Salary'
                ))
                # Pay rent
                transactions.append(Transaction(
                    user=user, account=checking, transaction_type='EXPENSE',
                    amount=Decimal('1200.00'), date=current_date, description='Rent Payment',
                    category_name='Rent'
                ))
                
            # Random daily expenses (Food, Transport, Shopping)
            if random.random() > 0.3:  # 70% chance of an expense on any given day
                num_tx = random.randint(1, 3)
                for _ in range(num_tx):
                    cat = random.choice(expense_cats)
                    amt = Decimal(random.uniform(5.0, 150.0)).quantize(Decimal('0.01'))
                    
                    # Occasional large anomaly expense
                    if random.random() < 0.01:
                        amt = Decimal(random.uniform(800.0, 2000.0)).quantize(Decimal('0.01'))
                        
                    transactions.append(Transaction(
                        user=user, account=checking, transaction_type='EXPENSE',
                        amount=amt, date=current_date, description=f'Purchase at {cat.name} store',
                        category_name=cat.name
                    ))
                    
            # Occasional side income
            if random.random() < 0.05:
                cat = random.choice([c for c in income_cats if c.name != 'Salary'])
                amt = Decimal(random.uniform(100.0, 800.0)).quantize(Decimal('0.01'))
                transactions.append(Transaction(
                    user=user, account=checking, transaction_type='INCOME',
                    amount=amt, date=current_date, description=f'Side hustle - {cat.name}',
                    category_name=cat.name
                ))
                
            current_date += timedelta(days=1)
            
        Transaction.objects.bulk_create(transactions)
        
        # 5. Budgets
        self.stdout.write('Creating budgets...')
        Budget.objects.get_or_create(
            user=user, category=ExpenseCategory.objects.get(name='Food'),
            month=end_date.replace(day=1), defaults={'amount': Decimal('600.00')}
        )
        Budget.objects.get_or_create(
            user=user, category=ExpenseCategory.objects.get(name='Entertainment'),
            month=end_date.replace(day=1), defaults={'amount': Decimal('200.00')}
        )
        
        # 6. Savings Goals
        self.stdout.write('Creating savings goals...')
        SavingsGoal.objects.get_or_create(
            user=user, name='New Laptop', target_amount=Decimal('2000.00'),
            defaults={'current_amount': Decimal('800.00'), 'target_date': end_date + timedelta(days=90)}
        )
        SavingsGoal.objects.get_or_create(
            user=user, name='Emergency Fund', target_amount=Decimal('10000.00'),
            defaults={'current_amount': Decimal('6500.00'), 'target_date': end_date + timedelta(days=365)}
        )
        
        # 7. Notifications and Audit
        Notification.objects.get_or_create(
            user=user, notification_type='SYSTEM', message='Welcome to Personal Finance Management System!'
        )
        AuditLog.objects.create(
            user=admin, action='SEED', module='SYSTEM', description='Database seeded with demo data'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database.'))
"""

def write_management_commands():
    app_dir = os.path.join("core", "management", "commands")
    os.makedirs(app_dir, exist_ok=True)
    
    with open(os.path.join(app_dir, "__init__.py"), "w") as f:
        f.write("")
    with open(os.path.join(os.path.dirname(app_dir), "__init__.py"), "w") as f:
        f.write("")
        
    with open(os.path.join(app_dir, "seed_data.py"), "w") as f:
        f.write(seed_data_code)

if __name__ == "__main__":
    write_management_commands()
    print("Management commands generated.")

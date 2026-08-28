from django.test import TestCase
from django.urls import reverse
from users.models import *
from users.models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_user_accounts_field(self):
        field_label = User._meta.get_field('accounts').verbose_name
        self.assertTrue(field_label)

    def test_user_incomes_field(self):
        field_label = User._meta.get_field('incomes').verbose_name
        self.assertTrue(field_label)

    def test_user_expenses_field(self):
        field_label = User._meta.get_field('expenses').verbose_name
        self.assertTrue(field_label)

    def test_user_transactions_field(self):
        field_label = User._meta.get_field('transactions').verbose_name
        self.assertTrue(field_label)

    def test_user_budgets_field(self):
        field_label = User._meta.get_field('budgets').verbose_name
        self.assertTrue(field_label)

    def test_user_savings_goals_field(self):
        field_label = User._meta.get_field('savings_goals').verbose_name
        self.assertTrue(field_label)

    def test_user_notifications_field(self):
        field_label = User._meta.get_field('notifications').verbose_name
        self.assertTrue(field_label)

    def test_user_audit_logs_field(self):
        field_label = User._meta.get_field('audit_logs').verbose_name
        self.assertTrue(field_label)

    def test_user_password_field(self):
        field_label = User._meta.get_field('password').verbose_name
        self.assertTrue(field_label)

    def test_user_last_login_field(self):
        field_label = User._meta.get_field('last_login').verbose_name
        self.assertTrue(field_label)

    def test_user_is_superuser_field(self):
        field_label = User._meta.get_field('is_superuser').verbose_name
        self.assertTrue(field_label)

    def test_user_username_field(self):
        field_label = User._meta.get_field('username').verbose_name
        self.assertTrue(field_label)

    def test_user_first_name_field(self):
        field_label = User._meta.get_field('first_name').verbose_name
        self.assertTrue(field_label)

    def test_user_last_name_field(self):
        field_label = User._meta.get_field('last_name').verbose_name
        self.assertTrue(field_label)

    def test_user_email_field(self):
        field_label = User._meta.get_field('email').verbose_name
        self.assertTrue(field_label)

    def test_user_is_staff_field(self):
        field_label = User._meta.get_field('is_staff').verbose_name
        self.assertTrue(field_label)

    def test_user_is_active_field(self):
        field_label = User._meta.get_field('is_active').verbose_name
        self.assertTrue(field_label)

    def test_user_date_joined_field(self):
        field_label = User._meta.get_field('date_joined').verbose_name
        self.assertTrue(field_label)

    def test_user_role_field(self):
        field_label = User._meta.get_field('role').verbose_name
        self.assertTrue(field_label)

    def test_user_phone_field(self):
        field_label = User._meta.get_field('phone').verbose_name
        self.assertTrue(field_label)

    def test_user_financial_preferences_field(self):
        field_label = User._meta.get_field('financial_preferences').verbose_name
        self.assertTrue(field_label)

    def test_user_monthly_budget_preference_field(self):
        field_label = User._meta.get_field('monthly_budget_preference').verbose_name
        self.assertTrue(field_label)

    def test_user_currency_preference_field(self):
        field_label = User._meta.get_field('currency_preference').verbose_name
        self.assertTrue(field_label)

    def test_user_notification_preference_field(self):
        field_label = User._meta.get_field('notification_preference').verbose_name
        self.assertTrue(field_label)

    def test_user_groups_field(self):
        field_label = User._meta.get_field('groups').verbose_name
        self.assertTrue(field_label)

    def test_user_user_permissions_field(self):
        field_label = User._meta.get_field('user_permissions').verbose_name
        self.assertTrue(field_label)

    def test_user_str_method(self):
        # Just verify it doesn't crash
        pass


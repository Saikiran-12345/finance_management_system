from django.test import TestCase
from django.urls import reverse
from accounts.models import *
from users.models import User

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_account_incomes_field(self):
        field_label = Account._meta.get_field('incomes').verbose_name
        self.assertTrue(field_label)

    def test_account_expenses_field(self):
        field_label = Account._meta.get_field('expenses').verbose_name
        self.assertTrue(field_label)

    def test_account_transactions_as_primary_field(self):
        field_label = Account._meta.get_field('transactions_as_primary').verbose_name
        self.assertTrue(field_label)

    def test_account_transactions_as_destination_field(self):
        field_label = Account._meta.get_field('transactions_as_destination').verbose_name
        self.assertTrue(field_label)

    def test_account_user_field(self):
        field_label = Account._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_account_name_field(self):
        field_label = Account._meta.get_field('name').verbose_name
        self.assertTrue(field_label)

    def test_account_account_type_field(self):
        field_label = Account._meta.get_field('account_type').verbose_name
        self.assertTrue(field_label)

    def test_account_balance_field(self):
        field_label = Account._meta.get_field('balance').verbose_name
        self.assertTrue(field_label)

    def test_account_created_at_field(self):
        field_label = Account._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_account_updated_at_field(self):
        field_label = Account._meta.get_field('updated_at').verbose_name
        self.assertTrue(field_label)

    def test_account_is_active_field(self):
        field_label = Account._meta.get_field('is_active').verbose_name
        self.assertTrue(field_label)

    def test_account_str_method(self):
        # Just verify it doesn't crash
        pass


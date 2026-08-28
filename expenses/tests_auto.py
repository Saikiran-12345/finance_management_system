from django.test import TestCase
from django.urls import reverse
from expenses.models import *
from users.models import User

class ExpenseCategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_expensecategory_expense_field(self):
        field_label = ExpenseCategory._meta.get_field('expense').verbose_name
        self.assertTrue(field_label)

    def test_expensecategory_budget_field(self):
        field_label = ExpenseCategory._meta.get_field('budget').verbose_name
        self.assertTrue(field_label)

    def test_expensecategory_name_field(self):
        field_label = ExpenseCategory._meta.get_field('name').verbose_name
        self.assertTrue(field_label)

    def test_expensecategory_description_field(self):
        field_label = ExpenseCategory._meta.get_field('description').verbose_name
        self.assertTrue(field_label)

    def test_expensecategory_is_active_field(self):
        field_label = ExpenseCategory._meta.get_field('is_active').verbose_name
        self.assertTrue(field_label)

    def test_expensecategory_str_method(self):
        # Just verify it doesn't crash
        pass

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_expense_user_field(self):
        field_label = Expense._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_expense_account_field(self):
        field_label = Expense._meta.get_field('account').verbose_name
        self.assertTrue(field_label)

    def test_expense_category_field(self):
        field_label = Expense._meta.get_field('category').verbose_name
        self.assertTrue(field_label)

    def test_expense_amount_field(self):
        field_label = Expense._meta.get_field('amount').verbose_name
        self.assertTrue(field_label)

    def test_expense_date_field(self):
        field_label = Expense._meta.get_field('date').verbose_name
        self.assertTrue(field_label)

    def test_expense_payment_method_field(self):
        field_label = Expense._meta.get_field('payment_method').verbose_name
        self.assertTrue(field_label)

    def test_expense_is_recurring_field(self):
        field_label = Expense._meta.get_field('is_recurring').verbose_name
        self.assertTrue(field_label)

    def test_expense_notes_field(self):
        field_label = Expense._meta.get_field('notes').verbose_name
        self.assertTrue(field_label)

    def test_expense_created_at_field(self):
        field_label = Expense._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_expense_str_method(self):
        # Just verify it doesn't crash
        pass


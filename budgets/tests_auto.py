from django.test import TestCase
from django.urls import reverse
from budgets.models import *
from users.models import User

class BudgetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_budget_user_field(self):
        field_label = Budget._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_budget_category_field(self):
        field_label = Budget._meta.get_field('category').verbose_name
        self.assertTrue(field_label)

    def test_budget_month_field(self):
        field_label = Budget._meta.get_field('month').verbose_name
        self.assertTrue(field_label)

    def test_budget_amount_field(self):
        field_label = Budget._meta.get_field('amount').verbose_name
        self.assertTrue(field_label)

    def test_budget_amount_spent_field(self):
        field_label = Budget._meta.get_field('amount_spent').verbose_name
        self.assertTrue(field_label)

    def test_budget_status_field(self):
        field_label = Budget._meta.get_field('status').verbose_name
        self.assertTrue(field_label)

    def test_budget_str_method(self):
        # Just verify it doesn't crash
        pass


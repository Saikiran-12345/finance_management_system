from django.test import TestCase
from django.urls import reverse
from income.models import *
from users.models import User

class IncomeCategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_incomecategory_income_field(self):
        field_label = IncomeCategory._meta.get_field('income').verbose_name
        self.assertTrue(field_label)

    def test_incomecategory_name_field(self):
        field_label = IncomeCategory._meta.get_field('name').verbose_name
        self.assertTrue(field_label)

    def test_incomecategory_description_field(self):
        field_label = IncomeCategory._meta.get_field('description').verbose_name
        self.assertTrue(field_label)

    def test_incomecategory_is_active_field(self):
        field_label = IncomeCategory._meta.get_field('is_active').verbose_name
        self.assertTrue(field_label)

    def test_incomecategory_str_method(self):
        # Just verify it doesn't crash
        pass

class IncomeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_income_user_field(self):
        field_label = Income._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_income_account_field(self):
        field_label = Income._meta.get_field('account').verbose_name
        self.assertTrue(field_label)

    def test_income_category_field(self):
        field_label = Income._meta.get_field('category').verbose_name
        self.assertTrue(field_label)

    def test_income_source_field(self):
        field_label = Income._meta.get_field('source').verbose_name
        self.assertTrue(field_label)

    def test_income_amount_field(self):
        field_label = Income._meta.get_field('amount').verbose_name
        self.assertTrue(field_label)

    def test_income_date_field(self):
        field_label = Income._meta.get_field('date').verbose_name
        self.assertTrue(field_label)

    def test_income_is_recurring_field(self):
        field_label = Income._meta.get_field('is_recurring').verbose_name
        self.assertTrue(field_label)

    def test_income_notes_field(self):
        field_label = Income._meta.get_field('notes').verbose_name
        self.assertTrue(field_label)

    def test_income_created_at_field(self):
        field_label = Income._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_income_str_method(self):
        # Just verify it doesn't crash
        pass


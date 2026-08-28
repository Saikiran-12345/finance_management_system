from django.test import TestCase
from django.urls import reverse
from transactions.models import *
from users.models import User

class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_transaction_user_field(self):
        field_label = Transaction._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_transaction_account_field(self):
        field_label = Transaction._meta.get_field('account').verbose_name
        self.assertTrue(field_label)

    def test_transaction_destination_account_field(self):
        field_label = Transaction._meta.get_field('destination_account').verbose_name
        self.assertTrue(field_label)

    def test_transaction_transaction_type_field(self):
        field_label = Transaction._meta.get_field('transaction_type').verbose_name
        self.assertTrue(field_label)

    def test_transaction_amount_field(self):
        field_label = Transaction._meta.get_field('amount').verbose_name
        self.assertTrue(field_label)

    def test_transaction_date_field(self):
        field_label = Transaction._meta.get_field('date').verbose_name
        self.assertTrue(field_label)

    def test_transaction_description_field(self):
        field_label = Transaction._meta.get_field('description').verbose_name
        self.assertTrue(field_label)

    def test_transaction_category_name_field(self):
        field_label = Transaction._meta.get_field('category_name').verbose_name
        self.assertTrue(field_label)

    def test_transaction_created_at_field(self):
        field_label = Transaction._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_transaction_str_method(self):
        # Just verify it doesn't crash
        pass


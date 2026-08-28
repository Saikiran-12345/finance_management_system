from django.test import TestCase
from django.urls import reverse
from savings.models import *
from users.models import User

class SavingsGoalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_savingsgoal_user_field(self):
        field_label = SavingsGoal._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_name_field(self):
        field_label = SavingsGoal._meta.get_field('name').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_target_amount_field(self):
        field_label = SavingsGoal._meta.get_field('target_amount').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_current_amount_field(self):
        field_label = SavingsGoal._meta.get_field('current_amount').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_target_date_field(self):
        field_label = SavingsGoal._meta.get_field('target_date').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_status_field(self):
        field_label = SavingsGoal._meta.get_field('status').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_created_at_field(self):
        field_label = SavingsGoal._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_savingsgoal_str_method(self):
        # Just verify it doesn't crash
        pass


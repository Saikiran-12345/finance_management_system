from django.test import TestCase
from django.urls import reverse
from users.models import User
from .models import SavingsGoal

class SavingsGoalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        # We might need additional setup depending on the model, this is a base
        
    def test_list_view_unauthenticated(self):
        response = self.client.get(reverse('savings:savingsgoal-list'))
        self.assertEqual(response.status_code, 302) # Redirect to login
        
    def test_list_view_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('savings:savingsgoal-list'))
        self.assertEqual(response.status_code, 200)

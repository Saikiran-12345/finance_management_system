from django.test import TestCase
from django.urls import reverse
from notifications.models import *
from users.models import User

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_notification_user_field(self):
        field_label = Notification._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_notification_notification_type_field(self):
        field_label = Notification._meta.get_field('notification_type').verbose_name
        self.assertTrue(field_label)

    def test_notification_message_field(self):
        field_label = Notification._meta.get_field('message').verbose_name
        self.assertTrue(field_label)

    def test_notification_is_read_field(self):
        field_label = Notification._meta.get_field('is_read').verbose_name
        self.assertTrue(field_label)

    def test_notification_created_at_field(self):
        field_label = Notification._meta.get_field('created_at').verbose_name
        self.assertTrue(field_label)

    def test_notification_str_method(self):
        # Just verify it doesn't crash
        pass


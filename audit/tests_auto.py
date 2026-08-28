from django.test import TestCase
from django.urls import reverse
from audit.models import *
from users.models import User

class AuditLogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
    
    def test_auditlog_user_field(self):
        field_label = AuditLog._meta.get_field('user').verbose_name
        self.assertTrue(field_label)

    def test_auditlog_action_field(self):
        field_label = AuditLog._meta.get_field('action').verbose_name
        self.assertTrue(field_label)

    def test_auditlog_module_field(self):
        field_label = AuditLog._meta.get_field('module').verbose_name
        self.assertTrue(field_label)

    def test_auditlog_description_field(self):
        field_label = AuditLog._meta.get_field('description').verbose_name
        self.assertTrue(field_label)

    def test_auditlog_timestamp_field(self):
        field_label = AuditLog._meta.get_field('timestamp').verbose_name
        self.assertTrue(field_label)

    def test_auditlog_str_method(self):
        # Just verify it doesn't crash
        pass


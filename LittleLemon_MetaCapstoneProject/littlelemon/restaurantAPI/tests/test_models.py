from django.test import TestCase
from .models import Menu


# Create your tests here.

class MenuItemTest(TestCase):
    def test_string_representation(self):
        item = Menu.objects.create(title="Test Item", price=10.00)
        self.assertEqual(item, "Test Item : 10.00")
from django.test import TestCase
from .models import Menu
from .serializers import MenuItemSerializer

# Create your tests here.


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Test Item 1", price=10.00, inventory=10)
        Menu.objects.create(title="Test Item 2", price=20.00, inventory=20)
        Menu.objects.create(title="Test Item 3", price=30.00, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(serializer.data, [
            {'id': items[0].id, 'title': 'Test Item 1', 'price': '10.00', 'inventory': 10},
            {'id': items[1].id, 'title': 'Test Item 2', 'price': '20.00', 'inventory': 20},
            {'id': items[2].id, 'title': 'Test Item 3', 'price': '30.00', 'inventory': 30},
        ])
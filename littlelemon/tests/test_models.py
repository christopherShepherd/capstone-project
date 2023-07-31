from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="icecream", price=Decimal('80.00'), inventory=100)
        itemstr = str(item)
        self.assertEqual(itemstr, "icecream : 80.00")